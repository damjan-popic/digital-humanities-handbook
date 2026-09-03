"""Small, auditable graph calculations; standard library only, not for large graphs."""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations


def partitions(nodes):
    if not nodes:
        yield ()
        return
    first, *rest = nodes
    for partition in partitions(tuple(rest)):
        yield ((first,), *partition)
        for index in range(len(partition)):
            yield (*partition[:index], (first, *partition[index]), *partition[index + 1:])


def communities(nodes, edges):
    """Exact unweighted undirected modularity, resolution 1; retain all ties."""
    if len(nodes) > 6:
        return {'method': 'not applied to bipartite graph'}
    edges = sorted(set(tuple(sorted(edge)) for edge in edges))
    degree = {node: sum(node in edge for edge in edges) for node in nodes}
    if not edges:
        return {'method': 'undefined for zero edges', 'partitions': []}
    m = len(edges)
    best, winners = Fraction(-2), set()
    for partition in partitions(tuple(sorted(nodes))):
        score = Fraction(0)
        for group in partition:
            inside = sum(u in group and v in group for u, v in edges)
            volume = sum(degree[node] for node in group)
            score += Fraction(inside, m) - Fraction(volume, 2 * m) ** 2
        canonical = tuple(sorted(tuple(sorted(group)) for group in partition))
        if score > best:
            best, winners = score, {canonical}
        elif score == best:
            winners.add(canonical)
    return {'method': 'exact unweighted undirected modularity; resolution=1; all ties',
            'modularity': float(best), 'partitions': sorted(winners)}


def graph_metrics(nodes, edges, directed=False):
    """Unit-length paths; raw betweenness; outgoing harmonic closeness/(N-1)."""
    edges = sorted(set(tuple(edge) if directed else tuple(sorted(edge)) for edge in edges))
    adjacent = {node: set() for node in nodes}
    for source, target in edges:
        adjacent[source].add(target)
        if not directed:
            adjacent[target].add(source)
    betweenness = dict.fromkeys(nodes, 0.0)
    harmonic = {}
    for source in nodes:
        stack, predecessors = [], {node: [] for node in nodes}
        paths, distance = dict.fromkeys(nodes, 0), {source: 0}
        paths[source] = 1
        queue = deque([source])
        while queue:
            node = queue.popleft()
            stack.append(node)
            for neighbor in sorted(adjacent[node]):
                if neighbor not in distance:
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
                if distance[neighbor] == distance[node] + 1:
                    paths[neighbor] += paths[node]
                    predecessors[neighbor].append(node)
        harmonic[source] = sum(1 / length for length in distance.values() if length) / max(1, len(nodes) - 1)
        dependency = dict.fromkeys(nodes, 0.0)
        while stack:
            node = stack.pop()
            for previous in predecessors[node]:
                dependency[previous] += paths[previous] / paths[node] * (1 + dependency[node])
            if node != source:
                betweenness[node] += dependency[node]
    if not directed:
        betweenness = {node: value / 2 for node, value in betweenness.items()}
    weak = {node: set(adjacent[node]) for node in nodes}
    for source, target in edges:
        weak[target].add(source)
    unseen, components = set(nodes), []
    while unseen:
        queue, component = [min(unseen)], set()
        while queue:
            node = queue.pop()
            if node not in component:
                component.add(node)
                queue.extend(weak[node] - component)
        unseen -= component
        components.append(sorted(component))
    metrics = []
    for node in sorted(nodes):
        incoming = sum(node == v for _, v in edges) if directed else len(adjacent[node])
        metrics.append({'node': node, 'degree': len(adjacent[node]) + (incoming if directed else 0),
                        'in_degree': incoming, 'out_degree': len(adjacent[node]),
                        'betweenness_raw': round(betweenness[node], 6),
                        'harmonic_closeness': round(harmonic[node], 6)})
    return {'node_count': len(nodes), 'edge_count': len(edges), 'directed': directed,
            'components': components, 'metrics': metrics, 'communities': communities(nodes, edges)}


def compare(root, output, read_csv, write_csv):
    documents = {row['document_id']: row for row in read_csv(root / 'input/documents.csv')}
    people = [row['entity_id'] for row in read_csv(root / 'input/entities.csv') if row['kind'] == 'person']
    participation = read_csv(root / 'input/participation.csv')
    by_document = defaultdict(list)
    for row in participation:
        by_document[row['document_id']].append(row)
    result = {}
    bipartite = [(row['person_id'], row['document_id']) for row in participation]
    result['bipartite'] = graph_metrics(people + list(documents), bipartite)
    write_csv(output / 'bipartite-edges.csv', participation)
    support = defaultdict(list)
    for document, participants in sorted(by_document.items()):
        for pair in combinations(sorted({row['person_id'] for row in participants}), 2):
            support[pair].append(document)
    evidence = [{'person_a': a, 'person_b': b, 'document_id': doc,
                 'source_locator': documents[doc]['source_locator'], 'synthetic': 'true'}
                for (a, b), docs in sorted(support.items()) for doc in docs]
    write_csv(output / 'projection-evidence.csv', evidence)
    for threshold in (1, 2, 3):
        selected = [pair for pair, docs in sorted(support.items()) if len(docs) >= threshold]
        name = f'projection_t{threshold}'
        result[name] = graph_metrics(people, selected)
        write_csv(output / f'{name}-edges.csv',
                  [{'person_a': a, 'person_b': b, 'weight_documents': len(support[a, b]),
                    'evidence_ids': '|'.join(support[a, b]), 'synthetic': 'true'} for a, b in selected])
    no_press = [pair for pair, docs in sorted(support.items()) if any(doc != 'SYN-D5' for doc in docs)]
    result['without_press_list'] = graph_metrics(people, no_press)
    fractional = {pair: sum(Fraction(1, len(by_document[doc]) - 1) for doc in docs)
                  for pair, docs in support.items()}
    result['fractional_ge_1'] = graph_metrics(people, [pair for pair in sorted(fractional) if fractional[pair] >= 1])
    write_csv(output / 'fractional-weights.csv',
              [{'person_a': a, 'person_b': b, 'weight': float(value)}
               for (a, b), value in sorted(fractional.items())])
    correspondence = []
    for document, rows in sorted(by_document.items()):
        if documents[document]['genre'] != 'letter':
            continue
        senders = [row for row in rows if row['role'] == 'sender']
        recipients = [row for row in rows if row['role'] == 'recipient']
        for sender in senders:
            for recipient in recipients:
                correspondence.append({'source': sender['person_id'], 'target': recipient['person_id'],
                                       'document_id': document, 'confidence': recipient['confidence'],
                                       'date_start': documents[document]['date_start'],
                                       'date_end': documents[document]['date_end'],
                                       'date_kind': 'event_window', 'relation': 'asserted_correspondence',
                                       'source_locator': documents[document]['source_locator'], 'synthetic': 'true'})
    write_csv(output / 'correspondence-edges.csv', correspondence)
    for name, rows in [('correspondence', correspondence),
                       ('correspondence_certain', [row for row in correspondence if row['confidence'] == 'certain'])]:
        result[name] = graph_metrics(people, [(row['source'], row['target']) for row in rows], directed=True)
    result['missing_D6'] = graph_metrics(people, [pair for pair, docs in sorted(support.items())
                                                if sum(doc != 'SYN-D6' for doc in docs) >= 2])
    for name, graph in result.items():
        write_csv(output / f'{name}-metrics.csv', graph['metrics'])
    return result

"""Affine pilot and deliberately synthetic boundary sensitivity; no GIS dependency."""
import math


def interval_intersection(left_start, left_end, right_start, right_end):
    """Return a half-open intersection, or None when intervals do not overlap."""
    start, end = max(left_start, right_start), min(left_end, right_end)
    return (start, end) if start < end else None


def solve(matrix, vector):
    augmented = [list(row) + [value] for row, value in zip(matrix, vector, strict=True)]
    for column in range(len(vector)):
        pivot = max(range(column, len(vector)), key=lambda row: abs(augmented[row][column]))
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        if abs(divisor) < 1e-12:
            raise ValueError('Control points do not determine an affine transformation')
        augmented[column] = [value / divisor for value in augmented[column]]
        for row in range(len(vector)):
            if row != column:
                factor = augmented[row][column]
                augmented[row] = [a - factor * b for a, b in zip(augmented[row], augmented[column], strict=True)]
    return [row[-1] for row in augmented]


def fit_affine(rows):
    # Condition the design matrix; input pixel y is positive DOWN.
    design = [[1.0, float(row['source_x_px']) / 1000, float(row['source_y_px']) / 1000] for row in rows]
    matrix = [[sum(row[i] * row[j] for row in design) for j in range(3)] for i in range(3)]
    return tuple(solve(matrix, [sum(x[i] * float(row[field]) for x, row in zip(design, rows, strict=True))
                               for i in range(3)]) for field in ('target_e_m', 'target_n_m'))


def residual(row, fit):
    point = [1, float(row['source_x_px']) / 1000, float(row['source_y_px']) / 1000]
    predicted = [sum(a * b for a, b in zip(coefficients, point, strict=True)) for coefficients in fit]
    return math.hypot(predicted[0] - float(row['target_e_m']), predicted[1] - float(row['target_n_m']))


def compare(root, output, read_csv, write_csv):
    places = read_csv(root / 'input/places.csv')
    boundaries = read_csv(root / 'input/boundaries.csv')
    sources = {row['source_id']: row for row in read_csv(root / 'input/sources.csv')}
    documents = {row['document_id']: row for row in read_csv(root / 'input/documents.csv')}
    memberships = []
    for boundary in boundaries:
        divider = float(boundary['divider_x_m'])
        for place in places:
            x = float(place['x_m'])
            uncertainty = float(place['positional_uncertainty_m'])
            memberships.append({'boundary_id': boundary['boundary_id'], 'place_id': place['place_id'],
                                'centre_membership': 'SYN-W' if x < divider else 'SYN-EAST',
                                'possible_memberships': '|'.join(region for region, allowed in
                                    [('SYN-W', x - uncertainty < divider), ('SYN-EAST', x + uncertainty >= divider)] if allowed),
                                'boundary_valid_start': boundary['valid_start'],
                                'boundary_valid_end': boundary['valid_end'],
                                'boundary_source_id': boundary['source_id'],
                                'synthetic': 'true'})
    write_csv(output / 'membership.csv', memberships)
    candidates = read_csv(root / 'input/candidates.csv')
    names = read_csv(root / 'input/toponyms.csv')
    candidate_rows = []
    for membership in memberships:
        for candidate in candidates:
            if candidate['place_id'] != membership['place_id']:
                continue
            mention = documents[candidate['source_id']]
            for name in names:
                if name['place_id'] != candidate['place_id']:
                    continue
                overlap = interval_intersection(membership['boundary_valid_start'], membership['boundary_valid_end'],
                                                name['valid_start'], name['valid_end'])
                if overlap is None:
                    continue
                candidate_rows.append({
                    'mention_id': candidate['mention_id'],
                    'mention_source_id': candidate['source_id'],
                    'mention_source_locator': sources[candidate['source_id']]['locator'],
                    'source_form': candidate['source_form'],
                    'mention_date_start': mention['date_start'],
                    'mention_date_end': mention['date_end'],
                    'mention_date_kind': mention['date_kind'],
                    'place_id': candidate['place_id'],
                    'review_status': candidate['review_status'],
                    'confidence': candidate['confidence'],
                    'evidence': candidate['evidence'],
                    'boundary_id': membership['boundary_id'],
                    'boundary_valid_start': membership['boundary_valid_start'],
                    'boundary_valid_end': membership['boundary_valid_end'],
                    'boundary_source_id': membership['boundary_source_id'],
                    'centre_membership': membership['centre_membership'],
                    'possible_memberships': membership['possible_memberships'],
                    'name_id': name['name_id'],
                    'toponym': name['name'],
                    'language': name['language'],
                    'name_context': name['context'],
                    'name_source_id': name['source_id'],
                    'name_source_locator': sources[name['source_id']]['locator'],
                    'name_valid_start': name['valid_start'],
                    'name_valid_end': name['valid_end'],
                    'comparison_interval_start': overlap[0],
                    'comparison_interval_end': overlap[1],
                    'comparison_scope': 'candidate_place_history_not_mention_duration',
                    'synthetic': 'true',
                })
    write_csv(output / 'candidate-places.csv', candidate_rows)
    gcps = read_csv(root / 'input/gcps.csv')
    fitted = [row for row in gcps if row['use'] == 'fit']
    fit = fit_affine(fitted)
    residual_rows = [{**row, 'residual_m': round(residual(row, fit), 3)} for row in gcps]
    write_csv(output / 'gcp-residuals.csv', residual_rows)
    loo = []
    for excluded in fitted:
        alternative = fit_affine([row for row in fitted if row != excluded])
        loo.append({'withheld': excluded['gcp_id'], 'check_residual_m': round(residual(excluded, alternative), 3)})
    write_csv(output / 'gcp-leave-one-out.csv', loo)
    points = [f"{row['target_e_m']},{row['target_n_m']},{row['source_x_px']},-{row['source_y_px']},{1 if row['use']=='fit' else 0},0,0,0"
              for row in gcps]
    (output / 'ljubljana-1910.points').write_text(
        'mapX,mapY,sourceX,sourceY,enable,dX,dY,residual\n' + '\n'.join(points) + '\n', encoding='utf-8')
    write_csv(output / 'current-landmarks.csv', gcps)
    def rms(role):
        rows = [row for row in gcps if row['use'] == role]
        return math.sqrt(sum(residual(row, fit) ** 2 for row in rows) / len(rows))
    return {'memberships': memberships, 'candidate_places': candidate_rows, 'affine_coefficients_scaled_pixels': fit,
            'fit_rmse_m': round(rms('fit'), 3), 'independent_check_rmse_m': round(rms('check'), 3),
            'residuals': [{'gcp_id': row['gcp_id'], 'use': row['use'], 'residual_m': row['residual_m']} for row in residual_rows],
            'leave_one_out': loo,
            'warning': 'Pilot landmark centres are not survey controls; synthetic boundaries are unrelated to this real map.'}

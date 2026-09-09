# Case-study framework display checks

Captured on 2026-09-09 from the local strict MkDocs build. The before images use
main at `a728334d2fa2d1f217ffbce20d8a1e5354692806`; after images show the phase 1
issue #27 catalogue. These are original screenshots of this handbook, not
third-party project interfaces. The repository's text/image licence applies.

Both catalogues were checked at 360, 768 and 1280 CSS pixels wide (900 pixels
high), in light and dark mode. All twelve combinations showed eleven cards,
correctly paired language links and no horizontal page overflow. Edit/source
actions remain separate from the content. Cards use the existing theme; no
CSS, client-side filtering application or navigation redesign was added.
The Slovene catalogue visibly identifies its eleven English fallback links;
it does not claim that the case pages have been translated.

## Before and after: English

| Width | Before | After |
| --- | --- | --- |
| 360 px, light | ![Old English catalogue at mobile width](before-en-360-light.png) | ![Generated English catalogue with counts and legacy status at mobile width](after-en-360-light.png) |
| 1280 px, light | ![Old English catalogue at desktop width](before-en-1280-light.png) | ![Generated English catalogue with metadata cards at desktop width](after-en-1280-light.png) |

## Before and after: Slovene

| Width | Before | After |
| --- | --- | --- |
| 360 px, light | ![Old Slovene catalogue at mobile width](before-sl-360-light.png) | ![Generated Slovene catalogue with explicit English fallback counts at mobile width](after-sl-360-light.png) |
| 1280 px, light | ![Old Slovene catalogue at desktop width](before-sl-1280-light.png) | ![Generated Slovene catalogue with localized metadata and English fallback labels at desktop width](after-sl-1280-light.png) |

## Dark-mode mobile samples

![Generated English catalogue in dark mode at 360 px](after-en-360-dark.png)

![Generated Slovene catalogue in dark mode at 360 px](after-sl-360-dark.png)

Display checks do not constitute a complete assistive-technology audit or
human Slovene-language approval. The visible machine-assisted draft notice
and the remaining translation gap are intentional.

# Tarazu brand kit

Tarazu means a weighing scale. The mark is a letter T whose beam carries two bowls: money in, money out, in balance.

## Colours
| Name | Hex | Use |
| ---- | --- | --- |
| Ink | #111111 | The T, the word, text |
| Tarazu Blue | #2457D6 | The two bowls, app icon background, links |
| White | #FFFFFF | Backgrounds, mark on blue or dark |

## Font
Inter (the wordmark in these files is already converted to outlines, so no font install is needed). Wordmark is Inter Display SemiBold, lowercase, letter spacing about -1%.

## Folder guide
- `logo/` SVG logos (use SVG on the web). `logo/png/` the same as transparent PNGs.
  - `tarazu-mark*` the T symbol alone. Variants: colour, black, white, reverse (white T and blue bowls, for dark backgrounds).
  - `tarazu-logo-horizontal*` symbol and word side by side. `tarazu-logo-stacked*` symbol above the word.
  - On a white background use the plain file. On a dark background use `-reverse` or `-white`.
- `icons/` app and browser icons.
  - `app-icon-1024.png` App Store. `play-store-512.png` Google Play. `apple-touch-icon-180.png` iPhone home screen.
  - `pwa-192.png`, `pwa-512.png`, `pwa-maskable-512.png` for the web app manifest.
  - `favicon.svg`, `favicon.ico`, `favicon-16.png`, `favicon-32.png` for browser tabs.
  - `app-icon-dark*` an alternative ink-black icon.

## Rules
- Keep clear space around the logo equal to the width of the post (the vertical stem of the T).
- Do not stretch, rotate, add shadows or gradients, or change the colours.
- Smallest size: 16 px for the icon, 24 px for the horizontal logo height.
- Do not use the bowls in blue on a blue background; use the white version.

## Web setup (Next.js / any site)
```html
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon-180.png">
<link rel="manifest" href="/manifest.webmanifest">
```
`manifest.webmanifest`:
```json
{
  "name": "Tarazu",
  "short_name": "Tarazu",
  "theme_color": "#2457D6",
  "background_color": "#FFFFFF",
  "display": "standalone",
  "icons": [
    { "src": "/pwa-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/pwa-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "/pwa-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ]
}
```

## Still to do before launch
- Search IP India's trademark register for "Tarazu" (classes 9 and 36) and check domains. Not checked yet.

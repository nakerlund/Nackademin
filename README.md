# Nackademin IoT Konnektivitet

Detta repo innehåller kursmaterial och presentationer för Nackademin IoT och Embedded Linux, genererat med [Marp](https://marp.app/) och publicerat via GitHub Pages.

## 📖 Se presentationerna online

Alla presentationer publiceras automatiskt på:

👉 [https://nakerlund.github.io/Nackademin](https://nakerlund.github.io/Nackademin)

## 🛠️ Hur fungerar det?

### Marp för Markdown-presentationer

- Slides skrivs i Markdown med [Marp](https://marp.app/)-format.
- Varje presentation ligger i `marps/<presentation>/<presentation>.md`.
- Egna teman finns i mappen `themes/`.

### Automatiserad bygg & publicering

- **GitHub Actions** workflow (`.github/workflows/build-marp.yml`) körs vid varje push till `main`.
- Workflowen använder Python och Docker för att:
  1. Hitta alla Marp-markdownfiler.
  2. Konvertera dem till HTML med Marp CLI (via Docker).
  3. Skriva om bildlänkar för GitHub Pages.
  4. Generera en indexsida med alla presentationer.
  5. Publicera mappen `docs/` till GitHub Pages.

### GitHub Pages

- Mappen `docs/` publiceras som en statisk webbplats via GitHub Pages.
- Alla slides och tillhörande bilder finns på [https://nakerlund.github.io/Nackademin](https://nakerlund.github.io/Nackademin).

## 🐳 Docker som verktyg för Marp

- Byggscriptet (`generate.py`) använder Docker för att köra Marp CLI, så du slipper installera Marp lokalt.
- Docker monterar projektmappen och kör Marp CLI i containern, så att alla Markdown-filer konverteras till HTML.
- Detta funkar på alla operativsystem där Docker är installerat.

**Exempel på Docker-kommando (används i scriptet):**

```bash
docker run --rm -v $PWD:/home/marp/app -e LANG=$LANG marpteam/marp-cli marps/binary/binary.md -o docs/binary.html
```

## 📝 Lintning och kvalitet

- Markdown-filer lintas automatiskt med [markdownlint](https://github.com/DavidAnson/markdownlint) via en separat GitHub Actions-workflow (`.github/workflows/markdown-lint.yml`).
- Lintning körs på alla brancher och pull requests för att hålla formateringen konsekvent.

## 🚀 Lokal utveckling

- Så här bygger och förhandsgranskar du slides lokalt:
  1. Installera [Docker](https://docs.docker.com/get-docker/).
  2. Kör `python generate.py` (eller med base URL för GitHub Pages-kompatibilitet).
  3. Öppna de genererade HTML-filerna i `docs/`.

## 💡 Mer info

- [Marp dokumentation](https://marp.app/)
- [GitHub Pages dokumentation](https://docs.github.com/en/pages)
- [GitHub Actions dokumentation](https://docs.github.com/en/actions)
- [markdownlint dokumentation](https://github.com/DavidAnson/markdownlint)

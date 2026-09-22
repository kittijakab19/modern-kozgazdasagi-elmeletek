# Modern Közgazdasági Elméletek — vizsgatréner

Egyoldalas tanulóalkalmazás a BGE *Modern közgazdasági elméletek* tárgyához
(Dr. Dobó Róbert előadásai, 01–03.). Kérdésbank, vizsgaformátumú igaz–hamis
blokkok, diaszámos magyarázatok és ismétlési ütemező — minden külső szolgáltatás
nélkül, egyetlen HTML fájlban.

## Mit tud

- **Gyakorlás** — 107 kérdés 9 témakörben. Minden kör főként új kérdéseket hoz:
  amit elrontottál, a következő körben visszatér, amit tudtál, 2 · 3 · 5 · 8 · 13
  kör múlva jön elő újra (Leitner-dobozos ütemezés). A kör mérete 10 / 20 / 40 /
  mind.
- **Pluszpontos kérdések** — a pluszpontos teszt kilenc feladata eredeti
  sorrendben, az eredeti pontozással (összesen 8,5 pont).
- **Tételvázlat** — mindhárom diasor szövege diánként, szó szerint, diaszámokkal.
- **Haladás** — találati arány és témakörönkénti erősség; az első próbálkozás
  számít bele.
- Világos és sötét téma, mobilbarát elrendezés. A haladás a böngésző
  `localStorage`-ában marad, szerver nem kell hozzá.

## Fájlok

| fájl | mire való |
| --- | --- |
| `modern-kozgazdasagi-elmeletek.html` | a forrásoldal (Claude Artifact formátum: `<head>`/`<body>` nélkül) |
| `index.html` | a statikus, önálló változat — ezt szolgálja ki a GitHub Pages |
| `build.py` | `index.html` előállítása a forrásból |
| `serve.py` | helyi előnézet: `http://localhost:8947`, minden újratöltésnél újraolvassa a forrást |
| `robots.txt` | a keresőmotorok kizárása |

A forrásoldalt szerkeszd, utána futtasd a buildet:

```bash
python3 build.py
```

Helyi megtekintés:

```bash
python3 serve.py
```

## Keresők kizárása

Az oldal `noindex, nofollow` metacímkét kap a buildkor, és a `robots.txt` minden
robotot kizár. A GitHub Pages linkje így nem kerül be a Google találatai közé —
aki viszont ismeri a linket, meg tudja nyitni.

## Tartalom

A kérdések és a tételvázlat a tárgy 01–03. előadásának diasoraiból készültek,
tanulási célra. Az előadásanyag szerzői joga az előadót illeti.

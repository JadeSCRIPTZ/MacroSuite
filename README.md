# JadeSCRIPTZ Macro Suite

Un singur launcher care iti da acces la doua tool-uri complet separate:

- **🎣 FishBot Pro** — macro dedicat de fishing (pixel color detection pe bobber, trage/arunca automat undita).
- **🎮 PixelKey Macro** — macro general: secvente de taste/click-uri, pixel watch-points multiple, profile, timing randomization, Dry Run, panic hotkey.

Cele doua tool-uri **nu sunt combinate** — fiecare ruleaza in fereastra proprie, cu codul si logica lui originale, neschimbate. Launcher-ul doar le deschide.

## Rulare din surse

```bash
pip install -r requirements.txt
python macro_suite.py
```

## Build .exe (Windows)

Fisierele `fishing_macro.py` si `pixelkey_macro.py` pot fi rulate si independent, la fel ca inainte. `macro_suite.py` e noul entrypoint recomandat.

Vezi `.github/workflows/build.yml` pentru build automat cu PyInstaller la fiecare tag `v*`.

## Structura

```
macro_suite.py      # launcher (UI de selectie)
fishing_macro.py     # FishBot Pro — neschimbat
pixelkey_macro.py     # PixelKey Macro — neschimbat
requirements.txt
```

Author: JadeSCRIPTZ

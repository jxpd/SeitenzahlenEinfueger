# PDF Seitenzahlen-Einfüger

Ein Python-Tool zum automatischen Einfügen von Seitenzahlen in PDF-Dokumente – optimiert für doppelseitigen Druck und Ordnerablage.

## Features

- **Doppelseitiger Druck**: Seitenzahlen werden abwechselnd positioniert (Vorderseite links, Rückseite rechts)
- **Overlay über Bildern**: Seitenzahlen werden als Annotations eingefügt und erscheinen über allen bestehenden Inhalten (auch über Stempel, Zeichnungen, etc.)
- **Kompaktes Design**: Weißer Hintergrund mit dünnem schwarzen Rahmen, dynamische Größe
- **Batch-Verarbeitung**: Verarbeitet PDFs beliebiger Länge

## Installation

```bash
# Repository klonen
git clone https://github.com/DEIN-USERNAME/SeitenzahlenEinfueger.git
cd SeitenzahlenEinfueger

# Virtuelle Umgebung erstellen (empfohlen)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# oder: .venv\Scripts\activate  # Windows

# Abhängigkeiten installieren
pip install pymupdf
```

## Verwendung

```bash
python main.py <input.pdf> [output.pdf]
```

### Beispiele

```bash
# Mit explizitem Ausgabepfad
python main.py skript.pdf skript_nummeriert.pdf

# Ausgabe wird automatisch als "skript_nummeriert.pdf" gespeichert
python main.py skript.pdf
```

## Konfiguration

Die folgenden Parameter können im Code (`main.py`) angepasst werden:

| Parameter | Standard | Beschreibung |
|-----------|----------|--------------|
| `font_size` | 11 | Schriftgröße der Seitenzahlen |
| `margin_x` | 20 | Abstand vom seitlichen Rand (in Points) |
| `margin_y` | 25 | Abstand vom oberen Rand (in Points) |

## Positionierung

Das Tool ist für Dokumente optimiert, die doppelseitig gedruckt und gelocht werden:

```
VORDERSEITE (1, 3, 5, ...)     RÜCKSEITE (2, 4, 6, ...)
┌─────────────────────┐        ┌─────────────────────┐
│ [1]                 │        │                 [2] │
│ ○                   │        │                   ○ │
│ ○    Inhalt         │        │       Inhalt      ○ │
│ ○                   │        │                   ○ │
│                     │        │                     │
└─────────────────────┘        └─────────────────────┘
  ↑ Lochrand                              Lochrand ↑
```

## Abhängigkeiten

- Python 3.8+
- [PyMuPDF](https://pymupdf.readthedocs.io/) (fitz)

## Lizenz

MIT License

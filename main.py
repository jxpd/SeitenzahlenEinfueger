#!/usr/bin/env python3
"""
Skript zum Hinzufügen von Seitenzahlen für doppelseitigen Druck.

Vorderseite (ungerade Seiten): Seitenzahl links oben (innen)
Rückseite (gerade Seiten): Seitenzahl rechts oben (innen)

Die Seitenzahlen werden als FreeText-Annotation eingefügt, damit sie
ÜBER eventuellen Stamp/Ink-Annotations liegen.

Verwendung:
    pip install pymupdf
    python main.py input.pdf output.pdf
"""

import sys
import fitz  # PyMuPDF


def add_page_numbers(input_path: str, output_path: str):
    """
    Fügt Seitenzahlen als FreeText-Annotations hinzu.
    """
    print(f"\n{'#' * 60}")
    print(f"# PDF Seitenzahlen-Tool (Annotation-Methode)")
    print(f"{'#' * 60}")
    print(f"\nEingabe: {input_path}")
    print(f"Ausgabe: {output_path}")
    
    doc = fitz.open(input_path)
    total_pages = len(doc)
    print(f"\n>>> Dokument hat {total_pages} Seiten\n")
    
    # Schriftgröße
    font_size = 11
    
    # Abstände vom Rand (in Points) - näher am Heftrand
    margin_x = 20
    margin_y = 25
    
    for page_num in range(total_pages):
        page = doc[page_num]
        display_num = page_num + 1
        is_front = (display_num % 2 == 1)
        side = "Vorderseite" if is_front else "Rückseite"
        position = "links" if is_front else "rechts"
        
        # Seitengröße
        rect = page.rect
        page_width = rect.width
        
        # Text für Seitenzahl
        text = str(display_num)
        
        # Textbreite dynamisch berechnen
        actual_text_width = fitz.get_text_length(text, fontname="helv", fontsize=font_size)
        box_width = actual_text_width + 6  # Kleiner Padding
        box_height = font_size + 2
        
        # Position berechnen - OBEN (y von oben gemessen in PyMuPDF)
        y_top = margin_y
        y_bottom = margin_y + box_height
        
        if is_front:
            # Vorderseite: links oben (nah am Heftrand)
            x_left = margin_x
            x_right = margin_x + box_width
        else:
            # Rückseite: rechts oben (nah am Heftrand)
            x_left = page_width - margin_x - box_width
            x_right = page_width - margin_x
        
        # Rechteck für die Annotation
        annot_rect = fitz.Rect(x_left, y_top, x_right, y_bottom)
        
        # FreeText Annotation erstellen
        annot = page.add_freetext_annot(
            rect=annot_rect,
            text=text,
            fontsize=font_size,
            fontname="helv",  # Helvetica
            text_color=(0, 0, 0),  # Schwarz
            fill_color=(1, 1, 1),  # Weißer Hintergrund
            align=fitz.TEXT_ALIGN_CENTER,  # Zentriert
        )
        
        # Annotation-Flags setzen: Print=True, damit es gedruckt wird
        annot.set_flags(fitz.PDF_ANNOT_IS_PRINT)
        annot.update()
        
        # Rahmen als separate Rechteck-Annotation hinzufügen
        border_annot = page.add_rect_annot(annot_rect)
        border_annot.set_colors(stroke=(0, 0, 0))  # Schwarzer Rahmen
        border_annot.set_border(width=0.5)
        border_annot.set_flags(fitz.PDF_ANNOT_IS_PRINT)
        border_annot.update()
        
        print(f"  Seite {display_num}/{total_pages}: {side} → Seitenzahl {position} oben")
    
    # Speichern
    print(f"\nSpeichere...")
    doc.save(output_path, garbage=4, deflate=True)
    doc.close()
    
    print(f"✓ Fertig! Ausgabe: {output_path}\n")


def main():
    if len(sys.argv) < 2:
        print("Verwendung: python main.py <input.pdf> [output.pdf]")
        print("\nBeispiel:")
        print("  python main.py skript.pdf skript_mit_seitenzahlen.pdf")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        if input_path.lower().endswith(".pdf"):
            output_path = input_path[:-4] + "_nummeriert.pdf"
        else:
            output_path = input_path + "_nummeriert.pdf"
    
    add_page_numbers(input_path, output_path)


if __name__ == "__main__":
    main()

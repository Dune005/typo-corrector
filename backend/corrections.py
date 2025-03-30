import re

def apply_corrections(text):
    """
    Wendet grundlegende typografische Korrekturen auf den gegebenen Text an.

    Args:
        text (str): Der zu korrigierende Text.

    Returns:
        str: Der korrigierte Text.
    """
    if not isinstance(text, str):
        return "" # Oder einen Fehler werfen, je nach Anforderung

    # 1. Doppelte Leerzeichen entfernen
    corrected_text = re.sub(r' +', ' ', text)

    # 2. Deutsche typografische Anführungszeichen (vereinfachte Version)
    #    Ersetzt " oder ” am Wortanfang oder nach Leerzeichen/Zeilenanfang mit „
    corrected_text = re.sub(r'(^|\s)["”](?=\S)', r'\1„', corrected_text)
    #    Ersetzt " oder ” am Wortende oder vor Leerzeichen/Zeilenende/Satzzeichen mit “
    corrected_text = re.sub(r'(\S)["”](?=\s|\.|,|;|!|\?|$)', r'\1“', corrected_text)

    # 3. Apostroph korrigieren (' -> ’)
    #    Ersetzt ' zwischen Buchstaben oder Zahlen (z.B. geht's, '90s)
    corrected_text = re.sub(r"(\w)'(\w)", r"\1’\2", corrected_text)
    #    Ersetzt ' am Anfang eines Wortes (selten, aber möglich, z.B. 'ne)
    #    Hinweis: Diese Regel ist spezifischer als nur (r"'", "’")
    corrected_text = re.sub(r"(\s)'(\w)", r"\1’\2", corrected_text)

    # 4. Ellipse (...) ersetzen durch typografische Ellipse (…)
    corrected_text = re.sub(r'\.\.\.', '…', corrected_text)

    # 5. Häufige Encoding-Fehler korrigieren (Beispiele)
    #    Hinweis: Eine robustere Lösung würde Bibliotheken wie ftfy verwenden.
    encoding_map = {
        'Ã¤': 'ä', 'Ã¶': 'ö', 'Ã¼': 'ü', 'ÃŸ': 'ß',
        'Ã„': 'Ä', 'Ã–': 'Ö', 'Ãœ': 'Ü'
        # Weitere nach Bedarf hinzufügen
    }
    for wrong, right in encoding_map.items():
        corrected_text = corrected_text.replace(wrong, right) # Einfaches replace ist hier oft ausreichend

    # 6. Einfache PDF-Zeilenumbrüche entfernen (Wort-Trennstrich-Umbruch)
    #    Fügt Wortteile zusammen, die durch einen Bindestrich am Zeilenende getrennt wurden.
    corrected_text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', corrected_text)

    # 7. Ersetzt ß durch ss
    corrected_text = corrected_text.replace('ß', 'ss')

    # Weitere Regeln können hier hinzugefügt werden

    return corrected_text.strip() # Entfernt führende/nachfolgende Leerzeichen

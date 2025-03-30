import re

def apply_corrections(text):
    """
    Wendet typografische Korrekturen auf den gegebenen Text an,
    mit Fokus auf Schweizer Konventionen und logischer Reihenfolge.

    Args:
        text (str): Der zu korrigierende Text.

    Returns:
        str: Der korrigierte Text.
    """
    # Eingabe validieren
    if not isinstance(text, str):
        # Stellt sicher, dass wir einen String haben, gibt leeren String zurück wenn nicht.
        # Alternativ könnte hier ein TypeError geworfen werden.
        return ""

    # *** KORREKTUR: Initialisierung NACH dem if-Block und VOR der ersten Verwendung ***
    # Initialisiere corrected_text mit dem Originaltext, damit es immer definiert ist.
    corrected_text = text

    # --- BLOCK 1: Encoding-Korrekturen (Früh ausführen) ---
    #    Behebt häufige Probleme, die durch falsche Zeichenkodierung entstehen.
    encoding_map = {
        'Ã¤': 'ä', 'Ã¶': 'ö', 'Ã¼': 'ü', 'ÃŸ': 'ß',
        'Ã„': 'Ä', 'Ã–': 'Ö', 'Ãœ': 'Ü',
        'â‚¬': '€', 'â„¢': '™', 'Â©': '©', 'Â®': '®' # Einige weitere Beispiele
        # Weitere nach Bedarf hinzufügen
    }
    for wrong, right in encoding_map.items():
        # Hier wird corrected_text zum ersten Mal gelesen und geschrieben
        corrected_text = corrected_text.replace(wrong, right)

    # --- BLOCK 2: Grundlegende Leerzeichen-Korrekturen ---
    # 2.1 Mehrfache Leerzeichen zu einem einzigen normalisieren. Wichtige Basis.
    corrected_text = re.sub(r' +', ' ', corrected_text)

    # --- BLOCK 4: Anführungs- und Schlusszeichen (Schweizer Stil: « » und ‘ ’) --- # BLOCK VERSCHOBEN!
    #    Ersetzt gerade und deutsche/englische typografische Zeichen.

    # 4.1 Doppelte Anführungszeichen (Primary Quotes)
    double_quotes_pattern = r'["„“”]' # Gerade ", deutsche „“, englische “ ”
    # 4.1.1 Öffnende doppelte Guillemets («) - Korrigiert: ohne variablen Lookbehind
    #       Erfasst das vorhergehende Zeichen/Anfang (Gruppe 1) und fügt es wieder ein.
    corrected_text = re.sub(r'(^|\s|[\(\{\[])(' + double_quotes_pattern + ')', r'\1«', corrected_text)
    # 4.1.2 Schliessende doppelte Guillemets (») - NEU: Spezifischere Regel
    #       Ersetzt ein doppeltes Anführungszeichen, wenn es nach einem Nicht-Leerzeichen
    #       und vor einem Leerzeichen, Satzzeichen oder dem Ende steht.
    corrected_text = re.sub(r'(\S)(' + double_quotes_pattern + r')(?=[\s.,;!?]|$)', r'\1»', corrected_text)
    #       Hinweis: Diese Regel ist immer noch eine Heuristik und könnte in verschachtelten Fällen versagen.

    # 4.2 Einfache Anführungszeichen (Secondary/Nested Quotes) - ÜBERARBEITET
    #     WICHTIG: Diese Regeln laufen NACH den Apostroph-Regeln!
    # 4.2.1 Schliessendes einfaches typografisches Anführungszeichen (’ U+2019)
    #       Sucht explizit nach dem geraden ' nach einem Nicht-Leerzeichen und vor Leerzeichen/Satzzeichen/Ende.
    corrected_text = re.sub(r"(\S)'(?=[\s.,;!?]|$)", r"\1’", corrected_text)
    # 4.2.2 Öffnendes einfaches typografisches Anführungszeichen (‘ U+2018)
    #       Sucht explizit nach dem geraden ' am Anfang oder nach Leerzeichen/Klammer.
    corrected_text = re.sub(r"(^|\s|[\(\{\[«])'", r"\1‘", corrected_text)
    #       Hinweis: Die Reihenfolge (erst schliessend, dann öffnend) kann helfen, Konflikte zu vermeiden.

    # --- BLOCK 3: Apostroph-Korrekturen (NACH Anführungszeichen!) --- # BLOCK VERSCHOBEN!
    #    Ersetzt verbleibende gerade Schreibmaschinen-Apostrophe durch typografische Apostrophe (’ U+2019).
    #    Läuft nach den Anführungszeichen, um sicherzustellen, dass nur echte Apostrophe erfasst werden.
    # 3.1 Apostroph zwischen Buchstaben/Zahlen (z.B. geht's, '90s).
    corrected_text = re.sub(r"(\w)'(\w)", r"\1’\2", corrected_text)
    # 3.2 Apostroph am Wortanfang nach einem Leerzeichen (z.B. 'ne Idee -> ’ne Idee).
    #     Diese Regel ist jetzt weniger kritisch, da Anführungszeichen bereits behandelt wurden.
    corrected_text = re.sub(r"(\s)'(\w)", r"\1’\2", corrected_text)
    # 3.3 Regel für Apostroph am Zeilenanfang entfernt, da sie mit öffnenden einfachen Anführungszeichen kollidiert.
    # corrected_text = re.sub(r"^'(\w)", r"’\1", corrected_text) # ENTFERNT

    # --- BLOCK 5: Spezifische Leerzeichen-Anpassungen (NACH Zeichenersetzung) ---
    #    Passt Leerzeichen basierend auf den nun korrekten Zeichen an.

    # 5.1 Einzelnes Leerzeichen um Et-Zeichen (&), wenn es Wörter verbindet.
    corrected_text = re.sub(r'(\w)\s*&\s*(\w)', r'\1 & \2', corrected_text)
    # 5.2 Einzelnes Leerzeichen um Bis-Strich (Gedankenstrich – U+2013) bei Bereichen.
    corrected_text = re.sub(r'([.\d/\-])\s*(–)\s*([.\d/\-])', r'\1 \2 \3', corrected_text)
    # 5.3 KEIN Leerzeichen vor Prozent/Promille (%, ‰) nach einer Zahl.
    corrected_text = re.sub(r'(\d)\s+([%‰])', r'\1\2', corrected_text)
    # 5.4 Einzelnes Leerzeichen vor Einheiten/Währungssymbolen nach einer Zahl.
    units_pattern = r'\b(?:CHF|Fr|SFr|EUR|USD|km|kg|g|mg|m|cm|mm|m²|ha|L|ml|h|min|s|B|KB|MB|GB|TB)\b'
    corrected_text = re.sub(r'(\d)\s*(' + units_pattern + ')', r'\1 \2', corrected_text)
    # 5.5 Einzelnes Leerzeichen nach Abkürzungspunkten (1-3 Buchstaben) vor nächstem Wort.
    corrected_text = re.sub(r'(\b[a-zA-Z]{1,3}\.)(\w)', r'\1 \2', corrected_text)
    # 5.6 KEINE Leerzeichen direkt innerhalb von Schweizer Guillemets («Text»).
    corrected_text = re.sub(r'«\s+', '«', corrected_text)
    corrected_text = re.sub(r'\s+»', '»', corrected_text)
    # 5.7 KEINE Leerzeichen um Punkte in Datumsangaben.
    corrected_text = re.sub(r'(\d)\s*\.\s*(\d)', r'\1.\2', corrected_text)








    # --- BLOCK 6: Sonstige Korrekturen ---

    # 6.1 Ellipse (...) ersetzen durch typografische Ellipse (…) U+2026.
    corrected_text = re.sub(r'\.\s*\.\s*\.', '…', corrected_text)
    corrected_text = re.sub(r'\.\.\.', '…', corrected_text)

    # 6.2 Einfache PDF-Zeilenumbrüche entfernen (Wort-Trennstrich-Umbruch)
    corrected_text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', corrected_text)

    # NEUE REGEL: 6.3 Entfernt unerwünschte Trennstriche innerhalb von Wörtern
    # Behält Bindestriche vor Grossbuchstaben bei.
    corrected_text = re.sub(r'(\w)-([a-zäöüß])', r'\1\2', corrected_text)

    # 6.3 Ersetzt ß durch ss (Schweizer Rechtschreibung).
    corrected_text = corrected_text.replace('ß', 'ss')

    # 6.4 Einfache PDF-Zeilenumbrüche entfernen (Wort-Trennstrich-Umbruch)
#     Fügt Wortteile zusammen, die durch einen Bindestrich (-) am Zeilenende (\n) getrennt wurden.
    corrected_text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', corrected_text)
#     Optional: Auch Umbrüche ohne Trennstrich entfernen, wenn es sinnvolle Sätze ergibt (komplexer!)










    # --- BLOCK 7: Finale Bereinigung ---
    # 7.1 Entfernt führende/nachfolgende Leerzeichen vom gesamten Text.
    corrected_text = corrected_text.strip()

    # Rückgabe des vollständig korrigierten Textes
    return corrected_text

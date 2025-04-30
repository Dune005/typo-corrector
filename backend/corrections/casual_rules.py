import re

def apply_corrections(text, preserve_formatting=False):
    """
    Wendet typografische Korrekturen auf den gegebenen Text an,
    mit Fokus auf Schweizer Konventionen und logischer Reihenfolge.

    Args:
        text (str): Der zu korrigierende Text.
        preserve_formatting (bool, optional): Wenn True, werden Zeilenumbrüche beibehalten.
                                             Defaults to False.

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

    # --- BLOCK 10: Datumsformatierung (Schweizer Stil) ---
    # WICHTIG: Datumsformatierung muss VOR der Zahlenformatierung (Block 8) erfolgen!
    #    Formatierungsregeln für Datumsangaben gemäß Schweizer Typografie-Konventionen

    # Liste der Monatsbezeichnungen für die Erkennung
    months_de = r'(?:Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)'
    # Liste der Wochentagsbezeichnungen für die Erkennung
    weekdays_de = r'(?:Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag)'
    # Abkürzungen der Wochentage
    weekdays_abbr_de = r'(?:Mo|Di|Mi|Do|Fr|Sa|So)\.?'

    # 10.1 Konsistente Punktsetzung im numerischen Datum (DD.MM.YYYY)
    # Stellt sicher, dass Punkte nach Tag und Monat stehen: 03.02.2021
    corrected_text = re.sub(r'\b(\d{1,2})[-/](\d{1,2})[-/](\d{2}|\d{4})\b', r'\1.\2.\3', corrected_text)

    # 10.2 Führende Nullen bei Tag und Monat ergänzen
    # Beispiel: 3.2.2021 -> 03.02.2021
    corrected_text = re.sub(r'\b(\d)\.(\d{1,2})\.(\d{2}|\d{4})\b', r'0\1.\2.\3', corrected_text) # Führende Null für Tag
    corrected_text = re.sub(r'\b(\d{2})\.(\d)\.(\d{2}|\d{4})\b', r'\1.0\2.\3', corrected_text) # Führende Null für Monat

    # 10.3 Führende Null bei Tag ergänzen wenn nötig (Kombination aus 10.1 und 10.2)
    # Beispiel: 3.02.2021 -> 03.02.2021
    corrected_text = re.sub(r'\b(\d)\.(\d{2})\.(\d{2}|\d{4})\b', r'0\1.\2.\3', corrected_text)

    # 10.4 Jahreszahl auf vier Stellen erweitern, wenn nur zwei Stellen vorhanden
    # Beispiel: 03.02.21 -> 03.02.2021
    # Regel für Jahreszahlen: < 50 -> 20xx, >= 50 -> 19xx (Annahme für gegenwärtigen Zeitbezug)
    corrected_text = re.sub(r'\b(\d{1,2})\.(\d{1,2})\.(\d{2})\b',
                          lambda m: f"{m.group(1)}.{m.group(2)}.20{m.group(3)}" if int(m.group(3)) < 50
                          else f"{m.group(1)}.{m.group(2)}.19{m.group(3)}", corrected_text)

    # 10.5 Korrektur für Datumsangaben mit Wochentag
    # Beispiel: Mittwoch 03.02.2021 -> Mittwoch, 03.02.2021
    corrected_text = re.sub(r'\b(' + weekdays_de + r')\s+(\d{1,2}\.\d{1,2}\.\d{2,4})\b', r'\1, \2', corrected_text)
    corrected_text = re.sub(r'\b(' + weekdays_abbr_de + r')\s+(\d{1,2}\.\d{1,2}\.\d{2,4})\b', r'\1, \2', corrected_text)

    # 10.6 Korrektur für Datumsangaben mit ausgeschriebenem Monat
    # 10.6.1 Komma nach Wochentag einfügen, falls fehlend
    corrected_text = re.sub(r'\b(' + weekdays_de + r')\s+(\d{1,2})\.?\s+(' + months_de + r')\s+(\d{4}|\d{2})\b',
                          r'\1, \2. \3 \4', corrected_text)
    corrected_text = re.sub(r'\b(' + weekdays_abbr_de + r')\s+(\d{1,2})\.?\s+(' + months_de + r')\s+(\d{4}|\d{2})\b',
                          r'\1, \2. \3 \4', corrected_text)
    # NEU 10.6.2: Führende Null bei einstelligem Tag ergänzen, wenn Monatsname folgt (mit/ohne Punkt)
    #             Stellt sicher, dass das Format "0D. Monat" ist.
    corrected_text = re.sub(r'\b(\d)(?=\.?\s+' + months_de + r')', r'0\1', corrected_text) # Fügt nur die 0 hinzu
    corrected_text = re.sub(r'\b(0\d)\s+(' + months_de + r')', r'\1. \2', corrected_text) # Fügt Punkt hinzu, falls fehlt
    corrected_text = re.sub(r'\b(0\d)\.\s+(' + months_de + r')', r'\1. \2', corrected_text) # Korrigiert Leerzeichen nach Punkt

    # ALT 10.6.2 (jetzt 10.6.3): Punkt nach Tag einfügen, falls fehlend (nur wenn Tag zweistellig ist)
    corrected_text = re.sub(r'\b(\d{2})\s+(' + months_de + r')\s+(\d{4}|\d{2})\b', r'\1. \2 \3', corrected_text) # Nur für zweistellige Tage

    # ALT 10.6.3 (jetzt 10.6.4): Abkürzung der Wochentage mit Punkt, aber NUR am Ende des Wortes
    corrected_text = re.sub(r'\b(Mo|Di|Mi|Do|Fr|Sa|So)\b(?!\.)', r'\1.', corrected_text)

    # 10.7 ENTFERNT (Konflikt mit Anforderung für führende Null)
    # corrected_text = re.sub(r'\b0(\d)\. (' + months_de + r')\s+(\d{4}|\d{2})\b', r'\1. \2 \3', corrected_text)

    # ALT 10.8 (jetzt 10.7): Konsistente Formatierung von Bindestrich-Datumsangaben
    # Beispiel: 03-02-2021 -> 03.02.2021 (überschreibt teilweise 10.1, aber mit spezifischerer Regel)
    corrected_text = re.sub(r'\b(\d{1,2})-(\d{1,2})-(\d{2}|\d{4})\b', r'\1.\2.\3', corrected_text)

    # ALT 10.9 (jetzt 10.8): Inkonsistente gemischt verwendete Trenner korrigieren
    # Beispiel: 03.02/2021 oder 03/02.2021 -> 03.02.2021
    corrected_text = re.sub(r'\b(\d{1,2})\.(\d{1,2})[/-](\d{2}|\d{4})\b', r'\1.\2.\3', corrected_text)
    corrected_text = re.sub(r'\b(\d{1,2})[/-](\d{1,2})\.(\d{2}|\d{4})\b', r'\1.\2.\3', corrected_text)

    # ALT 10.10 (jetzt 10.9): Zwei- bis vierstellige Jahresangaben vereinheitlichen (für Datumsangaben ab 2000)
    # Diese Regel korrigiert Fälle, die in 10.4 nicht erfasst wurden
    corrected_text = re.sub(r'\b(\d{1,2})\.(\d{1,2})\.(\d{2})\b',
                          lambda m: f"{m.group(1)}.{m.group(2)}.20{m.group(3)}" if int(m.group(3)) < 50
                          else f"{m.group(1)}.{m.group(2)}.19{m.group(3)}", corrected_text)

    # 10.11 ENTFERNT (Inkonsistente Marker)

    # --- BLOCK 4: Anführungszeichen-Korrekturen (Schweizer Typographie) ---
    # Vereinfachter Ansatz: Direkte kontextbasierte Ersetzung in mehreren Schritten

    # 1. Innere Anführungszeichen (falls benötigt - Vorerst auskommentiert, da Fokus auf «»)
    # opening_inner = r"[‹`']" # Beispiel: ‹ oder ` oder '
    # closing_inner = r"[›']"   # Beispiel: › oder '
    # corrected_text = re.sub(r'«([^»]*)' + opening_inner + r'([^»' + closing_inner + r']*)' + closing_inner, r'«\1‹\2›', corrected_text) # Beispiel für innere

    # 2. Äußere Anführungszeichen (Priorität auf spezifische Paare, dann Fallback)

    # 2.1 Spezifische Paare zuerst (Deutsch „...“)
    #     Suche nach „ gefolgt von nicht-“ Zeichen, bis zum nächsten “
    #     Verwendet non-greedy match `.*?`
    corrected_text = re.sub(r'„(.*?)“', r'«\1»', corrected_text)

    # 2.2 Fallback für öffnende Anführungszeichen (sollten « werden)
    #     Beinhaltet: Gerade Zollzeichen ("), verbleibendes deutsches öffnendes („), englisches öffnendes (“)
    #     Wird nur ersetzt, wenn am Anfang/nach Leerzeichen/Klammer etc.
    opening_quotes_to_convert = r'["„“]'
    corrected_text = re.sub(r'(^|\s|[\(\{\[])(' + opening_quotes_to_convert + ')', r'\1«', corrected_text)

    # 2.3 Fallback für schliessende Anführungszeichen (sollten » werden)
    #     Beinhaltet: Gerade Zollzeichen ("), verbleibendes deutsches schliessendes (“), englisches schliessendes (”)
    #     Wird nur ersetzt, wenn nach Nicht-Leerzeichen und vor Satzzeichen/Leerzeichen/Ende.
    closing_quotes_to_convert = r'["“”]' # Gerade Zollzeichen, deutsches/englisches schliessendes
    corrected_text = re.sub(r'(\S)(' + closing_quotes_to_convert + r')(?=[\s.,;!?]|$)', r'\1»', corrected_text)

    # 2.4 Konvertiere verschachtelte «...» zu ‹...›
    #     Sucht nach « gefolgt von nicht-» Zeichen, dann «...», dann nicht-« Zeichen, dann »
    #     Wiederholt anwenden, falls mehrere Verschachtelungsebenen (obwohl selten)
    #     Verwendet non-greedy match `.*?` für den inneren Inhalt
    #     Lookbehind (?<!«) und Lookahead (?![»]) um sicherzustellen, dass wir nicht Teil eines schon konvertierten ‹› sind.
    while re.search(r'«[^»]*«', corrected_text): # Solange verschachtelte « gefunden werden
         corrected_text = re.sub(r'(«[^»]*?)(?<!‹)«(.*?)»(?!›)([^«]*?») ', r'\1‹\2›\3', corrected_text)
         # Fallback, falls die obige komplexere Regex nicht greift (einfachere Version)
         if not re.search(r'«[^»]*«', corrected_text): # Prüfen ob noch verschachtelte « da sind
             break # Wenn nicht, Schleife beenden
         corrected_text = re.sub(r'(«.*?)«(.*?)»(.*?»)', r'\1‹\2›\3', corrected_text) # Einfachere Version ohne Lookarounds


    # --- BLOCK 3: Apostroph-Korrekturen ---
    #    Ersetzt verbleibende gerade Schreibmaschinen-Apostrophe durch typografische Apostrophe (' U+2019).
    # 3.1 Apostroph zwischen Buchstaben/Zahlen (z.B. geht's, '90s).
    corrected_text = re.sub(r"(\w)'(\w)", r"\1'\2", corrected_text)
    # 3.2 Apostroph am Wortanfang nach einem Leerzeichen (z.B. 'ne Idee -> 'ne Idee).
    corrected_text = re.sub(r"(\s)'(\w)", r"\1'\2", corrected_text)

    # --- BLOCK 5: Spezifische Leerzeichen-Anpassungen ---
    #    Passt Leerzeichen basierend auf den nun korrekten Zeichen an.

    # 5.1 Einzelnes Leerzeichen um Et-Zeichen (&), wenn es Wörter verbindet.
    # Stellt sicher, dass ein Leerzeichen vor und nach dem & steht, ohne Buchstaben zu entfernen
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

    # --- BLOCK 6: Ersetzt Bindestriche durch Gedanken-/Bis-Striche (– U+2013) in typischen Bereichen ---

    # 6.1 Zwischen Zahlen (z.B. 10-20 -> 10–20). Beachtet auch Punkte/Doppelpunkte für Daten/Zeiten.
    #       Wichtig: Fügt hier KEINE Leerzeichen hinzu, das behandelt Regel 5.2 später, falls nötig.
    corrected_text = re.sub(r'(\d)([.:]?\d*)\s*-\s*(\d)', r'\1\2–\3', corrected_text)
    # 6.2 Zwischen Wochentags-Abkürzungen (Mo-Fr -> Mo–Fr)
    days_pattern = r'\b(Mo|Di|Mi|Do|Fr|Sa|So)\b'
    corrected_text = re.sub(days_pattern + r'\s*-\s*' + days_pattern, r'\1–\2', corrected_text)
    # 6.3 Als Gedankenstrich: Ersetzt Bindestrich mit Leerzeichen davor und danach.
    corrected_text = re.sub(r'\s+-\s+', ' – ', corrected_text) # Mit Leerzeichen ersetzen

    # --- BLOCK 7: Korrekturen für Schrägstriche ---
    # 7.1 Entfernt Leerzeichen um Schrägstriche, wenn sie einzelne Wörter oder
    #       typische Abkürzungen/Gender-Notationen verbinden.
    #       Beispiele: "Sa / So" -> "Sa/So", "Techniker / Supporter" -> "Techniker/Supporter",
    #                  "Taxifahrer / -in" -> "Taxifahrer/-in", "w / m" -> "w/m"
    #       Das (\S) stellt sicher, dass keine Leerzeichen vor/nach dem Slash sind.
    #       (?<!\s) und (?!\s) sind negative Lookarounds, um sicherzustellen, dass KEIN Leerzeichen da ist.
    #       Wir suchen nach Mustern MIT Leerzeichen und ersetzen sie durch das Muster OHNE.
    #       Muster 1: Leerzeichen VOR dem Slash
    corrected_text = re.sub(r'(\S)\s+/', r'\1/', corrected_text)
    #       Muster 2: Leerzeichen NACH dem Slash
    corrected_text = re.sub(r'/\s+(\S)', r'/\1', corrected_text)
    #       Hinweis: Diese Regeln erhalten Leerzeichen bei Wortgruppen wie 'PHP Operator / C# Supporter',
    #       da der Slash dort nicht direkt von einem Nicht-Leerzeichen (\S) umgeben ist.

    # --- BLOCK 9: Schweizer Währungsformatierung (CHF) --- ÜBERARBEITET
    #    Ziel: Einheitliches Format "CHF Betrag.–" oder "CHF Betrag.xx"
    #    WICHTIG: Währungsformatierung VOR Tausendertrennern durchführen!

    # 9.0 Vorbereitung: Ersetze alle Währungsvarianten durch CHF
    # Speichere zuerst den Text, um später zu prüfen, ob es sich um einen Währungsbetrag handelt
    original_text = corrected_text

    # Prüfe, ob es sich um einen Währungsbetrag handelt
    is_currency = re.search(r'\b(CHF|Fr\.?|SFr\.?|Franken)\s+\d', original_text)

    corrected_text = re.sub(r'\b(Fr\.?|SFr\.?)\b', 'CHF', corrected_text)
    corrected_text = re.sub(r'\bFranken\b', 'CHF', corrected_text)

    # 9.1 Stelle sicher, dass CHF VOR dem Betrag steht
    #     Behandelt Fälle wie "100 CHF" -> "CHF 100"
    corrected_text = re.sub(r'\b(\d+(?:[.,]\d+)?)\s+(CHF)\b', r'\2 \1', corrected_text)

    # 9.2 Stelle sicher, dass ein Leerzeichen zwischen CHF und Betrag ist
    corrected_text = re.sub(r'\b(CHF)(\d)', r'\1 \2', corrected_text)

    # 9.3 Konvertiere Komma zu Punkt bei Dezimalzahlen nach CHF
    corrected_text = re.sub(r'\b(CHF)\s+(\d+),(\d{1,2})\b', r'\1 \2.\3', corrected_text)

    # 9.4 Normalisiere ".00" zu ".–" nach CHF
    corrected_text = re.sub(r'\b(CHF)\s+(\d+)\.00\b', r'\1 \2.–', corrected_text)

    # 9.5 Ersetze "--" generell durch einen Halbgeviertstrich "–"
    corrected_text = re.sub(r'--', '–', corrected_text)

    # 9.6 Normalisiere ".-" und ".--" zu ".–" nach einer Zahl (unabhängig von CHF)
    #     Behandelt Fälle wie "30.-" -> "30.–" und "30.--" -> "30.–"
    corrected_text = re.sub(r'(\d)\s*\.(?:--|-)\b', r'\1.–', corrected_text)

    # 9.7 Ersetze normale Bindestriche mit Punkten bei Währungsbeträgen durch Halbgeviertstriche
    corrected_text = re.sub(r'\b(CHF\s+\d+)\.-', r'\1.–', corrected_text)

    # 9.8 Ergänze ".–" bei ganzen CHF-Beträgen, die noch keine Endung haben
    #     (?![.,\d]) stellt sicher, dass keine Dezimalstellen folgen
    #     (?<!–) stellt sicher, dass nicht bereits ".–" vorhanden ist
    #     KORRIGIERT: Erlaubt alle Apostrophe (', ‘, ’) innerhalb der Zahl.
    corrected_text = re.sub(r'\b(CHF)\s+([\d\'‘’]+)(?![.,\d])(?<!–)\b', r'\1 \2.–', corrected_text)

    # 9.9 Spezialfall: Korrigiere falsch formatierte Währungsbeträge mit Apostrophen
    corrected_text = re.sub(r'\b(CHF)\s+(\d+)\.–\'(\d+)\.–', r"\1 \2'\3.–", corrected_text)

    # 9.10 Spezialfall: Ersetze Apostrophe in Währungsbeträgen durch typografische Apostrophe (’)
    # REAKTIVIERT und ERWEITERT: Behandelt ' und ‘ nur bei Währungen.
    if is_currency:
        # Ersetze gerade (') und linke (‘) Apostrophe durch typografische Apostrophe (’)
        corrected_text = corrected_text.replace("'", "’") # U+0027 -> U+2019
        corrected_text = corrected_text.replace("‘", "’") # U+2018 -> U+2019

    # --- BLOCK 8: Zahlenformatierung (Schweizer Stil - Fokus auf Tausendertrenner) ---
    #    Ziel: Konsistente Tausendertrennung mit Leerzeichen (MVP-Entscheidung).
    #    Hinweis: Kontextabhängiger Apostroph für Währung (z.B. CHF 10'000.-) wird NICHT implementiert.

    # 8.1 Entfernt Kommas, die als Tausendertrenner zwischen Ziffern verwendet werden,
    #     ABER NUR, wenn danach nicht genau 2 Ziffern folgen (um Dezimalkommas zu erhalten)
    #     Beispiel: 10,000 -> 10000, aber 12,50 bleibt 12,50
    corrected_text = re.sub(r'(\d),(?!\d{1,2}(?:\b|[,.;:!?]))', r'\1', corrected_text)

    # 8.2 Entfernt Apostrophe, die als Tausendertrenner zwischen Ziffern verwendet werden.
    #     Beispiel: 10'000 -> 10000, 10‘000 -> 10000 (Bereitet für korrekte Einfügung vor)
    #     Aber nur, wenn es sich nicht um einen Währungsbetrag handelt
    if not is_currency:
        # Entferne gerade (') und linke (‘) Apostrophe zwischen Ziffern
        corrected_text = re.sub(r'(\d)[\'‘](\d)', r'\1\2', corrected_text)

    # 8.3 Entfernt Leerzeichen, die WAHRSCHEINLICH als Tausendertrenner dienen.
    #     Sucht nach Leerzeichen zwischen Ziffern, denen genau 3 Ziffern folgen.
    #     Vorsichtiger als einfaches Entfernen aller Leerzeichen zwischen Zahlen.
    #     Beispiel: 10 000 -> 10000, aber "Call 123 456" bleibt eher unberührt.
    corrected_text = re.sub(r'(\d) +(?=\d{3})', r'\1', corrected_text) # Lookahead (?=...) prüft, ohne zu konsumieren

    # 8.4 Fügt einen typografischen Apostroph (’ U+2019) als Tausendertrenner ein (NEUER ANSATZ).
    try:
        # Funktion zum Einfügen des Apostroph-Trennzeichens
        def insert_apostrophe_separator(match):
            number_str = match.group(0)
            # Zahlen ab 1000 (4+ Ziffern) bearbeiten
            if len(number_str) >= 4:
                # Ersetze zuerst alle vorhandenen geraden (') und linken (‘) Apostrophe durch typografische Apostrophe (’)
                number_str = number_str.replace("'", "’") # U+0027 -> U+2019
                number_str = number_str.replace("‘", "’") # U+2018 -> U+2019
                # Fügt ’ vor jede Gruppe von 3 Ziffern ein, die von einer Ziffer gefolgt wird,
                # aber nicht am Anfang der Zahl steht.
                # Vermeidet Trennung bei Dezimalzahlen.
                return re.sub(r'(?<=\d)(?=(\d{3})+(?!\d*[,.])\b)', r'’', number_str)
            else:
                # Zahlen < 1000 bleiben unverändert
                return number_str

        # Finde alle Zahlen mit 4+ Ziffern und wende die Funktion darauf an.
        # \b stellt sicher, dass wir ganze Zahlen erwischen.
        corrected_text = re.sub(r'\b\d{4,}\b', insert_apostrophe_separator, corrected_text)

    except re.error as e:
        print(f"Regex Fehler bei Tausendertrenner-Einfügung (Block 8.4): {e}")
        # Bei Fehler den Originaltext (vor diesem Block) weiterverwenden
        # (corrected_text behält den Wert von vor dem try-Block)
        pass

    # --- BLOCK X: Sonstige Korrekturen ---

    # X.1 Ellipse (...) ersetzen durch typografische Ellipse (…) U+2026.
    corrected_text = re.sub(r'\.\s*\.\s*\.', '…', corrected_text)
    corrected_text = re.sub(r'\.\.\.', '…', corrected_text)

    # X.2 Einfache PDF-Zeilenumbrüche entfernen (Wort-Trennstrich-Umbruch)
    corrected_text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', corrected_text)

    # NEUE REGEL: X.3 Entfernt unerwünschte Trennstriche innerhalb von Wörtern
    # Behält Bindestriche vor Grossbuchstaben bei und in bestimmten englischen Begriffen.

    # Schritt 1: Markiere Ausnahmen, bei denen der Bindestrich erhalten bleiben soll
    # Liste der englischen Begriffe, bei denen der Bindestrich erhalten bleiben soll
    patterns_to_preserve = [
        r'\b[Ss]it-up(s)?\b',
        r'\b[Pp]ush-up(s)?\b',
        r'\b[Ww]arm-up(s)?\b',
        r'\b[Cc]ool-down(s)?\b',
        r'\b[Cc]heck-in(s)?\b',
        r'\b[Ll]og-in(s)?\b',
        r'\b[Ss]ign-in(s)?\b',
        r'\b[Oo]pt-in(s)?\b',
        r'\b[Oo]pt-out(s)?\b',
        r'\b[Ll]og-out(s)?\b',
        r'\b[Ss]ign-out(s)?\b',
        r'\b[Cc]heck-out(s)?\b',
        r'\b[Ss]tand-up(s)?\b',
        r'\b[Ss]et-up(s)?\b',
        r'\b[Ff]ollow-up(s)?\b',
        r'\b[Bb]ack-up(s)?\b',
        r'\b[Ss]tart-up(s)?\b'
    ]

    # Spezieller Platzhalter, der in normalen Texten unwahrscheinlich ist
    placeholder = "___HYPHEN_PRESERVE___"

    # Markiere alle zu erhaltenden Muster
    for pattern in patterns_to_preserve:
        corrected_text = re.sub(pattern, lambda m: m.group(0).replace('-', placeholder), corrected_text)

    # Schritt 2: Wende die allgemeine Regel an, um andere Bindestriche zu entfernen
    corrected_text = re.sub(r'(\w)-([a-zäöüß])', r'\1\2', corrected_text)

    # Schritt 3: Stelle die markierten Ausnahmen wieder her
    corrected_text = corrected_text.replace(placeholder, '-')

    # X.3 Ersetzt ß durch ss (Schweizer Rechtschreibung).
    corrected_text = corrected_text.replace('ß', 'ss')

    # X.4 Einfache PDF-Zeilenumbrüche entfernen (Wort-Trennstrich-Umbruch)
#     Fügt Wortteile zusammen, die durch einen Bindestrich (-) am Zeilenende (\n) getrennt wurden.
    corrected_text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', corrected_text)
#     Optional: Auch Umbrüche ohne Trennstrich entfernen, wenn es sinnvolle Sätze ergibt (komplexer!)

    # X.5 Gradzeichen (Buchstabe o -> ° U+00B0) nach Zahlen
    #       Beispiel: 90o -> 90°
    #       Ersetzt nur den Kleinbuchstaben 'o' direkt nach einer Ziffer, gefolgt von einer Wortgrenze (\b).
    corrected_text = re.sub(r'(\d)o\b', r'\1°', corrected_text)
    #       Optional: Auch den maskulinen Ordinalindikator 'º' (U+00BA) ersetzen, falls dieser falsch verwendet wird.
    #       corrected_text = re.sub(r'(\d)º', r'\1°', corrected_text)

    # X.6 Multiplikationszeichen (x oder mal -> × U+00D7) zwischen Zahlen
    #       Beispiel: 3x4 -> 3×4, 3 x 4 -> 3×4, 5mal6 -> 5×6, 5 mal 6 -> 5×6
    #       Ersetzt 'x', 'X' oder 'mal' (in beliebiger Schreibweise), optional von Leerzeichen umgeben, nur zwischen Ziffern.
    corrected_text = re.sub(r'(\d)\s*(?:[xX]|[mM][aA][lL])\s*(\d)', r'\1×\2', corrected_text)
    #       Optional: Mit (geschütztem) Leerzeichen für bessere Lesbarkeit ersetzen:
    #       corrected_text = re.sub(r'(\d)\s*(?:[xX]|[mM][aA][lL])\s*(\d)', r'\1\u00A0×\u00A0\2', corrected_text) # U+00A0 = non-breaking space

    # X.7 Geschützte Leerzeichen um & (nicht-brechende Leerzeichen, U+00A0)
    # Beispiel: "Mix & Match" -> "Mix\u00A0&\u00A0Match"

    # WICHTIG: Diese Regeln werden NACH Regel 5.1 angewendet, die bereits normale Leerzeichen
    # um das &-Zeichen einfügt. Diese Regeln ersetzen dann die normalen Leerzeichen durch
    # geschützte Leerzeichen (non-breaking spaces).

    # Schritt 1: Ersetze normale Leerzeichen vor und nach & durch geschützte Leerzeichen
    # Wichtig: Wir suchen nach einem Muster mit Leerzeichen und ersetzen nur die Leerzeichen
    # Verwenden eines normalen Strings (nicht raw string) für die Ersetzung mit Escape-Sequenz
    # Verwenden von \b\w+\b, um das gesamte Wort zu erfassen, nicht nur den letzten Buchstaben
    corrected_text = re.sub(r' &', '\u00A0&', corrected_text)
    corrected_text = re.sub(r'& ', '&\u00A0', corrected_text)

    # X.8 Ersetzt numerische Brüche durch Unicode-Bruchzeichen
    # Definiere ein Dictionary mit häufigen Brüchen und ihren Unicode-Äquivalenten
    fractions_map = {
        '1/2': '½',   # U+00BD
        '1/3': '⅓',   # U+2153
        '2/3': '⅔',   # U+2154
        '1/4': '¼',   # U+00BC
        '3/4': '¾',   # U+00BE
        '1/5': '⅕',   # U+2155
        '2/5': '⅖',   # U+2156
        '3/5': '⅗',   # U+2157
        '4/5': '⅘',   # U+2158
        '1/6': '⅙',   # U+2159
        '5/6': '⅚',   # U+215A
        '1/8': '⅛',   # U+215B
        '3/8': '⅜',   # U+215C
        '5/8': '⅝',   # U+215D
        '7/8': '⅞'    # U+215E

    }

    # X.9 Entfernt alle harten Umbrüche, wenn preserve_formatting nicht aktiviert ist
    if not preserve_formatting:
        corrected_text = re.sub(r'\n', ' ', corrected_text)


    # Ersetze die Brüche durch ihre Unicode-Äquivalente
    # Verwenden eines Wortgrenzenmusters (\b), um nur alleinstehende Brüche zu ersetzen
    for fraction, unicode_fraction in fractions_map.items():
        # Sucht nach Brüchen mit Leerzeichen davor oder danach oder am Anfang/Ende des Textes
        pattern = r'(\s|^)' + re.escape(fraction) + r'(\s|$)'
        corrected_text = re.sub(pattern, r'\1' + unicode_fraction + r'\2', corrected_text)

        # Sucht nach Brüchen gefolgt von Einheiten oder bestimmten Wörtern
        pattern = r'\b' + re.escape(fraction) + r'(?=\s*(?:[a-zA-ZäöüÄÖÜ]+|' + units_pattern + r'))'
        corrected_text = re.sub(pattern, unicode_fraction, corrected_text)

    # Erweiterte Regel für gemischte Zahlen mit Brüchen (z.B. "1 1/2" -> "1½")
    for fraction, unicode_fraction in fractions_map.items():
        pattern = r'(\d+)\s+' + re.escape(fraction) + r'\b'
        corrected_text = re.sub(pattern, r'\1' + unicode_fraction, corrected_text)



    # --- BLOCK Z: Finale Bereinigung ---
    # Z.1 Entfernt führende/nachfolgende Leerzeichen vom gesamten Text.
    corrected_text = corrected_text.strip()

    # Z.2 Entferne die temporären Marker für Jahreszahlen
    corrected_text = corrected_text.replace('__PROTECTED__', '') # KORRIGIERT

    # Rückgabe des vollständig korrigierten Textes
    return corrected_text

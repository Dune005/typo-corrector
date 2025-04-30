import re

def apply_ampersand_rules(text):
    """Apply only the ampersand rules to the text."""
    # 5.1 Einzelnes Leerzeichen um Et-Zeichen (&), wenn es Wörter verbindet.
    corrected_text = re.sub(r'(\w)\s*&\s*(\w)', r'\1 & \2', text)
    
    # X.7 Geschützte Leerzeichen um & (nicht-brechende Leerzeichen, U+00A0)
    # Schritt 1: Ersetze alle vorhandenen normalen Leerzeichen um & durch geschützte Leerzeichen
    corrected_text = re.sub(r'(\S)\s+&', '\1\u00A0&', corrected_text)
    corrected_text = re.sub(r'&\s+(\S)', '&\u00A0\1', corrected_text)
    
    # Schritt 2: Füge geschützte Leerzeichen ein, wo keine Leerzeichen sind, aber nur
    # wenn & zwischen Wort-/Zahlenzeichen steht
    corrected_text = re.sub(r'(\w)&', '\1\u00A0&', corrected_text)
    corrected_text = re.sub(r'&(\w)', '&\u00A0\1', corrected_text)
    
    return corrected_text

# Test cases for ampersand corrections
test_cases = [
    "Sparen & Anlegen",
    "Hinz&Kunz",
    "A & B",
    "A&B",
    "Test & Test",
    "Test&Test"
]

print("Testing ampersand corrections (rules 5.1 and X.7):")
print("-" * 40)

for test in test_cases:
    corrected = apply_ampersand_rules(test)
    print(f"Original: '{test}'")
    print(f"Corrected: '{corrected}'")
    print("-" * 40)

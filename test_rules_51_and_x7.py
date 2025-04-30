import re

def apply_rules_51_and_x7(text):
    """Apply only rules 5.1 and X.7 to the text."""
    # 5.1 Einzelnes Leerzeichen um Et-Zeichen (&), wenn es Wörter verbindet.
    corrected_text = re.sub(r'(\w)\s*&\s*(\w)', r'\1 & \2', text)
    
    # X.7 Geschützte Leerzeichen um & (nicht-brechende Leerzeichen, U+00A0)
    # Schritt 1: Ersetze normale Leerzeichen vor und nach & durch geschützte Leerzeichen
    corrected_text = re.sub(r'(\S) &', '\1\u00A0&', corrected_text)
    corrected_text = re.sub(r'& (\S)', '&\u00A0\1', corrected_text)
    
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

# Unicode code point for non-breaking space
NBSP = 160  # Unicode code point for \u00A0

for test in test_cases:
    corrected = apply_rules_51_and_x7(test)
    print(f"Original: '{test}'")
    print(f"Corrected: '{corrected}'")
    
    # Check for non-breaking spaces around &
    chars_around_amp = []
    for i, c in enumerate(corrected):
        if c == '&' and i > 0 and i < len(corrected) - 1:
            chars_around_amp.append((ord(corrected[i-1]), ord(corrected[i+1])))
    
    print(f"Characters around &: {chars_around_amp}")
    print(f"Has non-breaking spaces: {any(NBSP in pair for pair in chars_around_amp)}")
    print("-" * 40)

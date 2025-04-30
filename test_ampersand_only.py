import re

def apply_ampersand_rule(text):
    """Apply only the ampersand rule to the text."""
    # 5.1 Einzelnes Leerzeichen um Et-Zeichen (&), wenn es Wörter verbindet.
    return re.sub(r'(\w)\s*&\s*(\w)', r'\1 & \2', text)

# Test cases for ampersand corrections
test_cases = [
    "Sparen & Anlegen",
    "Hinz&Kunz",
    "A & B",
    "A&B",
    "Test & Test",
    "Test&Test"
]

print("Testing ampersand corrections (only rule 5.1):")
print("-" * 40)

for test in test_cases:
    corrected = apply_ampersand_rule(test)
    print(f"Original: '{test}'")
    print(f"Corrected: '{corrected}'")
    print("-" * 40)

from backend.corrections.casual_rules import apply_corrections

# Test cases for ampersand corrections
test_cases = [
    "Sparen & Anlegen",
    "Hinz&Kunz",
    "A & B",
    "A&B",
    "Test & Test",
    "Test&Test"
]

print("Testing ampersand corrections with fixed rules:")
print("-" * 40)

# Unicode code point for non-breaking space
NBSP = 160  # Unicode code point for \u00A0

for test in test_cases:
    corrected = apply_corrections(test)
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

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

print("Testing ampersand corrections:")
print("-" * 40)

for test in test_cases:
    corrected = apply_corrections(test)
    print(f"Original: '{test}'")
    print(f"Corrected: '{corrected}'")
    print("-" * 40)

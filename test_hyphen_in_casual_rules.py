from backend.corrections.casual_rules import apply_corrections

# Test cases for hyphen corrections
test_cases = [
    "Sit-ups",
    "sit-ups",
    "E-Mail",
    "Push-ups",
    "Log-in",
    "Check-in",
    "Warm-up",
    "Cool-down",
    "T-Shirt",
    "Kinder-garten",  # Should remove hyphen
    "Schreib-tisch",  # Should remove hyphen
    "Haus-tier",      # Should remove hyphen
    "Arbeits-platz",  # Should remove hyphen
    "Geburts-tag",    # Should remove hyphen
    "Der Warm-up Bereich",  # Test in context
    "Mache 20 Sit-ups und 10 Push-ups"  # Test multiple terms
]

print("Testing hyphen corrections in casual_rules.py:")
print("-" * 40)

for test in test_cases:
    corrected = apply_corrections(test)
    print(f"Original: '{test}'")
    print(f"Corrected: '{corrected}'")
    print("-" * 40)

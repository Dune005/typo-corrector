from backend.corrections.casual_rules import apply_corrections

# Test cases
test_cases = [
    "35'000 Personen",
    "35‘000 Personen", # NEU: Testfall mit U+2018
    "1'000 Einwohner",
    "10'000 Besucher",
    "100'000 Euro",
    "1'000'000 Dollar",
    "999 Franken",  # Should remain unchanged (less than 1000)
    "CHF 5'000.–",  # Currency amount
    "CHF 135’000", # NEU: Currency amount without .– but with apostrophe
]

print("Original vs. Corrected:")
print("-" * 50)

for test in test_cases:
    corrected = apply_corrections(test)
    print(f"Original: {test}")
    print(f"Corrected: {corrected}")
    print(f"Original apostrophe: {repr(test)}")
    print(f"Corrected apostrophe: {repr(corrected)}")

    # Print each character's Unicode code point
    print("Original characters:")
    for char in test:
        print(f"{char}: {ord(char)}")
    print("Corrected characters:")
    for char in corrected:
        print(f"{char}: {ord(char)}")

    print("-" * 50)

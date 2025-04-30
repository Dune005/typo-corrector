import re

def test_hyphen_rule(text):
    """Test different versions of the hyphen rule."""
    print(f"Original text: '{text}'")
    
    # Current rule: Removes hyphens before lowercase letters
    result1 = re.sub(r'(\w)-([a-zäöüß])', r'\1\2', text)
    print(f"Current rule: '{result1}'")
    
    # Improved rule 1: Keep hyphens in common English terms
    # This uses a negative lookahead to avoid matching certain patterns
    result2 = re.sub(r'(\w)-(?!(?:up|in|out|off|on|to|by|at|as)\b)([a-zäöüß])', r'\1\2', text)
    print(f"Improved rule 1: '{result2}'")
    
    # Improved rule 2: Keep hyphens in words that are likely to be compound terms
    # This is more conservative and only removes hyphens in specific cases
    result3 = re.sub(r'(\w{3,})-([a-zäöüß]{1,2}\w{0,1})', r'\1\2', text)
    print(f"Improved rule 2: '{result3}'")
    
    return result2  # Return the result of the first improved rule

# Test cases
test_cases = [
    "Sit-ups",
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
    "Geburts-tag"     # Should remove hyphen
]

print("Testing hyphen rules:")
print("-" * 40)

for test in test_cases:
    print("\nTest case:", test)
    result = test_hyphen_rule(test)
    print("-" * 20)

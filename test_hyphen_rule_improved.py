import re

def test_hyphen_rule(text):
    """Test different versions of the hyphen rule."""
    print(f"Original text: '{text}'")
    
    # Current rule: Removes hyphens before lowercase letters
    result1 = re.sub(r'(\w)-([a-zäöüß])', r'\1\2', text)
    print(f"Current rule: '{result1}'")
    
    # Improved rule: Keep hyphens in common English terms
    # Define a list of common English terms that should keep their hyphens
    exceptions = [
        r'sit-up', r'push-up', r'warm-up', r'cool-down', r'check-in', r'log-in', 
        r'sign-in', r'opt-in', r'opt-out', r'log-out', r'sign-out', r'check-out',
        r'stand-up', r'set-up', r'follow-up', r'back-up', r'start-up'
    ]
    
    # Create a pattern that matches any of these terms (case-insensitive)
    exception_pattern = '|'.join(exceptions)
    
    # Apply the rule with exceptions
    result2 = text
    # First, apply the rule to remove hyphens in normal German compound words
    result2 = re.sub(r'(\w)-([a-zäöüß])', r'\1\2', result2)
    # Then, restore the hyphens in the exception terms
    for exception in exceptions:
        # Create patterns to match the term without hyphen, case-insensitive
        without_hyphen = exception.replace('-', '')
        # Use word boundaries to ensure we match the whole word
        pattern = r'(?i)\b' + without_hyphen + r'\b'
        # Replace with the hyphenated version
        replacement = exception.replace('-', '-')  # This is just to make it clear we're adding the hyphen back
        result2 = re.sub(pattern, replacement, result2)
    
    print(f"Improved rule: '{result2}'")
    
    return result2

# Test cases
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
    "Geburts-tag"     # Should remove hyphen
]

print("Testing hyphen rules:")
print("-" * 40)

for test in test_cases:
    print("\nTest case:", test)
    result = test_hyphen_rule(test)
    print("-" * 20)

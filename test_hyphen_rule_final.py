import re

def test_hyphen_rule(text):
    """Test the final version of the hyphen rule."""
    print(f"Original text: '{text}'")
    
    # Current rule: Removes hyphens before lowercase letters
    result1 = re.sub(r'(\w)-([a-zäöüß])', r'\1\2', text)
    print(f"Current rule: '{result1}'")
    
    # Improved approach: Use a two-step process
    # 1. First, identify and mark the exceptions we want to preserve
    # 2. Then apply the general rule to remove other hyphens
    # 3. Finally, restore the marked exceptions
    
    # Step 1: Mark exceptions with a special placeholder
    result2 = text
    
    # Define patterns for common English terms with hyphens that should be preserved
    # Using word boundaries and case-insensitive matching
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
    
    # Special placeholder that's unlikely to appear in normal text
    placeholder = "___HYPHEN_PRESERVE___"
    
    # Mark all patterns to preserve
    for pattern in patterns_to_preserve:
        result2 = re.sub(pattern, lambda m: m.group(0).replace('-', placeholder), result2)
    
    # Step 2: Apply the general rule to remove other hyphens
    result2 = re.sub(r'(\w)-([a-zäöüß])', r'\1\2', result2)
    
    # Step 3: Restore the marked exceptions
    result2 = result2.replace(placeholder, '-')
    
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
    "Geburts-tag",    # Should remove hyphen
    "Der Warm-up Bereich",  # Test in context
    "Mache 20 Sit-ups und 10 Push-ups"  # Test multiple terms
]

print("Testing hyphen rules:")
print("-" * 40)

for test in test_cases:
    print("\nTest case:", test)
    result = test_hyphen_rule(test)
    print("-" * 20)

import re

def debug_x7_rules(text):
    """Debug the X.7 rules step by step."""
    print(f"Starting text: '{text}'")
    
    # 5.1 Einzelnes Leerzeichen um Et-Zeichen (&), wenn es Wörter verbindet.
    corrected_text = re.sub(r'(\w)\s*&\s*(\w)', r'\1 & \2', text)
    print(f"After rule 5.1: '{corrected_text}'")
    
    # Let's examine what's happening with the regex patterns in X.7
    # First, let's see what (\S) captures in "Sparen & Anlegen"
    match = re.search(r'(\S) &', corrected_text)
    if match:
        print(f"Match for '(\\S) &': {match.group(0)}, Captured: '{match.group(1)}'")
    
    # Now let's try a different pattern that captures the whole word
    match = re.search(r'(\S+) &', corrected_text)
    if match:
        print(f"Match for '(\\S+) &': {match.group(0)}, Captured: '{match.group(1)}'")
    
    # Let's try a pattern that specifically looks for word boundaries
    match = re.search(r'(\b\w+\b) &', corrected_text)
    if match:
        print(f"Match for '(\\b\\w+\\b) &': {match.group(0)}, Captured: '{match.group(1)}'")
    
    return corrected_text

# Test with a single example
test = "Sparen & Anlegen"
print(f"Testing with: '{test}'")
print("-" * 40)
result = debug_x7_rules(test)
print("-" * 40)

# Test with another example
test = "Hinz&Kunz"
print(f"Testing with: '{test}'")
print("-" * 40)
result = debug_x7_rules(test)
print("-" * 40)

import re

def apply_ampersand_rules_step_by_step(text):
    """Apply ampersand rules one by one to see which one causes the issue."""
    print(f"Starting text: '{text}'")
    
    # 5.1 Einzelnes Leerzeichen um Et-Zeichen (&), wenn es Wörter verbindet.
    corrected_text = re.sub(r'(\w)\s*&\s*(\w)', r'\1 & \2', text)
    print(f"After rule 5.1: '{corrected_text}'")
    
    # X.7 Geschützte Leerzeichen um & (nicht-brechende Leerzeichen, U+00A0)
    # Schritt 1: Ersetze alle vorhandenen normalen Leerzeichen um & durch geschützte Leerzeichen
    # Using a normal string (not a raw string) for the replacement part
    temp = re.sub(r'(\S)\s+&', '\1\u00A0&', corrected_text)
    print(f"After X.7 step 1a: '{temp}'")
    
    temp = re.sub(r'&\s+(\S)', '&\u00A0\1', temp)
    print(f"After X.7 step 1b: '{temp}'")
    
    # Schritt 2: Füge geschützte Leerzeichen ein, wo keine Leerzeichen sind, aber nur
    # wenn & zwischen Wort-/Zahlenzeichen steht
    temp = re.sub(r'(\w)&', '\1\u00A0&', temp)
    print(f"After X.7 step 2a: '{temp}'")
    
    temp = re.sub(r'&(\w)', '&\u00A0\1', temp)
    print(f"After X.7 step 2b: '{temp}'")
    
    return temp

# Test with a single example
test = "Hinz&Kunz"
print(f"Testing with: '{test}'")
print("-" * 40)
result = apply_ampersand_rules_step_by_step(test)
print("-" * 40)
print(f"Final result: '{result}'")

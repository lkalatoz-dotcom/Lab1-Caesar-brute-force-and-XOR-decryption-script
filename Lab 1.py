# caesar_bruteforce.py
ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."

def caesar_decrypt(ct, shift):
    result = ""
    for c in ct:
        if c.isupper():
            result += chr((ord(c) - 65 - shift) % 26 + 65)
        elif c.islower():
            result += chr((ord(c) - 97 - shift) % 26 + 97)
        else:
            result += c
    return result

# Brute-force all shifts and print them
print("Brute-force results (shift -> plaintext):\n")
for s in range(26):
    candidate = caesar_decrypt(ciphertext, s)
    print(f"Shift {s:2d}: {candidate}")

# Simple auto-detect: check for common English words
print("\nAuto-detect likely plaintext(s):")
common_words = [" the ", " and ", " of ", " is ", "quick", "over"]
for s in range(26):
    candidate = caesar_decrypt(ciphertext, s).lower()
    if any(word in candidate for word in common_words):
        print(f"Shift {s:2d} -> {candidate}")

def compress(s):
    if not s:
        return ""
    
    compressed = []  # Store compressed parts
    count = 1  # Initialize character count
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1  # Increase count if same char repeats
        else:
            compressed.append(s[i - 1] + str(count))  # Store previous char & count
            count = 1  # Reset counter
    
    # Add last character sequence
    compressed.append(s[-1] + str(count))
    
    return "".join(compressed)

def decompress(s):
    import re
    
    if not s:
        return ""
    
    decompressed = []
    matches = re.findall(r'([a-z])(\d+)', s)  # Find character-number pairs
    
    for char, num in matches:
        decompressed.append(char * int(num))  # Expand characters
    
    return "".join(decompressed)

# Example runs
print(compress("aaabb"))  # Output: "a3b2"
print(compress("abc"))   # Output: "a1b1c1"
print(compress(""))      # Output: ""

print(decompress("a3b2"))  # Output: "aaabb"
print(decompress("a1b1c1"))  # Output: "abc"
print(decompress(""))  # Output: ""

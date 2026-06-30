def substring_between_chars(text, char):
    first = text.find(char)
    last = text.rfind(char)
    if first == -1 or first == last:
        return ""
    return text[first + 1:last]

# Sample calls
print(substring_between_chars("abracadabra", "a"))  # Expected: "bracadabr"
print(substring_between_chars("hello world", "l"))  # Expected: "lo wor"
print(substring_between_chars("test", "x"))         # Expected: ""
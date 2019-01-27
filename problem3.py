

#Test cases:
s = "azcbobobegghakl"
s = "zyxwvutsrqponmlkjihgfedcba"
s = "abcbcd"
alphabetic_char = ""
longest_aplhabet_char = ""
char_len = len(s)

for char_index in range(char_len - 1 ):
    next_char_index = char_index + 1
    next_char_symbol = s[next_char_index]
    char_symbol = s[char_index]
    if char_symbol <= next_char_symbol:
        if alphabetic_char != "":
            alphabetic_char += next_char_symbol
            if next_char_index + 1 == char_len and len(alphabetic_char) > len(longest_aplhabet_char):
                longest_aplhabet_char = alphabetic_char
        else:
            alphabetic_char += char_symbol + next_char_symbol
    else:
        if longest_aplhabet_char != "":
            if len(alphabetic_char) > len(longest_aplhabet_char):
                longest_aplhabet_char = alphabetic_char
        else:   
            longest_aplhabet_char = alphabetic_char
            if next_char_index + 1 == char_len:
                longest_aplhabet_char = s[0]
        alphabetic_char = ""


print("Longest substring in alphabetical order is " + longest_aplhabet_char)

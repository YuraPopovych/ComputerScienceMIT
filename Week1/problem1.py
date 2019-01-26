


s = 'azcbobobegghakl'
valid_vowels = ['a', 'e', 'i', 'o', 'u']

valid_vowel_count = 0
for char in s:
    if char in valid_vowels:
        valid_vowel_count += 1
print("Number of vowels:", valid_vowel_count)



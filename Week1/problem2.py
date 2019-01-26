

s = 'azcbobobegghakl'
bob_count = 0
for symbol_index in range( len(s) ):
    symbol = s[symbol_index]
    if symbol_index > 1 and symbol == 'b':
        if s[symbol_index - 2] == 'b' and s[symbol_index - 1] == 'o':
            bob_count += 1

print("Number of times bob occurs is:", bob_count)

        
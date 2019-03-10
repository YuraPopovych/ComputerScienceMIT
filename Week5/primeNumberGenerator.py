def genPrimes():
    p = 2
    primeNumbers = []
    while True:
        if p == 2:
            yield p
            primeNumbers.append(p)
        elif p % 2 != 0:
            dividedByPreviousNumber = False
            for i in primeNumbers:
                if p % i == 0:
                    dividedByPreviousNumber = True
            if not dividedByPreviousNumber:
                yield p
                primeNumbers.append(p)
        p += 1
            
test_range = 171
a = genPrimes()
for i in range(test_range):
    print(a.__next__())
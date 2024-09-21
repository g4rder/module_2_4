numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 25, 30, 55, 56, 57]
primes, not_primes, is_prime = [], [], True
for i in numbers:
    if i == 1:
        continue
    for j in (2, i - 1):
        if i == 2 or i % j != 0:
            is_prime = True
            continue
        else:
            not_primes.append(i)
            break
        not_primes.append(i)
    else:
        primes.append(i)
for i in primes[::]:
    if i != 3 and i != 5 and (i % 3 == 0 or i % 5 == 0):
        primes.remove(i)
        not_primes.append(i)
        continue
    else:
        continue
print(sorted(primes), sorted(not_primes), sep = '\n')

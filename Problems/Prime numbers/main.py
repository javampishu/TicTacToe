prime_numbers = []

for n in range (2, 1000):
    if not any(n % d == 0 for d in range(2, n)):
        prime_numbers.append(n)


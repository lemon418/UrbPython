numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = numbers
not_primes = []

for i in range(len(numbers)):
    # is_prime = True
    num = numbers[i]
    if num == 1:
        continue

    for j in range(2, num):
        if num % j == 0:
            # is_prime = False
            not_primes.append(num)
            break

for i in range(len(numbers) + 1 ):
    for j in not_primes:
        if i == j:
            primes.remove(i)
primes.remove(1)

print('Primes: ', primes)
print('Not Primes: ', not_primes)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
print('numbers: ', numbers)
for i in range(1,15):
    is_prime = True
    for j in range(2, numbers[i]//2+1):
        if numbers[i]%j == 0:
            is_prime = False
            not_primes.append(numbers[i])
            break
    if is_prime:
        primes.append(numbers[i])
print('primes: ', primes)
print('not_primes: ', not_primes)












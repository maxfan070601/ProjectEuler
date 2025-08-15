import math


def largest_prime_factor():
    num = 600851475143
    factors = []
    while num > 1:
        for i in range(2, int(math.sqrt(600851475143)) + 1):
            if num % i == 0:
                factors.append(i)
                num /= i
    return max(factors)

print(largest_prime_factor())
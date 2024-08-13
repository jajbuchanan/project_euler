import math


def prime_factorisation(n):
    i = 2
    factors = {}
    while i <= math.isqrt(n):
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count:
            factors[i] = count
        i += 1 if i == 2 else 2  # After 2, check only odd numbers
    if n > 1:
        factors[n] = 1
    return factors


def count_divisors(n):
    factors = prime_factorisation(n)
    count = 1
    for exponent in factors.values():
        count *= exponent + 1
    return count


def find_triangle_number(min_divisors):
    n = 1
    max_divisors = 0
    while True:
        triangle = n * (n + 1) // 2

        # Depending on whether n is even or odd, factorise n//2 and n+1 or n and (n+1)//2
        if n % 2 == 0:
            factors_n = prime_factorisation(n // 2)
            factors_n1 = prime_factorisation(n + 1)
        else:
            factors_n = prime_factorisation(n)
            factors_n1 = prime_factorisation((n + 1) // 2)

        # Combine the exponents
        total_factors = {}
        for key in set(factors_n.keys() | factors_n1.keys()):
            total = factors_n.get(key, 0) + factors_n1.get(key, 0)
            total_factors[key] = total

        # Calculate the number of divisors
        divisors = 1
        for exponent in total_factors.values():
            divisors *= exponent + 1

        if divisors > max_divisors:
            max_divisors = divisors
            print(f"Triangle Number: {triangle}, Divisors: {divisors}")

        if divisors > min_divisors:
            return triangle

        n += 1


def main():
    min_divisors = 500
    result = find_triangle_number(min_divisors)
    print(f"The first triangle number with over {min_divisors} divisors is {result}")


if __name__ == "__main__":
    main()

def get_prime_numbers(n):
    import math

    n_squareroot = int(math.sqrt(n))

    not_prime_numbers = set()

    for increment_check in range(2, n_squareroot+1):
        for number in range(increment_check+1, n+1):
            if number%increment_check == 0:
                not_prime_numbers.add(number)
                continue

    prime_numbers = list()
    for number in range(2, n+1):
        if number not in not_prime_numbers:
            prime_numbers.append(number)

    return prime_numbers


if __name__ == "__main__":

    print("PRIME NUMBERS - SIEVE OF ERATOSTHENES")

    while True:
        try:
            max_number = int(input("Please provide a limit to look for prime numbers: \n"))
            if max_number <= 2:
                print("Number must be greater than 2 - in other case there are no prime numbers")
            else:
                break
        except ValueError:
            print("Please provide a numeric value")

    prime_numbers = get_prime_numbers(max_number)
    print(f"There are {len(prime_numbers)} prime numbers less or equal to {max_number}.\nThey are:")
    [print(i) for i in prime_numbers]

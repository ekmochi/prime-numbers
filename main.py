def get_prime_numbers(n):
    # todo
    pass


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

    get_prime_numbers(max_number)

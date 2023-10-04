"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    currentNum = 2

    if number_of_primes >= 1:
        while len(list) != number_of_primes:
            isPrime = True
            for i in range(2, currentNum):
                if (currentNum % i == 0) and (currentNum != 2):
                    isPrime = False
                    break
            if isPrime:
                list.append(currentNum)
            currentNum += 1
    elif number_of_primes < 1:
        raise ValueError
    return list
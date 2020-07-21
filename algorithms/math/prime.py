def prime(limit):
    """
    Prints the first limit primes.
    """
    count = 1
    while count < limit:

        flag = 0
        for i in range(3, count, 2):
            if count % i == 0:
                flag = 1

        if flag == 0:
            print(count)
            
        count += 2


# TESTING
if __name__ == "__main__":
    LIMIT = 100
    print("The primes below", str(LIMIT), "are:")
    prime(LIMIT)

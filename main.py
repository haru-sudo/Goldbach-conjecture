def sieve_of_eratosthenes(target_sum):
    sieve = [True] * (target_sum + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(target_sum**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, target_sum + 1, i):
                sieve[j] = False

    return [x for x in range(2, target_sum + 1) if sieve[x]]

def goldbach_conjecture(filename, target_sum):
    with open(filename, "w") as fileObj:
        pass

    primes = sieve_of_eratosthenes(target_sum)

    with open(filename, "a") as fileObj:
        for even_num in range(4, target_sum + 1, 2):
            for p in primes:
                q = even_num - p
                if q >= p and q in primes:
                    fileObj.write(f"{even_num} = {p} + {q}\n")
                    break

filename = "Goldbach-conjecture.txt"
target_sum = int(input("Total to be sought>>"))
goldbach_conjecture(filename, target_sum)
print("Successful output to Goldbach-conjecture.txt")

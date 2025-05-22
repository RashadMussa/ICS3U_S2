import math

def factorize(N):
    # Return a list of proper factors of N (excluding N itself)
    if N <= 1:
        return []  # 1 and below have no proper factors except empty set
    
    factors = [1]  # 1 is always a proper factor for N > 1
    limit = int(math.sqrt(N))
    
    for j in range(2, limit + 1):
        if N % j == 0:
            factors.append(j)
            other_factor = N // j
            if other_factor != j:  # Avoid adding the square root twice if perfect square
                factors.append(other_factor)
    
    return sorted(factors)

def sum_factors(factors):
    # Return the sum of integers in the list
    return sum(factors)

def classify_number(N):
    factors = factorize(N)
    total = sum_factors(factors)
    
    print("Factor sum: %d" % total)
    if total == N:
        print("%d is perfect" % N)
    elif total > N:
        print("%d is abundant" % N)
    else:
        print("%d is deficient" % N)

def main():
    while True:
        N = int(input("Please input a number: "))
        if N == 0:
            print("Goodbye!")
            break
        classify_number(N)

if __name__ == "__main__":
    main()

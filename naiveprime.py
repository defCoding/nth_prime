import time, math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 3:
        return False
    
    factor = 5
    skip = 2

    while factor <= math.ceil(math.sqrt(n)):
        if n % factor == 0:
            return False
        
        factor += skip
        skip = 6 - skip
    
    return True

def get_prime(n):
    count = 2

    candidate = 5
    while count < n:
        if is_prime(candidate):
            count += 1
            if count == n:
                break
        
        if (candidate % 6 == 5):
            candidate += 2
        elif (candidate % 6 == 1):
            candidate += 4
    
    print("The %dth prime number is %d"%(n, candidate))

def run():
    n = int(input())
    start_time = time.time()
    get_prime(n)
    print("--- %s seconds ---"%(time.time() - start_time))

if __name__ == "__main__":
    run()
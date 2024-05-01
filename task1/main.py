
def caching_fibonacci():
    cache = {} # cache initialization

    def fibonacci(n):
        if n <= 1:
            return n
    
        if n in cache:
            return cache[n]
        
        # recursive call for 2 previous numbers and save sum in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

def main():
    fibonacci = caching_fibonacci();
    print(fibonacci(10))
    print(fibonacci(15))

if __name__ == "__main__":
    main()
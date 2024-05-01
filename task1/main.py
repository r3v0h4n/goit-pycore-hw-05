
def caching_fibonacci():
    cache = {}  # Створюємо пустий кеш

    def fibonacci(n):
        if n <= 1:
            return n
    
        if n in cache:
            return cache[n]
        
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci

def main():
    fibonacci = caching_fibonacci();
    print(fibonacci(10))
    print(fibonacci(15))

if __name__ == "__main__":
    main()
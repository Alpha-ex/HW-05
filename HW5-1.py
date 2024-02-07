n=10

def caching_fibonacci():
    cache = {}  # Кеш для зберігання обчислених значень

    def fibonacci(n):
        if n <= 1:
            return n
        elif n in cache:
            return cache[n]
        else:
            # Обчислюємо число Фібоначчі за допомогою рекурсії
            result =( fibonacci(n - 1) + fibonacci(n - 2))
            # Зберігаємо результат у кеші
            cache[n] = result
            return result
    return fibonacci
cached_fibonacci = caching_fibonacci()
result = cached_fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
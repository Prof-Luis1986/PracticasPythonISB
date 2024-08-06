def fib(n):
    return fib(n-1) + [fib(n-2)[-1] + fib(n-2)[-2]] if n > 2 else [0] * (n == 1) + [0, 1][:n]

print(fib(10))

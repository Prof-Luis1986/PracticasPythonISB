fib = lambda n, a=0, b=1: [a] + fib(n-1, b, a+b) if n > 1 else [a]
print(fib(10))

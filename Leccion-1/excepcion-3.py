def factorial(n):
    assert(n >= 0)
    fct = 1
    for i in range(1, n+1):
        fct *= i
    
    print(f"{n}! = {fct}")

factorial(5)
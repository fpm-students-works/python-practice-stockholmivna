def fact(n):
    if n < 0:
        return "Factorial isn't defined for negative numbers"
    elif n == 0:
        return 1
    else:
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return factorial

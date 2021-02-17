def g(a, b):
    return a - b

def f(a, b, c, d):
    t0 = a + b - g(a, 0)
    t1 = g(c, d)
    try:
        t3 = 2 * (t0 / t1) #The error is given when t1 = 0, which happens when c = d.
        return t0 + 2 * t1 + t3 * t3
    except ZeroDivisionError:
        print("You cannot divide by zero (c and d cannot be equal).")



# -- Main program
print("Result 1: ", f(5, 2, 5, 0))
print("Result 2: ", f(0, 2, 3, 3))
print("Result 3: ", f(1, 3, 2, 3))
print("Result 4: ", f(1, 9, 22.0, 3))
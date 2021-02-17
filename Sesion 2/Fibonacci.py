def fibonacci(n):
    a = 0
    b = 1
    series = [a,b]
    for i in range(1, n-1):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series, c
exit = False
while not exit:
    try:
        n = int(input("Introduce a natural number: "))
        if n > 0:
            print("The " + str(n) + " number of the Fibonacci series for is: " + str(fibonacci(n)[1]) + " ,and the Fibonacci series for that number is: ", fibonacci(n)[0])
            exit = True
        else:
            print("The number you have introduced is not valid. Please introduce a natural number")
    except ValueError:
        print("The number you have introduced is not valid. Please introduce a natural number")
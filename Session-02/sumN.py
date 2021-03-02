def SUM(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
exit = False
while not exit:
    try:
        n = int(input("Introduce a natural number: "))
        if n > 0:
            print("The sum of the " + str(n) + " first natural numbers is: " + str(SUM(n)))
            exit = True
        else:
            print("The number you have introduced is not valid. Please introduce a natural number")
    except ValueError:
        print("The number you have introduced is not valid. Please introduce a natural number")
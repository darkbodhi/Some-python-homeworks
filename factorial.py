x = int(input("Please insert the number that will be factorized: "))
if x > 0:
    def factorial(x):
        if x == 1:
            return 1
        else:
            return x*factorial(x-1)
    print(factorial(x))
else:
    print(-1)
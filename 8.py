# Factorial

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

if __name__ == '__main__':
    n = input("Enter your number:\t")
    print "ans:\t{}!={}".format(n, factorial(n))

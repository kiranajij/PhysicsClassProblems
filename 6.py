def fib(n):
    a = 0; b = 1
    for i in range(n):
        a, b = b, a+b
    return b

if __name__ == '__main__':
    i = int(raw_input("Please enter your number:\t"))
    print "The {}-th term of fibonacci sequence is {}".format(i, fib(i))
    print "And the ratio is given by"
    for j in range(i):
        print "\t{}".format(fib(j+1)/float(fib(j)))

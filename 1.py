def fehrenheit_to_celcius(f):
    f = float(f)
    c = 5 * (f - 32)/ 9.0
    return c

def main():
    inp = raw_input("Enter temp:\t")
    temp = float(inp)
    c = fehrenheit_to_celcius(temp)
    print("the temp is {} degree celcius".format(c))

if __name__ == '__main__':
    main()

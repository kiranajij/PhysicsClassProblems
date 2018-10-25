def vel(v_0, a, t):
    return v_0 + a * t

def dist(v_0, a, t):
    return v_0 * t + 0.5 * a * (t ** 2)

def main():
    v_0 = float(input("enter v_0:\t"))
    t = float(input("enter t:\t"))
    a = float(input("enter a:\t"))
    v = vel(v_0, a, t)
    s = dist(v_0, a, t)
    print "v = {}\ns = {}".format(v, s)

if __name__ == '__main__':
    main()

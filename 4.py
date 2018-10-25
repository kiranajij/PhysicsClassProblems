def make_conversation():
    print "computer: What is your name?"
    name = raw_input()
    print "computer: Hi {}, how are you today.".format(name)

if __name__ == '__main__':
    make_conversation()

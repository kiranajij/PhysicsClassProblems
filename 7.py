# Number picking game

import random
def start_game(a, b):
    n = random.randint(a, b)
    attempts = 6
    print "attempts left:\t {}".format(attempts)
    for i in range(6):
        guess = input("\tplease enter your guess:\t")
        if (guess == n):
            print "Congrats You Won"
            return
        elif (guess < n):
            print "\tA bit higher"
            print "attempts left:\t {}".format(attempts-i-1)
        elif (guess > n):
            print "\tA bit lower"
            print "attempts left:\t {}".format(attempts-i-1)

if __name__ == '__main__':
    start_game(1, 10)

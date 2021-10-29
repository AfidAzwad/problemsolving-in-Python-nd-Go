import math


def countinTurn(n, p):

    if n%2 != 0 and n-p == 1: # to avoid extra calculation and value flooring problem [input n=9, p=8]

        return 0

    elif n%2 == 0 and n-p == 1 and n != 2: # to avoid flooring problem and 2 pages book => input n=2, p=1

        return 1
    
    elif (n-p) == n/p or (n-p) > n/2:

        return math.floor(p/2)

    else:
        return math.floor(n/2-p/2)


if __name__ == '__main__':

    n = int(input("n = ").rstrip())
    p = int(input("p = ").rstrip())

    print(countinTurn(n, p))

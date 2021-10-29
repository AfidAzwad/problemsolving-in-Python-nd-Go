import math


def countinTurn(n, p):

    if (n-p) == n/p or (n-p) > n/2:

        return math.floor(p/2)

    else:
        return math.floor(n/2-p/2)


if __name__ == '__main__':

    n = int(input("n = ").rstrip())
    p = int(input("p = ").rstrip())

    print(countinTurn(n, p))

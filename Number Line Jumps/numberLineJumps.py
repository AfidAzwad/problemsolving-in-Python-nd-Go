# equation => x1 + v1*y = x2 + v2*y
#          -> x1+v1*y == x2+v2*y
#          -> x1-x2 == v2*y-v1*y
#          -> x1-x2 == (v2-v1)*y
#          -> y = (x1 - x2) / (v2 - v1)

def kangaroo(x1, v1, x2, v2):

    if x2>x1 and v2>v1: #  second kangaroo is already ahead of the first kangaroo
        return "No"
    # from Equation, y = (x1 - x2) / (v2 - v1) and if they start together in same move (x1+v1 == x2+v2) = ((x1 - x2) % (v2 - v1) == 0) also
    else:
        if (v1 > v2) and (x1 - x2) % (v2 - v1) == 0:
            return "YES"
        else:
            return "NO"

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
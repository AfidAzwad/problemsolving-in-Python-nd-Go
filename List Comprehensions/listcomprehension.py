if __name__ == '__main__':
    x = int(input("x = "))
    y = int(input("y = "))
    z = int(input("z = "))
    n = int(input("n = ")) # sum of x,y,z can't be equal to n

    permutations  = [(a,b,c) for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c != n ]

    print(permutations)



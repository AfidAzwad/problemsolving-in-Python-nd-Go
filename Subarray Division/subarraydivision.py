def subarraydivision(k,d,ar):
    count = 0

    # Consecutive pairs means (a,b) => (b,c) => (c,d) if k = 2
    for i in range(len(ar)-k+1):

        print(ar[i:i+k], "Sum:",sum(ar[i:i+k]))

        if (sum(ar[i:i+k]) == d):
         count += 1
    
    return "\n" + str(count) + " square of chocolate in the bar satisfies this constraint "


if __name__ == '__main__':

    k = int(input("consecutive squares : ").strip())

    ar = list(map(int, input("chocolates : ").rstrip().split()))

    d = int(input("Sum should be : ").strip())

    result = subarraydivision(k, d, ar)

    print(result)

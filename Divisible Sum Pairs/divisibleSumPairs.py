def divisibleSumPairs( k, ar):
    # Write your code here

    count = 0

    pairs = [(ar[i],ar[j]) for i in range(len(ar)) for j in range(i+1, len(ar))] # pairs of the list where (a,b) != (b,a)

    print("\n Pairs : ",pairs)

    sums = [(ar[i]+ar[j]) for i in range(len(ar)) for j in range(i+1, len(ar))] # sum of the pairs

    for s in sums:
        if s%k == 0: #checking divisibility by k
            count += 1
    
    return "\n Total divisible sum of the pairs by " + str(k) + " = " + str(count) + " pairs"



if __name__ == '__main__':

    k = int(input("divisible value : ").strip())

    ar = list(map(int, input("values : ").rstrip().split()))

    result = divisibleSumPairs(k, ar)

    print(result)

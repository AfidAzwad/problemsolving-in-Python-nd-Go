def minimumAbsoluteDifference(arr):
    # Write your code here
    diff = []
    L = len(arr)
    
    arr.sort()
    
    if len(arr) != len(list(set(arr))):
        return 0
    else:
     for i in range(L-1):
        result = arr[i+1] - arr[i]
        diff.append(abs(result))
        if result == 0:  # to avoid unnecessary computations
            return min(diff)
     return diff, min(diff)


if __name__ == '__main__':
    n = int(input("n = ").strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)

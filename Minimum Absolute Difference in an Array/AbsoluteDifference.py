def minimumAbsoluteDifference(arr):
    # Write your code here
    diff = []
    z = 1
    L = len(arr)

    if len(arr) != len(list(set(arr))):  # checking duplicates to avoid unnecessary computations
        return 0
    else:
        for i in arr:
            for j in range(z, L):
                result = i - arr[j]
                diff.append(abs(result))
                if result == 0:  # to avoid unnecessary computations
                    return min(diff)
            z += 1
        return min(diff)


if __name__ == '__main__':
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    a = [5, 6, 7, 99, 77, 23, 33, 11]
    result = minimumAbsoluteDifference(a)

    print(result)

import numpy as np


def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(arr)):
        sum1 = sum1 + arr[i][i]
    print("Sum 1:",sum1)

    for j in range(0, len(arr)):
        sum2 = sum2 + arr[j][len(arr)-1-j]
    print("Sum 2:",sum2)

    diff = abs(abs(sum1) - abs(sum2))

    return diff


if __name__ == '__main__':
    n = int(input("Dimension value, n = ").strip()) #strip() method Remove spaces at the beginning and at the end of the string
    arr = []

    # 2D array input. example: 4 5 [enter] 6 7 =>> 2x2 array
    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print("\n", np.reshape(arr, (n, n)))

    result = diagonalDifference(arr)
    print("Diagonal Difference : ", result)

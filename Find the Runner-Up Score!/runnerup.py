if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sorted = set(arr)

    sorted.remove(max(sorted))

    print("Runner Up value :", max(sorted))


def circularArrayRotation(a, k, queries):
    for i in range(k):
        a.insert(0, a.pop())
    return ([a[i] for i in queries])
        

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)


    print(circularArrayRotation(a, k, queries))


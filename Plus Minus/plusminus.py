def plusMinus(arr):
    # Write your code here
    l = len(arr)
    plus= 0
    minus =0
    zero = 0

    for i in arr:
        if i > 0:
            plus+=1
        elif i < 0:
            minus+=1
        else:
            zero +=1
    
    plusratio = "{:.6f}".format(plus/l)
    minusratio = "{:.6f}".format(minus/l)
    zeroratio = "{:.6f}".format(zero/l)

    return plusratio,minusratio,zeroratio

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    # arr = [-1,7,0,0,-1,1]


    result = plusMinus(arr)
    print(result)

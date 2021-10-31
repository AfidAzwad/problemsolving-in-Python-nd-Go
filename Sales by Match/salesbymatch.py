import collections
import math

def sbymatch(arr):

    result = collections.Counter(arr)
    pair = 0

    print("\n",result)

    for i in result:
        pair += math.floor(result[i]/2)

    return "pairs : " + str(int(pair))
        

if __name__ == '__main__':
    
    ar = [10, 10, 10, 10, 20, 20, 20, 10, 10, 30, 40, 40, 50]

    print("\n",sbymatch(ar))
    
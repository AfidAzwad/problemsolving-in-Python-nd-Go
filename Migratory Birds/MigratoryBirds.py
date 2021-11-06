# if more than 1 type has maximum frequency then we will print the lower type
# for this we will use list sorting

from collections import Counter

def migratoryBirds(arr):
    lists = sorted(arr) # sorting to find the minimum most frequently sighted type
    
    result = Counter(lists) # to find frequently sighted type values
    
    print("\n",result)
   
    return " The type " + str(max(result, key= result.get)) + " has maximum frequency of " +  str(max(result.values()))

if __name__ == '__main__':

    arr_count = int(input("n = ").strip())

    arr = list(map(int, input("Bird types : ").rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
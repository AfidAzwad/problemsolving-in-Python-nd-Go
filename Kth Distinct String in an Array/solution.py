from collections import Counter

def kthDistinct(arr,k):
    hashMap = Counter(arr)
    distinct_values = [key for key,value in hashMap.items() if value == 1]
    return distinct_values[k-1] if len(distinct_values) >= k else ""  # For distinct_values space is O(d). So space is O(n) + O(d) = O(n)

arr = ["d","b","c","b","c","a"]
k=2
print(kthDistinct(arr,k))

# Time and Space both O(n)
import heapq

def findKthLargest(nums, k):
    max_heap = [-num for num in nums]  # as heapq by default make min-heap so if we need max heap to get largest value in root
    heapq.heapify(max_heap)  # Transform list into a heap in O(n)
    for _ in range(k):
        kth_largest = -heapq.heappop(max_heap)
    return kth_largest

nums = [3, 2, 1, 5, 5, 6, 4]
k = 3
print(findKthLargest(nums,k))

# Time Complexity:
# Building the heap: O(n).
# The heap size decreases with each extraction, so technically:
# - The time taken is O(log n) for the first pop,
# - O(log (n-1)) for the second pop,
# - O(log (n-2)) for the third pop, and so on.
# However, these operations still sum up to O(k log n),
# so the overall time complexity remains O(n + k log n).

# Space Complexity: O(n)

# Extra NOTE:
# The first pop operation takes O(logn) because:
# - The element removed is the root, which takes constant time.
# - The heap property is restored using the heapify-down process.
# - The heapify-down process requires O(logn) steps due to the height of the binary heap being ⌊log2(n)⌋.


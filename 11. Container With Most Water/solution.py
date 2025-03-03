def maxArea(height):
    max_area = 0
    L, R = 0, len(height)-1

    while L < R:
        max_area = max(max_area, (R - L) * min(height[L], height[R]))
        if height[L] < height[R]:
            L += 1
        else:
            R -= 1
    return max_area

height = [1,2,1]
print(maxArea(height))

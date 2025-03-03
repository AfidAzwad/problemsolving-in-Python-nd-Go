def maxArea(height):
    trap = 0
    L, R = 0, len(height)-1

    while L < R:
        trap = max(trap, (R - L) * min(height[L], height[R]))
        if height[L] > height[R]:
            R -= 1
        elif height[L] < height[R]:
            L += 1
        else:
            R -= 1
    return trap

height = [1,2,1]
print(maxArea(height))

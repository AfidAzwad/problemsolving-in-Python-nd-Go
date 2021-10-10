def count_rotations_linear(nums):

    position = int(len(nums)-1)
    count = 0

    while position > 0:
        if nums[position] < nums[position-1]:
            count += 1
        position -= 1

    return count


def rotate_list(nums):

    rotation = int(len(nums)-1)
    nums = nums[-rotation:] + nums[:-rotation] # Right rotation
    
    print("Rotations : ", rotation)
    return nums


if __name__ == '__main__':

    # array = [10, 9, 8, 4, 2, 1]

    n = int(input("Define List length, n= ").strip()) #strip() method Remove spaces at the beginning and at the end of the string
    
    arr = []

    for i in range(n):
        arr.append(input().strip()) # 1st input [enter] 2nd input

    print(arr)
    result = rotate_list(arr)
    print(result)

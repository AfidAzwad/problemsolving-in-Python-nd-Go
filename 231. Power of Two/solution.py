def isPowerOfTwo(n):
    # i = 0
    # while True:
    #     if 2 ** i == n:
    #         return True
    #     elif 2 ** i > n:
    #         return False
    #     i += 1

    '''Binary approach - wihtout loops '''
    return n > 0 and (n & (n-1)) == 0

n = 4
print(isPowerOfTwo(n))

# A power of two in binary has exactly one 1 bit and the rest are 0s. For example:
# 1 (binary: 0001)
# 2 (binary: 0010)
# 4 (binary: 0100)
# 8 (binary: 1000)

# 4 (binary: 0100) and 3 (binary: 0011) ==> 0
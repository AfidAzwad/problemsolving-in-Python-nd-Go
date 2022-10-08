#!/bin/python3

import math
import os
import random
import re
import sys


def saveThePrisoner(n, m, s):
    # Write your code here
    L = n+2
    print('n', n)
    print('L', L)
    
while s<=n:
        # print('i', i)
        m -= 1
        print('candy count', m)
        if m==0:
            return s
        elif s == n:
            s=1
            continue
            print('s',s)
            print('i',i)
        s+=1
        

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        print(str(result) + '\n')

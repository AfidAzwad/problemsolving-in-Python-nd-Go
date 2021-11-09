# for this problem => tricky but think normally

from typing import Mapping


def catAndMouse(CatA, CatB, Mouse):
    
    distance1 = abs(CatA-Mouse)
    distance2 = abs(CatB-Mouse)
    
    if distance1 == distance2: # mouse will escape
        return "Mouse C"
    elif distance1 > distance2:
        return "Cat B"
    else:
        return "Cat A" 
    


if __name__ == '__main__':
    
    n = int(input("n = "))

    for q_itr in range(n):
        xyz = input().split()

        CatA = int(xyz[0])

        CatB = int(xyz[1])

        Mouse = int(xyz[2])

        result = catAndMouse(CatA, CatB, Mouse)
        
        print(result) # who will catch first or Mouse will escape
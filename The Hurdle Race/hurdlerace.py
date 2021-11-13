def hurdlerace(max_jump,hurdles_hight):
    
    if max(hurdles_hight) > max_jump:
        dose = max(hurdles_hight) - max_jump
    else:
        return 0
        
    return "Need " + str(dose) + " doses"
            

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    hurdles_hight = list(map(int, input().rstrip().split()))
    
    print(hurdlerace(k,hurdles_hight))
    
    
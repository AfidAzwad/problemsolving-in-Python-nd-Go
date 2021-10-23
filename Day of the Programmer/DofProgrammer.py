def dayOfProgrammer(year):
    # Write your code here
    total = 243 # total days of 1st 8 months of a year
    
    if year == 1918:
        if year%4 ==0:
            pday = 256 - (total+1-13)
            return str(pday) + ".09." + str(year)
        else:
            pday = 256 - (total-13)
            return str(pday) + ".09." + str(year)

    elif (year <=1917 and year%4==0) or (year%400 == 0 or year%4 == 0 and year%100!=0):
        pday = 256 - (total+1)
        return str(pday) + ".09." + str(year)
    else:
        pday = 256 - total
        return str(pday) + ".09." + str(year)
        
if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)
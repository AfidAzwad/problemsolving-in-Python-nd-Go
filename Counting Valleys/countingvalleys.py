def countingvalleys(steps):

    altitude, valley = 0, 0
    
    for i in steps:

        if i == "U": # for climbing up altitude changing to positive 1
            altitude += 1
        else:        # for climbing down altitude changing to negative 1
            altitude -= 1
        
        if altitude == 0 and i == 'U': # when hikers are on sea level at the end, altitude will be 0 as starting

            valley += 1  # total valley

    return "Valley : " + str(valley)

if __name__ == '__main__':

    # path = ['U','D','D','D','U','D','U','U'] # 2nd option

    path = input("Path : ") # UDDDUDUU  [ U = Up and D = Down ]

    print(countingvalleys(path))
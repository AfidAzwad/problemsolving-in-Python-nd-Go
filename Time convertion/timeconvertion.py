def convert(Tinput):

    print("Input :", Tinput)
    print(Tinput[:2])
    print(Tinput[2:-2])
    print(Tinput[-2:])
    print(Tinput[:-2])

    if Tinput[-2:] == "AM" and Tinput[:2] == "12":
            return "00" + Tinput[2:-2]

    # removing AM    
    elif Tinput[-2:] == "AM":
        return Tinput[:-2]
      
    # Checking if last two elements of time is PM and first two elements are 12   
    elif Tinput[-2:] == "PM" and Tinput[:2] == "12":
        return Tinput[:-2]

    else:
        # add 12 to hours and remove PM
        return str(int(Tinput[:2]) + 12) + Tinput[2:8]

if __name__ == '__main__':
    
    print("Converted in 24 format:",convert("12:05:45 PM"), "\n")
    
    print("Converted in 24 format:",convert("08:05:45 PM"), "\n")
    
    print("Converted in 24 format:",convert("12:05:45 AM"), "\n")


    
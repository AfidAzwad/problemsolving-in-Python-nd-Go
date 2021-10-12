# 1. The withdrawal amount must be greater than or equal to 500. If not ---> Print “INVALID AMOUNT”
# 2. Amount must be multiple of 500. If not ---> Print “Amount should be x500 !!"
# 3. The maximum amount must be less than or equal to 20,000. If not ---> Print “EXCEEDED AMOUNT” 
# 4. If the requested amount passes all the above conditions ---> print “TRANSACTION SUCCESSFUL”. 

def checkammount(amount):

    if amount >= 500:              # condition 1

       if amount%500 != 0:         # condition 2
           print("Amount should be x500 !! ")

       elif amount > 20000:        # condition 3
           print("EXCEEDED AMOUNT")
           
       else:                       # condition 4
           print("TRANSACTION SUCCESSFUL")

    else:
        print("INVALID AMOUNT")

if __name__ == '__main__':

    N = int(input("Amount to withdraw: "))

    checkammount(N)
    
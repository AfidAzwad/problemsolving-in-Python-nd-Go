def bonAppetit(bill, k, Billcharged):
    # Write your code here
    del bill[k]
    total = 0
    
    for i in range(len(bill)):
        total += bill[i]
    
    Billactual = int(total/2)

    if Billactual == Billcharged:
        print("Bon Appetit")
    else:
        print("Brian owes Anna :",Billcharged-Billactual)



if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])


    bill = list(map(int, input("Bills list :").rstrip().split()))

    b = int(input("Brian bill charged Anna : ").strip())
    
    bonAppetit(bill, k, b)
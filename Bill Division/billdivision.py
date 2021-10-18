def bonAppetit(bill, k, b):
    # Write your code here
    bill = bill.remove(k)

    total = 0
    
    for i in range(len(bill)):
        total += bill[i]
    
    pay = int(total/2)

    if pay == b:
        print("Bon Appetit")
    else:
        print(b-pay)



if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])


    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())
    
    print(n,k,b)

    bonAppetit(bill, k, b)
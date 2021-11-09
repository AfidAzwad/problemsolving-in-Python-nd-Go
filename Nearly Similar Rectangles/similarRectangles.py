def nearlySimilarRectangles(sides):
    # Write your code here
    count = 0 # a/c = b/d means nearly similar rectangle
    L = len(sides)
    k = L-1
        
    for a,b in sides:
        for c in range( L - k, L ):           
           if a/sides[c][0] == b/sides[c][1]:
                   count += 1
        k-=1
          
    return "Pairs : " + str(count)

if __name__ == '__main__':
    # sides_rows = int(input().strip())
    # sides_columns = int(input().strip())

    # sides = []

    # for _ in range(sides_rows):
    #     sides.append(list(map(int, input().rstrip().split())))

#     arr = [[10 ,7],
# [9, 5],
# [6 ,9],
# [7 ,3] ]
    arr = [ [4, 8], [15,30], [25,50] ]

    result = nearlySimilarRectangles(arr)
    
    print(result)

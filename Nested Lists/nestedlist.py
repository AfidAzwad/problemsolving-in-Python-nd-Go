if __name__ == '__main__':

    n = int(input().strip())
    
    grades = []
    
    for _ in range(0,n):
        grades.append([input(), float(input())])


    secondlowest = sorted(list(set([marks for name,marks in grades])))[1] #sorting to find second lowest

    print("Second lowest mark : ", secondlowest)

    
    print('\n'.join([a for a,b in sorted(grades) if b == secondlowest]))
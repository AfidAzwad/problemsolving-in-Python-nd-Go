def pickingNumbers(a):
    # Write your code here
    a.sort()
    
    multiset = []
    
    for i in range(0, len(a)):
          c = 1
          for j in range(i+1, len(a)):
                if a[i] == a[j] or a[j]- a[i] == 1:
                      c+=1
          multiset.append(c)
  
    return max(multiset)
  

if __name__ == '__main__':

    n = int(input("n = ").strip())

    a = list(map(int, input().rstrip().split()))
    
    result = pickingNumbers(a)
    print(result)
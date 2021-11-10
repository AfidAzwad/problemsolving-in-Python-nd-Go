def pickingNumbers(a):
      
    print("Array : " ,a)

    a.sort()
    multiset = []
    
    print("Sorted Array : " ,a)
    
    for i in range(0, len(a)):
          c = 1
          for j in range(i+1, len(a)):
                if a[i] == a[j] or a[j]- a[i] == 1:
                      c+=1
          multiset.append(c)
          
    print("Multiset with lengths of subarrays: ", multiset)
    
    return "Largest subarray lenght is :" + str(max(multiset))
  

if __name__ == '__main__':

    n = int(input("n = ").strip())
    a = list(map(int, input().rstrip().split()))
    
    result = pickingNumbers(a)
    print(result)
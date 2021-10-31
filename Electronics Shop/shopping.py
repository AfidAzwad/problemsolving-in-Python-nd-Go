def getMoneySpent(keyboards, drives, budget):

    result = [(i+j) for i in keyboards for j in drives if i != j] # sum of pairs of the 2 lists

    combo = [] # to store budget friendly sums

    for i in result:
        if i <= budget:
            combo.append(i)

    if combo == []: 
        return -1
    else:
        return max(combo)  # expensive pairs from the budget friendly sums


if __name__ == '__main__':

    b = int(input("budget = ").strip())


    keyboards = list(map(int, input("keyborads prices : ").rstrip().split()))

    drives = list(map(int, input("drives prices : ").rstrip().split()))



    print(getMoneySpent(keyboards, drives, b))

from bisect import bisect_right

def climbingLeaderboard(ranked, player):
    rank = list(set(ranked))
    rank.sort()
        
    for i in player:
      print(len(rank)-bisect_right(rank,i)+1) # +1 for ranking starts from 1 not 0
    
if __name__ == '__main__':
    
    ranked = [100, 100, 50, 40, 40, 20, 10]
    player = [5, 25, 50, 120]
    
    result = climbingLeaderboard(ranked, player)

def climbingLeaderboard(ranked, player):
    rank = list(set(ranked))
    
    for i in player:
        rank.append(i)
        rank.sort(reverse=True)
        print(rank.index(i)+1) # +1 for ranking starts from 1 not 0
        
if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))
    
    result = climbingLeaderboard(ranked, player)

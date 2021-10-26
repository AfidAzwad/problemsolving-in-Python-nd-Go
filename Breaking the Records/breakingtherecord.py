from collections import OrderedDict


def breakingTheRecord(score):

    scores = list(OrderedDict.fromkeys(score))  # to avoid duplicate values

    highstscore = scores[0]
    highcount = 0
    lowestscore = scores[0]
    lowcount = 0

    for i in range(1, len(scores)):
        # finding the numbers of highest scores in the whole Game
        if highstscore < scores[i]:
            highstscore = scores[i]
            highcount += 1
        # finding the numbers of lowest scores in the whole Game
        elif lowestscore > scores[i]:
            lowestscore = scores[i]
            lowcount += 1

    return highcount, lowcount


if __name__ == '__main__':
    n = int(input("game = ").strip())  # Game numbers

    score = list(map(int, input().split()))  # scores per game

    result = breakingTheRecord(score)

    print(result)

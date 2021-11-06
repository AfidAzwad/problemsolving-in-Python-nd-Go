def transformSentence(sentence):
    sentence.strip()
    result = ''   #empty string
    index = 0

    for i in sentence:
        if(index==0):
            result+= i
            index+=1
        elif(i == ' '):
            result += i
            index+=1
        else:
            y = sentence[index-1]
            if(y==' '): # 1st letter of a word will be unchanged
                result+= i
                index+=1
            elif(y.lower() < i.lower()): # if next letter is greater than previous one
                result += i.upper()
                index+=1
            elif(y.lower()>i.lower()):
                result += i.lower()
                index+=1
            else:
                result+= i
                index+=1
    return result

if __name__ == '__main__':
    s = input().strip()

    print(transformSentence(s))
def designerPdfViewer(h, word):
    
    p =  [h[ord(w)-ord('a')] for w in word ] # h[122 - 97] = h[25] = height of z
    
    print("value of a in ASCII :", ord('a'))
    
    print("value of z in ASCII :", ord('z'))
            
    print(p)
          
    return "The selection area for this word is " + str(max(p)*len(word))


if __name__ == '__main__':
    
    word = 'zaba'
    
    height = [1 ,3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]

    result = designerPdfViewer(height, word)
    
    print(result)
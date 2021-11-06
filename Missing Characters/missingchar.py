import string

def missingCharacters(s):

    duplicateremoved = list(set(s))

    alphabet_string = list(string.ascii_lowercase)

    numeric_list = []

    for i in range(0, 10):
        numeric_list.append(str(i)) # adding 0 to 9 as string
      
    for i in range(len(duplicateremoved)):
        if duplicateremoved[i]>= 'a' and duplicateremoved[i] <= 'z': # checking a to z
            alphabet_string.remove(duplicateremoved[i])
        elif duplicateremoved[i]>= '0' and duplicateremoved[i] <= '9': # checking 0 to 9
            numeric_list.remove(duplicateremoved[i])

    str1 = ""
    str2 = ""

    return str2.join(numeric_list)+str1.join(alphabet_string)

if __name__ == '__main__':

    s = input().lower()

    result = missingCharacters(s)
    print(result)
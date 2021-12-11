def decryptPassword(s):
    decryptedstring = ''
    numer = [] # to store numeric value 
    S = list(s)
    for i in s:
        if i > '0' and i <= '9':
            numer.append(i)
        elif i == '0':
            decryptedstring += numer[len(numer)-1] # replacing 0 with numeric value in reverse order
            numer.remove(numer[len(numer)-1])
        elif i == '*':
            decryptedstring += S[S.index(i)-1] # swapping
            decryptedstring += S[S.index(i)-2] # swapping
            S.remove(i) # removing * from List S
        elif i.lower() >= 'a' and i.lower() <= 'z':
            if s.index(i) == 0 or s.index(i) == len(s)-1: # checking if i is 1st or last item
                decryptedstring += i
            else:
                continue
        else:
            decryptedstring += i
    return decryptedstring

if __name__ == '__main__':
    s = input("Encrypted message : ").rstrip()  # input: pto*ta*O or 51Pa*0Lp*0e
    result = decryptPassword(s)
    print("Decrypted message : ", result)
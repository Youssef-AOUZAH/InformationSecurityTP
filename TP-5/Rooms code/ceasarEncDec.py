import string

lowerAlphabets=list(string.ascii_lowercase)
upperAlphabets=list(string.ascii_uppercase)
#text may have ponctuation and space,we gotta make sure we only shift letters
def shifter(c,shift):
    shift=shift%26
    if c in lowerAlphabets:
        indexElement=lowerAlphabets.index(c)
        return lowerAlphabets[(indexElement+shift)%26]
    elif c in upperAlphabets:
        indexElement=upperAlphabets.index(c)
        return upperAlphabets[(indexElement+shift)%26]
    else:
        return c




def ceasarEnc(text,shift):
    
    listText=list(text)
    
    currentIndex=0
    for c in listText:
        listText[currentIndex]=shifter(c,shift)
        currentIndex+=1
    return ''.join(listText)

def ceasarDec(cipher,shift):
    return ceasarEnc(cipher,(-1)*shift)

def ceasarBruteForce(cipher):
    listTexts=[]
    for i in range(26):
        listTexts.append(ceasarDec(cipher,i)) #including the original cipher just in case it wasnt even encrypted
    return listTexts



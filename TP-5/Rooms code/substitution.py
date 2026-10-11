import string
from collections import Counter
def substituionEnc(message, assignedAlphabets): 
    cipher = list(message)  
    for index in range(len(message)):  
        char = message[index]
        if char.isalpha():
            for tup in assignedAlphabets: 
                if tup[0].lower() == char.lower():  
                    if char.islower():  
                        cipher[index] = tup[1].lower() 
                    else:
                        cipher[index] = tup[1].upper() 
                    break

    return ''.join(cipher)  


def substituionDec(cipher, assignedAlphabets):
    
    swapped = [(c, p) for (p, c) in assignedAlphabets]
    return substituionEnc(cipher, swapped)


def closestMatche(tupleCipher, frequs):
    dist = abs(tupleCipher[1] - frequs[0][1])
    assigned = frequs[0]
    for frequTuple in frequs:
        if abs(tupleCipher[1] - frequTuple[1]) < dist:
            dist = abs(tupleCipher[1] - frequTuple[1])
            assigned = frequTuple
    return (tupleCipher[0], assigned[0])


def substituionDecFrequ(cipher, frequs): 
 
    letterCipherFrequs = list(Counter(c.upper() for c in cipher if c.isalpha()).items())
    
    numberOfAlphas = sum(count for _, count in letterCipherFrequs)
    lettersCipherFrequs = [(frequ[0], (frequ[1] / numberOfAlphas) * 100) for frequ in letterCipherFrequs]
   
    lettersCipherFrequs.sort(key=lambda x: x[1], reverse=True)

 
    available_frequs = list(frequs)
    assignedLetters = []
    for tupleCipher in lettersCipherFrequs:
        if available_frequs:
            match = closestMatche(tupleCipher, available_frequs)
            assignedLetters.append(match)
         
            available_frequs = [f for f in available_frequs if f[0] != match[1]]

    return substituionEnc(cipher, assignedLetters)


def letterFrequs(text):
    
    if isinstance(text, (list, tuple)):
        text = ''.join(str(item) for item in text)

    counts = {}
    for char in text:
        if char.isalpha():
            c = char.lower()
            counts[c] = counts.get(c, 0) + 1

    sorted_letters = sorted(counts, key=counts.get, reverse=True)
    return sorted_letters


def decryptGroupE(lettersGroup):
    frequentLetter = letterFrequs(lettersGroup)[0].upper()
    shift = (ord(frequentLetter) - ord('E')) % 26
    keyChar = chr(ord('A') + shift)

    decrypted = []
    for c in lettersGroup:
        if 'A' <= c <= 'Z':
            decrypted.append(chr((ord(c) - ord('A') - shift) % 26 + ord('A')))
        elif 'a' <= c <= 'z':
            decrypted.append(chr((ord(c) - ord('a') - shift) % 26 + ord('a')))
        else:
            decrypted.append(c)
    return decrypted, keyChar
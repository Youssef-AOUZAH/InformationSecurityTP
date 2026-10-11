import ceasarEncDec

message="CRYPTO IS FUN UNTIL THE PROFESSOR SAYS QUIZ"
k=4

#encrypting the message
cipher=ceasarEncDec.ceasarDec(message,k)
print(f"ceasar cipher with key=4 for {message} is {cipher}")


cipher2="GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA"
key=8
originalMessage=ceasarEncDec.ceasarDec(cipher2,key)
print(f"message from {cipher2} with key=8 is {originalMessage}")

#decrypting using brute force,we have a list of 26 potentiel decryptions ,and we should be able to find the correct one manualy
cipher3="ESP VPJ TD FYVYZHY ECJ MCFEP QZCNP"
listDecrypted=ceasarEncDec.ceasarBruteForce(cipher3)
print(f"Decrypting {cipher3} with brute force leads to the next list of elements \n")
print(listDecrypted)


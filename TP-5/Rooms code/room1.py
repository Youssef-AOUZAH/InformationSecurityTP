import substitution
message="KEEP THE SECRET SAFE"
assignedAlphabets = [
    ('A', 'Q'), ('B', 'M'), ('C', 'J'), ('D', 'Z'), ('E', 'T'),
    ('F', 'G'), ('G', 'F'), ('H', 'K'), ('I', 'P'), ('J', 'W'),
    ('K', 'L'), ('L', 'S'), ('M', 'B'), ('N', 'O'), ('O', 'X'),
    ('P', 'N'), ('Q', 'C'), ('R', 'R'), ('S', 'Y'), ('T', 'E'),
    ('U', 'V'), ('V', 'H'), ('W', 'I'), ('X', 'A'), ('Y', 'D'),
    ('Z', 'U')
]

cipher=substitution.substituionEnc(message,assignedAlphabets)

print(f"The cipher for {message} is {cipher}")

cipher2="ERVYE DXVR SXFPJ"
print(f"The message for {cipher} is {substitution.substituionDec(cipher2,assignedAlphabets)}")




interceptedCipher="""EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK.
STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,
MVE PE FPHTY Q FXXZ YEQRE.
SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,
QOZ YKXRE IXRZY.
IKTO DXV RTJXHTR EKT BTYYQFT,
EKT HPFTOTRT LTD KQY GXVR STEETRY."""

frequs = [
    ('E', 12.7),
    ('T', 9.1),
    ('A', 8.2),
    ('O', 7.5),
    ('I', 7.0),
    ('N', 6.7),
    ('S', 6.3),
    ('H', 6.1),
    ('R', 6.0),
    ('D', 4.3),
    ('L', 4.0),
    ('C', 2.8)
]
#The plaintext from intercepted cipher
print(substitution.substituionDecFrequ(interceptedCipher, frequs))
#which helps build the following hypothesis assignment table
assignedAlphabets2 = [
    ('A', 'Q'), ('B', 'M'), ('C', 'J'), ('D', 'Z'), ('E', 'T'),
    ('F', 'G'), ('G', 'F'), ('H', 'K'), ('I', 'P'), ('J', 'W'),
    ('K', 'L'), ('L', 'S'), ('M', 'B'), ('N', 'O'), ('O', 'X'),
    ('P', 'N'), ('Q', 'C'), ('R', 'R'), ('S', 'Y'), ('T', 'E'),
    ('U', 'V'), ('V', 'H'), ('W', 'I'), ('X', 'A'), ('Y', 'D'),
    ('Z', 'U')
]

#which reveals the true plaintext for the intercepted cipher
print(f"{substitution.substituionDec(interceptedCipher,assignedAlphabets2)}")


import substitution

ciphertext = """VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZL
GFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVC
OPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWL
GOFGGGVAQFGIEZLTUS
""".replace("\n", "").replace(" ", "").strip()


group1 = ciphertext[0::4]
group2 = ciphertext[1::4]
group3 = ciphertext[2::4]
group4 = ciphertext[3::4]

groups = [group1, group2, group3, group4]

decryptedGroups = []
recoveredKey = []
for group in groups:
    decGroup, keyChar = substitution.decryptGroupE(group)
    decryptedGroups.append(decGroup)         
    recoveredKey.append(keyChar)

key = "".join(recoveredKey)
print(f"Recovered Vigenere Key: {key}")

assembledText = []
for i in range(len(ciphertext)):
    groupIndex = i % 4
    charIndex = i // 4
    assembledText.append(decryptedGroups[groupIndex][charIndex])

plaintext = "".join(assembledText)
print("\nDecrypted Message:")
print(plaintext)
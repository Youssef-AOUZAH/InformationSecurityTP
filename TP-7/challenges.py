
from PIL import Image
import collections

#challenge 1.1
p = 5
q = 11
e = 3
C = 23

n=p*q
phi=(p-1)*(q-1)
d=pow(e,-1,phi)

#decryption
m=pow(C,d,n)
print(m)


#encryption

cipher=pow(m,e,n)
print(cipher==C)


#Mission 2
#challenge 1



from PIL import Image

WIDTH = 432
HEIGHT = 475
BLOCK_SIZE = 16
HEADER_SIZE = 16

with open("classified.enc", "rb") as f:
    data = f.read()

ciphertext = data[HEADER_SIZE:]

block_map = {}
unique_id = 0
pixels = []


for i in range(0, len(ciphertext), BLOCK_SIZE):
    block = ciphertext[i:i+BLOCK_SIZE]
    

    if block not in block_map:
        block_map[block] = unique_id
        unique_id += 1
        

    val = (block_map[block] * 37) % 256
    
    pixels.extend([val] * 16)

pixels = pixels[:WIDTH * HEIGHT]

img = Image.new("L", (WIDTH, HEIGHT))
img.putdata(pixels)
img.save("pattern_ecb.png")
print(f"Found {unique_id} unique blocks. Saved pattern_ecb.png")





with open("recovered.raw", "rb") as f:
    raw_data = f.read()

raw_data = raw_data[:WIDTH * HEIGHT]

img = Image.new("L", (WIDTH, HEIGHT))
img.putdata(raw_data)
img.save("recovered.png")

print("Done! The original image has been saved as recovered.png")
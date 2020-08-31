import binascii
filename = 'test.jpg'
with open(filename, 'rb') as f:
    content = f.read()
with open("hex.txt", 'w+') as file:
    file.write(str(binascii.hexlify(content)))

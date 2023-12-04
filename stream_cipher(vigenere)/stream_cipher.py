from textwrap import wrap

plaintext = input("Plaintext: ")
key = input("Key: ")

repeatKey = (len(plaintext) + len(key) - 1) // len(key)
repeatResult = key * repeatKey
repeatResult = repeatResult[:len(plaintext)]

plainBit = plaintext.encode('utf-8')
keyBit = repeatResult.encode('utf-8')

plainBinary = ''.join(format(byte, '08b') for byte in plainBit)
keyBinary = ''.join(format(byte, '08b') for byte in keyBit)

encryptedBinary = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(plainBinary, keyBinary))

decryptedBinary = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(encryptedBinary, keyBinary))

block = wrap(decryptedBinary, 8)

ascii = ''.join(chr(int(blok, 2)) for blok in block)

print("repeat: ", repeatKey)
print("repeatResult: ", repeatResult)
print("plainBit: ", plainBit)
print("keyBit: ", keyBit)
print("plainBinary: ", plainBinary)
print("keyBinary: ", keyBinary)
print("Encrypt: ", encryptedBinary)
print("Decrypt: ", decryptedBinary)
print("block: ", block)
print("ascii: ", ascii)

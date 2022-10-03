#a = "Hello World"
#e = "HFNOS XQUPD"

file3 = open('outputtext.txt', 'a')

def encrypt(plaintext, key):    
    index = 0
    b = ""
    for i in plaintext:
        b += chr(ord(i) + (index % key))
        index+=1
    file3.write(b.upper())

def decrypt(encryptedtext, key):
    index = 0
    b = ""
    for i in encryptedtext:
        b += chr(ord(i) - (index % key))
        index+=1
    file3.write(b.lower())

o = int(input("1. Encryption\n2. Decryption\nEnter Choice:\n"))
key = int(input("Enter key:\n"))
if(o == 1):
    file1 = open('plaintext.txt', 'r')
    p = file1.read()
    encrypt(p, key)
elif(o == 2):
    file2 = open('encryptedtext.txt', 'w')
    e = file2.read()
    decrypt(e, key)
else:
    print("invalid input")

file1 = open('plaintext.txt', 'r')
a = file1.read()

file2 = open('encryptedtext.txt', 'w')
a = "Hello World"
e = "HFNOS XQUPD"

key = int(input("Enter key:\n"))

def encrypt(plaintext):    
    index = 0
    b = ""
    for i in plaintext:
        b += chr(ord(i) + (index % key))
        index+=1
    file2.write(b.upper())

def decrypt(encryptedtext):
    index = 0
    b = ""
    for i in encryptedtext:
        b += chr(ord(i) - (index % key))
        index+=1
    file2.write(b.lower())
    
encrypt(a)
decrypt(e)

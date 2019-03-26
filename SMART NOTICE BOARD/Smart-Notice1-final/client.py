import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9990

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
tm = s.recv(1024)                                     


plainText = 'aaa'
shift = 2
#global cipherText
cipherText = ""
def caesar(plainText, shift, cipherText): 

    for ch in plainText:

        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
        cipherText = cipherText + finalLetter
        print (cipherText)
 #       print (cipherText, end='')

    return cipherText

caesar(plainText, shift, cipherText)
s.sendall(bytes("The encrypted message is ",cipherText))
print("The Decrypted message from server is %s" % tm.decode('ascii'))

s.close()





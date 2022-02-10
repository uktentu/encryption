# Encrypter
def encrypt(s,key):
    key = int(key)
    encrypt=[]
    if ((key/26)>1)or(key<0):
        key = key%26
    for i in list(s):
        j=ord(i)
        if (ord(i)>=65 and ord(i)<=90):
            for k in range(key):
                j+=1
                if j>90:
                    j=64+(key-k)
                    break
            encrypt.append(chr(j))
        elif (ord(i)>=97 and ord(i)<=122):
            for k in range(key):
                j+=1
                if j>122:
                    j=96+(key-k)
                    break
            encrypt.append(chr(j))
        else:
            encrypt.append(i)
    return ''.join(encrypt)


# Decoder
def decoder(s,key):
    key = int(key)
    decrypt=[]
    if ((key/26)>1) or key<0:
        key = key%26
    for i in list(s):
        j=ord(i)
        if (ord(i)>=65 and ord(i)<=90):
            for k in range(key):
                j-=1
                if j<65:
                    j=90-(key-k-1)
                    break
            decrypt.append(chr(j))
        elif (ord(i)>=97 and ord(i)<=122):
            for k in range(key):
                j-=1
                if j<97:
                    j=122-(key-k-1)
                    break
            decrypt.append(chr(j))
        else:
            decrypt.append(i)
    return ''.join(decrypt)

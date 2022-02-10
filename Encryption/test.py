from base64 import decode
from encryption import *

# assign any number to key but sont forget to use the same at decoding
key=8

#for encryption
print(  encrypt(    "helloworld"    ,key    )   )

# for decoding 
print(  decode(     "pmttwewztl"    ,key    )   )
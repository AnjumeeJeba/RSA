from __future__ import print_function
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
import codecs

import time
import psutil

start = time.time()  # starting time

message = b'Troye'
key = RSA.import_key(open('private.key').read())  # import private key
h = SHA256.new(message)  # create a hash of the message

'''
once hashing is done, we need to create a sign object through 
which we can sign a message
'''
time.sleep(1)  # sleeping for 1 sec to get 10 sec runtime
# signer = pkcs1_15.new(key)
# signature=signer.sign(h)
# sign the message
signature = pkcs1_15.new(key).sign(h)
signature_readable = codecs.getencoder('hex')(signature)
print(signature.hex())

# save signature and message
file_out = open("signature.pem", "wb")
file_out.write(signature)
file_out.close()

file_out = open("message.txt", "wb")
file_out.write(message)
file_out.close()

time.sleep(1)  # sleeping for 1 sec to get 10 sec runtime
end = time.time()  # end time
print(f"Runtime of the program is  {end - start}")  # total time taken
print('CPU  % used:', psutil.cpu_percent())
print('physical memory  % used:', psutil.virtual_memory())  # physical memory usage
print('memory % used:', psutil.virtual_memory()[2])

import hashlib
import os
import sys

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()
sha512 = hashlib.sha512()

BUFFER_SIZE = 65536

def updateHash(hash):
    with open(sys.argv[1], 'rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            hash.update(data)

whichHash = str(input('''Which hash do you want?\n
    1 = MD5
    2 = SHA1
    3 = SHA256
    4 = SHA512\n'''))

if whichHash == '1':
    print("MD5: {0}".format(md5.hexdigest()))
elif whichHash == '2':
    updateHash(sha1)
    print("SHA1: {0}".format(sha1.hexdigest()))
elif whichHash == '3':
    updateHash(sha256)
    print("SHA256: {0}".format(sha256.hexdigest()))
elif whichHash == '4':
    updateHash(sha512)
    print("SHA512: {0}".format(sha512.hexdigest()))
else:
    print('Please select one of the options listed, by entering the corresponding number.')
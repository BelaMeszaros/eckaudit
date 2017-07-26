import passlib.hash

def hashed_password(password):
    return passlib.hash.pbkdf2_sha256.hash(password)

def verify_password(password, hash):
    return passlib.hash.pbkdf2_sha256.verify(password, hash)

password = "abCD_1234"
hash1 = hashed_password(password)
hash2 = hashed_password(password)

print ("Hash1: ", len(hash1), " ", verify_password(password, hash1))
print ("Hash2: ", len(hash2), " ", verify_password(password, hash2))

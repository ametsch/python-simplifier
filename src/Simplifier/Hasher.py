import hashlib as hl
__doc__ = '''
    A class of functions to easily run a value through a variety of hash functions
'''

def hash_md5(e) -> str:
    return hl.md5(str(e).encode()).hexdigest()

def hash_sha1(e) -> str:
    return hl.sha1(str(e).encode()).hexdigest()

def hash_sha256(e) -> str:
    return hl.sha256(str(e).encode()).hexdigest()

def hash_sha512(e) -> str:
    return hl.sha512(str(e).encode()).hexdigest()

def hash_sha224(e) -> str:
    return hl.sha224(str(e).encode()).hexdigest()

def hash_sha384(e) -> str:
    return hl.sha384(str(e).encode()).hexdigest()

def hash_sha3_512(e) -> str:
    return hl.sha3_512(str(e).encode()).hexdigest()

def hash_sha3_256(e) -> str:
    return hl.sha3_256(str(e).encode()).hexdigest()

def hash_sha3_224(e) -> str:
    return hl.sha3_224(str(e).encode()).hexdigest()

def hash_sha3_384(e) -> str:
    return hl.sha3_384(str(e).encode()).hexdigest()

def hash_shake128(e) -> str:
    return hl.shake_128(str(e).encode()).hexdigest()

def hash_shake256(e) -> str:
    return hl.shake_256(str(e).encode()).hexdigest()

def hash_blake2b(e) -> str:
    return hl.blake2b(str(e).encode()).hexdigest()

def hash_blake2s(e) -> str:
    return hl.blake2s(str(e).encode()).hexdigest()

def hash_x_blake2b(e, i: int) -> str:
    if i <= 1:
        return hash_blake2b(e)
    else:
        return hash_x_blake2b(e, i-1)

def hash_x_blake2s(e, i: int) -> str:
    if i <= 1:
        return hash_blake2s(e)
    else:
        return hash_x_blake2s(e, i-1)

def hash_x_sha512(e, i: int) -> str:
    if i <= 1:
        return hash_sha512(e)
    else:
        return hash_x_sha512(e, i-1)

def hash_x_md5(e, i: int) -> str:
    if i <= 1:
        return hash_md5(e)
    else:
        return hash_x_md5(e, i-1)

def hash_x_sha3_512(e, i: int) -> str:
    if i <= 1:
        return hash_sha3_512(e)
    else:
        return hash_x_sha3_512(e, i-1)

def hash_x_sha1(e, i: int) -> str:
    if i <= 1:
        return hash_sha1(e)
    else:
        return hash_x_sha1(e, i-1)

def hash_x_sha384(e, i: int) -> str:
    if i <= 1:
        return hash_sha384(e)
    else:
        return hash_x_sha384(e, i-1)

def hash_x_sha224(e, i: int) -> str:
    if i <= 1:
        return hash_sha224(e)
    else:
        return hash_x_sha224(e, i-1)

def hash_x_shake256(e, i: int) -> str:
    if i <= 1:
        return hash_shake256(e)
    else:
        return hash_x_shake256(e, i-1)

def hash_x_shake128(e, i: int) -> str:
    if i <= 1:
        return hash_shake128(e)
    else:
        return hash_x_shake128(e, i-1)

def hash_x_sha3_384(e, i: int) -> str:
    if i <= 1:
        return hash_sha3_384(e)
    else:
        return hash_x_sha3_384(e, i-1)

def hash_x_sha3_224(e, i: int) -> str:
    if i <= 1:
        return hash_sha3_224(e)
    else:
        return hash_x_sha3_224(e, i-1)

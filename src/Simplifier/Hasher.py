import hashlib as hl
__doc__ = '''
    A group of functions to easily run a value through a variety of hash functions
'''

def md5(e) -> str:
    return hl.md5(str(e).encode()).hexdigest()

def sha1(e) -> str:
    return hl.sha1(str(e).encode()).hexdigest()

def sha256(e) -> str:
    return hl.sha256(str(e).encode()).hexdigest()

def sha512(e) -> str:
    return hl.sha512(str(e).encode()).hexdigest()

def sha224(e) -> str:
    return hl.sha224(str(e).encode()).hexdigest()

def sha384(e) -> str:
    return hl.sha384(str(e).encode()).hexdigest()

def sha3_512(e) -> str:
    return hl.sha3_512(str(e).encode()).hexdigest()

def sha3_256(e) -> str:
    return hl.sha3_256(str(e).encode()).hexdigest()

def sha3_224(e) -> str:
    return hl.sha3_224(str(e).encode()).hexdigest()

def sha3_384(e) -> str:
    return hl.sha3_384(str(e).encode()).hexdigest()

def shake128(e) -> str:
    return hl.shake_128(str(e).encode()).hexdigest()

def shake256(e) -> str:
    return hl.shake_256(str(e).encode()).hexdigest()

def blake2b(e) -> str:
    return hl.blake2b(str(e).encode()).hexdigest()

def blake2s(e) -> str:
    return hl.blake2s(str(e).encode()).hexdigest()

def multi_blake2b(e, i: int) -> str:
    if i <= 1:
        return blake2b(e)
    else:
        return multi_blake2b(e, i-1)

def multi_blake2s(e, i: int) -> str:
    if i <= 1:
        return blake2s(e)
    else:
        return multi_blake2s(e, i-1)

def multi_sha512(e, i: int) -> str:
    if i <= 1:
        return sha512(e)
    else:
        return multi_sha512(e, i-1)

def multi_md5(e, i: int) -> str:
    if i <= 1:
        return md5(e)
    else:
        return multi_md5(e, i-1)

def multi_sha3_512(e, i: int) -> str:
    if i <= 1:
        return sha3_512(e)
    else:
        return multi_sha3_512(e, i-1)

def multi_sha1(e, i: int) -> str:
    if i <= 1:
        return sha1(e)
    else:
        return multi_sha1(e, i-1)

def multi_sha384(e, i: int) -> str:
    if i <= 1:
        return sha384(e)
    else:
        return multi_sha384(e, i-1)

def multi_sha224(e, i: int) -> str:
    if i <= 1:
        return sha224(e)
    else:
        return multi_sha224(e, i-1)

def multi_shake256(e, i: int) -> str:
    if i <= 1:
        return shake256(e)
    else:
        return multi_shake256(e, i-1)

def multi_shake128(e, i: int) -> str:
    if i <= 1:
        return shake128(e)
    else:
        return multi_shake128(e, i-1)

def multi_sha3_384(e, i: int) -> str:
    if i <= 1:
        return sha3_384(e)
    else:
        return multi_sha3_384(e, i-1)

def multi_sha3_224(e, i: int) -> str:
    if i <= 1:
        return sha3_224(e)
    else:
        return multi_sha3_224(e, i-1)

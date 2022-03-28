import hashlib as hl
class Hasher:
    def __init__(self):
        pass

    def hash_md5(self, e):
        return hl.md5(str(e).encode()).hexdigest()

    def hash_sha1(self, e):
        return hl.sha1(str(e).encode()).hexdigest()

    def hash_sha256(self, e):
        return hl.sha256(str(e).encode()).hexdigest()

    def hash_sha512(self, e):
        return hl.sha512(str(e).encode()).hexdigest()

    def hash_sha224(self, e):
        return hl.sha224(str(e).encode()).hexdigest()

    def hash_sha384(self, e):
        return hl.sha384(str(e).encode()).hexdigest()

    def hash_sha3_512(self, e):
        return hl.sha3_512(str(e).encode()).hexdigest()

    def hash_sha3_256(self, e):
        return hl.sha3_256(str(e).encode()).hexdigest()

    def hash_sha3_224(self, e):
        return hl.sha3_224(str(e).encode()).hexdigest()

    def hash_sha3_384(self, e):
        return hl.sha3_384(str(e).encode()).hexdigest()

    def hash_shake128(self, e):
        return hl.shake_128(str(e).encode()).hexdigest()

    def hash_shake256(self, e):
        return hl.shake_256(str(e).encode()).hexdigest()

    def hash_blake2b(self, e):
        return hl.blake2b(str(e).encode()).hexdigest()

    def hash_blake2s(self, e):
        return hl.blake2s(str(e).encode()).hexdigest()

    def hash_x_blake2b(self, e, i: int):
        if i <= 1:
            return self.hash_blake2b(e)
        else:
            return self.hash_x_blake2b(e, i-1)
    
    def hash_x_blake2s(self, e, i: int):
        if i <= 1:
            return self.hash_blake2s(e)
        else:
            return self.hash_x_blake2s(e, i-1)

    def hash_x_sha512(self, e, i: int):
        if i <= 1:
            return self.hash_sha512(e)
        else:
            return self.hash_x_sha512(e, i-1)

    def hash_x_md5(self, e, i: int):
        if i <= 1:
            return self.hash_md5(e)
        else:
            return self.hash_x_md5(e, i-1)

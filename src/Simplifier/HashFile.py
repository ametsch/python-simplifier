from Simplifier import Hasher as h
from Simplifier import FileHelper as fh


def sha1(inPath: str) -> None:
    contents = fh.readFile(inPath)
    hash = h.sha1(contents)
    fh.strToFile(f'{inPath}.sha1.txt', hash)


def sha512(inPath: str) -> None:
    contents = fh.readFile(inPath)
    hash = h.sha512(contents)
    fh.strToFile(f'{inPath}.sha512.txt', hash)


def sha256(inPath: str) -> None:
    contents = fh.readFile(inPath)
    hash = h.sha256(contents)
    fh.strToFile(f'{inPath}.sha256.txt', hash)


def sha224(inPath: str) -> None:
    contents = fh.readFile(inPath)
    hash = h.sha224(contents)
    fh.strToFile(f'{inPath}.sha224.txt', hash)


def md5(inPath: str) -> None:
    contents = fh.readFile(inPath)
    hash = h.md5(contents)
    fh.strToFile(f'{inPath}.md5.txt', hash)


def blake2b(inPath: str) -> None:
    contents = fh.readFile(inPath)
    hash = h.blake2b(contents)
    fh.strToFile(f'{inPath}.blake2b.txt', hash)


def blake2s(inPath: str) -> None:
    contents = fh.readFile(inPath)
    hash = h.blake2s()(contents)
    fh.strToFile(f'{inPath}.blake2s.txt', hash)


def shake256(inPath: str) -> None:
    contents = fh.readFile(inPath)
    hash = h.shake256(contents)
    fh.strToFile(f'{inPath}.shake256.txt', hash)


def shake128(inPath: str) -> None:
    contents = fh.readFile(inPath)
    hash = h.shake128(contents)
    fh.strToFile(f'{inPath}.shake128.txt', hash)


def sha3_256(inPath: str) -> None:
    contents = fh.readFile(inPath)
    hash = h.sha3_256(contents)
    fh.strToFile(f'{inPath}.sha3_256.txt', hash)


def sha3_512(inPath: str) -> None:
    contents = fh.readFile(inPath)
    hash = h.sha3_512(contents)
    fh.strToFile(f'{inPath}.sha3_512.txt', hash)
nice = True
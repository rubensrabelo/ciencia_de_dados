import zlib
import hashlib

input_string = "Exemplo de string para hash"

input_bytes = input_string.encode("utf-8")

checksum = sum(input_bytes)
crc32 = zlib.crc32(input_bytes)
md5_hash = hashlib.md5(input_bytes)
sha1_hash = hashlib.sha1(input_bytes)
sha256_hash = hashlib.sha256(input_bytes)

print("String de entrada: ", input_string)
print("Checksum: ", checksum)
print("crc32: ", crc32)
print("MD5: ", md5_hash)
print("SHA-1: ", sha1_hash)
print("SHA-256: ", sha256_hash)

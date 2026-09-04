import zlib

with open("c:/Users/Debajyoti/.antigravity/wanderon/logo.png", "rb") as f:
    data = f.read()

# Extract IDAT chunks
pos = 8
idat = b""
while pos < len(data):
    length = int.from_bytes(data[pos:pos+4], "big")
    chunk_type = data[pos+4:pos+8]
    if chunk_type == b"IDAT":
        idat += data[pos+8:pos+8+length]
    pos += 12 + length

raw = zlib.decompress(idat)
# 540x540 RGBA, line size = 1 filter byte + 540*4 = 2161 bytes per line
# Check first pixel (x=0, y=0)
filter_byte = raw[0]
first_pixel = tuple(raw[1:5])
print("First pixel (RGBA):", first_pixel)

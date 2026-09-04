with open("c:/Users/Debajyoti/.antigravity/wanderon/logo.png", "rb") as f:
    data = f.read()

# PNG chunk parser to check color type
# IHDR chunk is at byte 12 to 29
# width: bytes 16-19, height: bytes 20-23, bit depth: byte 24, color type: byte 25
width = int.from_bytes(data[16:20], "big")
height = int.from_bytes(data[20:24], "big")
bit_depth = data[24]
color_type = data[25]
print(f"Width: {width}, Height: {height}, BitDepth: {bit_depth}, ColorType: {color_type}")
# ColorType 6 is RGBA, 2 is RGB, 3 is palette

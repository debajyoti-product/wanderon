from PIL import Image
import shutil

src = r"C:\Users\Debajyoti\.gemini\antigravity\brain\1cba8f28-6d21-4334-93ab-9b08570f708e\.user_uploaded\media_1788493154785.png"
dst = r"c:\Users\Debajyoti\.antigravity\wanderon\logo.png"
shutil.copyfile(src, dst)

img = Image.open(dst)
print("Dimensions:", img.size)
print("Mode:", img.mode)
# Check corners for transparency or white color
corners = [img.getpixel((0, 0)), img.getpixel((img.width-1, 0)), img.getpixel((0, img.height-1)), img.getpixel((img.width-1, img.height-1))]
print("Corner pixels:", corners)

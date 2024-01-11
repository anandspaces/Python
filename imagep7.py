from PIL import Image

img = Image.open(r"img.jpg")
img.show()
print(img.mode)
print(img.size)
print(img.format)

angle = 40
r_img = img.rotate(angle)
r_img.show()

size = (40, 40)
r_img1 = img.resize(size)
r_img1.show()

size = (40, 40)
r_img2 = img.resize(size, resample = Image.BILINEAR)
r_img2.save("resized_test.png")

img1 = Image.open(r"resized_test.png")
print(img.size)

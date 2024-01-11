import cv2
image = cv2.imread('img.jpg')
h, w = image.shape[:2]
print(f"height: {h}\nwidth: {w}")
B, G, R = image[100, 100]
print("R: {}, G: {}, B: {}".format(R, G, B))
B = image[100, 100, 0]
print("B: {}".format(B))

roi = image[100:500, 200:700]
cv2.imshow('Region of Interest', roi)
cv2.waitKey(0)

resize = cv2.resize(image, (800,800))
cv2.imshow('Resized', resize)
cv2.waitKey(0)

ratio = 800 / w
dim = (800, int(h * ratio))
resize_aspect = cv2.resize(image, dim)
cv2.imshow('Resized Aspect', resize_aspect)
cv2.waitKey(0)

center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, matrix, (w, h))
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)

output = image.copy()
rectangle = cv2.rectangle(output, (1500, 900), (600, 400), (225, 0, 0), 2)
cv2.imshow('Rectangle', output)
cv2.waitKey(0)

output1 = image.copy()
text = cv2.putText(output, 'OpenCV Demo', (500,550), cv2.FONT_HERSHEY_SIMPLEX, 4, (225, 0, 0), 2)
cv2.imshow('Text', output1)
cv2.waitKey(0)
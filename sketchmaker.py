import cv2 as cv

img = cv.imread("im2.jpg")  #read image provided by the user
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert to gray image

img_gr_inv = 255 - img_gray #inversion of gray image
img_blur = cv.GaussianBlur(img_gr_inv,ksize=(21,21),sigmaX=0,sigmaY=0) #addition of gaussian blurr to thr image

def dodgeV2(image,mask):
    return (cv.divide(image, 255 - mask, scale = 256))

def burnV2(image, mask):
    return (255 - cv.divide(255 - image, 255 - mask, scale=256))

img_blend = dodgeV2(img_gray, img_blur)

cv.imwrite('output.jpg',img_blend) #save result as output.jpg

cv.imshow("gray.jpg",img_blend) #show output to the user as gray.jpg
cv.waitKey(0)

"""
Convert the color image to grayscale.

Invert the grayscale image to get a negative.

Apply a Gaussian blur to the negative from step 2.

Blend the grayscale image from step 1 with the blurred negative from step 3 using a color dodge 

"""
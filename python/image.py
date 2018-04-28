# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
import cv2

# 图像二值化
def binaryzation(image,threshold):
    height = image.shape[0]
    width = image.shape[1]
    newImg = np.array(image)
    for i in range(height):
        for j in range(width):
            if(int(image[i,j]) < threshold):
                newImg[i,j] = 0
            else:
                newImg[i,j] = 255

    return newImg

# 灰度图取反
def bitwise(image):
    height = image.shape[0]
    width = image.shape[1]
    newImg = np.array(image)
    for i in range(height):
        for j in range(width):
            newImg[i,j] = 255 - image[i,j]

    return newImg
  
def sketch(img, threshold):
    '''
    素描
    param img: Image实例
    param threshold: 介于0到100
    '''
    if threshold < 0: threshold = 0
    if threshold > 100: threshold = 100
      
    width, height = img.size
    img = img.convert('L') # convert to grayscale mode
    pix = img.load() # get pixel matrix
  
    for w in xrange(width):
        for h in xrange(height):
            if w == width-1 or h == height-1:
                continue
              
            src = pix[w, h]
            dst = pix[w+1, h+1]
  
            diff = abs(src - dst)
  
            if diff >= threshold:
                pix[w, h] = 0
            else:
                pix[w, h] = 255
  
    return img

# 椒盐噪声
def SaltAndPepper(image,rate):
    w = image.shape[1]
    h = image.shape[0]
    noiseCount = int(rate * w * h)
    newImg = np.array(image)
    for k in range(0, noiseCount):
        i = int(np.random.uniform(0,w))
        j = int(np.random.uniform(0,h))
        if int(np.random.uniform(0,2)) == 0:
            newImg[j,i] = 0
        else:
            newImg[j,i] = 255

    return newImg

# 滤波
def imFilter(image,size,fType):
    h = image.shape[0]
    w = image.shape[1]
    halfSize = int(size/2)
    newImg = np.array(image)

    for y in range(halfSize,h-halfSize):
        for x in range(halfSize,w-halfSize):
            if fType == 'med':
                newImg[y,x]=np.median(image[y-halfSize:y+halfSize+1,x-halfSize:x+halfSize+1])
            elif fType == 'mean':
                newImg[y,x]=np.mean(image[y-halfSize:y+halfSize+1,x-halfSize:x+halfSize+1])

    return newImg


# 定义参数
noiseRate = 0.05 #噪声点比例
filterSize = 3 #滤波器尺寸

# 读图原图
srcImage = cv2.imread("lena.jpg",0)

# 添加椒盐噪声
srcImage = SaltAndPepper(srcImage,noiseRate)

# 中值滤波去噪
# dstImage = cv2.medianBlur(srcImage,filterSize) # cv2中值滤波
dstImage = imFilter(srcImage,filterSize,'med') # 自定义滤波器

# 显示结果
cv2.imshow('srcImage',srcImage)
cv2.imshow('dstImage',dstImage)
cv2.waitKey()
cv2.destroyAllWindows()

# path = 'car.jpg'
# im = cv2.imread('lena.jpg',0)
# cv2.imshow('a',im)
# im = binaryzation(im, 180)
# cv2.imshow('b',im)
# cv2.waitKey()
# img = Image.open(path)
# img = sketch(img, 20)
# img.show()
# print img


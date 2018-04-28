# coding: utf-8
from PIL import Image, ImageFilter
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

im = Image.open('lena.jpg')
# 高斯模糊
im2 = im.filter(ImageFilter.GaussianBlur)
# 边缘增强
im3 = im.filter(ImageFilter.EDGE_ENHANCE)
# 找到边缘
im4 = im.filter(ImageFilter.FIND_EDGES)
# 浮雕
im5 = im.filter(ImageFilter.EMBOSS)
# 轮廓
im6 = im.filter(ImageFilter.CONTOUR)

font = FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc", size=14)
plt.figure(u"三维模型分类",figsize=(10, 10))#创建图表1    
plt.subplot(3,3,1)
plt.title(u'原图'+ '',fontproperties=font)
plt.axis('off')
plt.imshow(im)
plt.subplot(3,3,2)
plt.title(u'高斯模糊'+ '',fontproperties=font)
plt.axis('off')
plt.imshow(im2)
plt.subplot(3,3,3)
plt.title(u'边缘增强'+ '',fontproperties=font)
plt.axis('off')
plt.imshow(im3)
plt.subplot(3,3,4)
plt.title(u'找到边缘'+ '',fontproperties=font)
plt.axis('off')
plt.imshow(im4)
plt.subplot(3,3,5)
plt.title(u'浮雕'+ '',fontproperties=font)
plt.axis('off')
plt.imshow(im5)
plt.subplot(3,3,6)
plt.title(u'轮廓'+ '',fontproperties=font)
plt.axis('off')
plt.imshow(im6)
plt.show()
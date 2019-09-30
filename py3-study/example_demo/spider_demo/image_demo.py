#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Date: 2019/7/12

from PIL import Image
import cv2
import random
import numpy as np


nums = range(255)
# nums = [0]
# # print(random.sample(nums, 3))
#
image_nums = []
for _ in range(100*100*3):
    image_nums.append(random.choice(nums))
# for i in range(256):
#     li = []
#     for z in range(400):
#         li.append([i, i, i])
#     image_nums.append(li)

#
# print(image_nums)
image_nums = np.array(image_nums, dtype=np.uint8)
image_nums = image_nums.reshape(100, 100, 3)
# print(image_nums)
# print(image_nums.shape)


im = Image.open('cloud_demo.jpg')
# im_new = im.convert('L')
# im_new.show()
# im_new.save('python_book_new.jpg')

# nums_ = np.array(im)
# print(nums_.dtype)
# for n in nums_:
#     for i in n:
#         if i[0] != 0:
#             print(i[0], end='')
#         else:
#             print(' ', end='')
#     print()
# nums += 55
# print(nums)
# for i in nums:
#     #print(i, 1)
#     pass
#     for j in i:
#         # print(j)
#         for x in range(3):
#             j[x] = 255 - j[x]
#             pass
#         pass
# print(nums)
#
# nums = nums[:5]

# nums = np.arange(255)
# nums = nums.reshape(1, 255)
# nums = [0]*1200
# print(nums)
# nums = np.array(nums, dtype=np.uint8).reshape(400, 3)
# print(nums, len(nums), nums == nums_[0])
#cv2.imshow('image', image_nums)

# import cv2   #导入模块，opencv的python模块叫cv2
# imgobj = cv2.imread('python_book.jpg') #读取图像
# cv2.namedWindow("image") #创建窗口并显示的是图像类型
# cv2.imshow("image",imgobj)


# img = np.zeros([400,400,3],np.uint8)    #创建一个三维数组高400，宽400，信号通道3个，初始都为0，每通道占8位个
# img[:,:,0] = np.ones([400,400])*255
# cv2.imshow("new image",img)
# cv2.imwrite('blue.jpg', img)

#cv2.waitKey(0)        #等待事件触发，参数0表示永久等待
#cv2.destroyAllWindows()   #释放窗口
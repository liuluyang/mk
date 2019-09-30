import pytesseract
from PIL import Image


im = Image.open('images/wenzi_02.jpg')
# im_new = im.convert('L')
# im_new.show()
# chi_sim中文识别
code = pytesseract.image_to_string(image=im, lang='chi_sim')
print(code)

# im_new = im.convert('L')
#
# threshold = 80
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# image = im_new.point(table, '1')
# image.show()
#im_new.save('images/code_02_c.jpg')
# im.show()

# text = pytesseract.image_to_string(im)
# print(text)


from PIL import Image
import pytesseract
import re  # 导入re
import os
import pytesseract

Image = Image.open(r'heartbeat.png')  # 打开图片
text = pytesseract.image_to_string(Image)  # 使用简体中文解析图片
file = open('heartbeat.png', mode='w')
file.writelines(text)
print(text)
file.close()
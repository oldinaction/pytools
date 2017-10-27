# -*- coding: utf-8 -*-
from PIL import Image
# pytesser(依赖PIL和Tesseract-OCR)安装比较麻烦, 使用pytesseract代替
import pytesseract

'''
简单识别：成功率低
'''
def getCodeSimple(name):
    # Open image object using PIL
    image = Image.open(name)
    # Run pytesser.exe on image
    return pytesseract.image_to_string(image)

'''
识别数字图片：彩色转灰度，灰度转二值，二值图像识别
'''
def getCodeNumExt(name, path=""):
    '''
    :param name: 文件名称
    :param path: 文件路径
    :return: 
    '''

    # 二值化
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    # 由于都是数字，对于识别成字母的采用该表进行修正
    rep = {'O': '0',
           'I': '1', 'L': '1',
           'Z': '2',
           'S': '8'
           }

    # 打开图片
    im = Image.open(path + name)
    # 转化到灰度图
    imgry = im.convert('L')
    # 保存图像
    imgry.save(path + '_g' + name)
    # 二值化，采用阈值分割法，threshold为分割点
    out = imgry.point(table, '1')
    out.save(path + '_b' + name)
    # 识别
    text = pytesseract.image_to_string(out)
    # 识别汉字(需要安装简体中文字库文件)
    # text = pytesseract.image_to_string(out, lang="chi_sim")
    # 识别对吗
    text = text.strip()
    text = text.upper()
    for r in rep:
        text = text.replace(r, rep[r])
    return text

if __name__ == '__main__':
    # 识别数字
    print "simple: " + getCodeSimple('img/num.jpg') # 失败
    print "ext: " + getCodeNumExt('num.jpg', "img/")
    print "simple: " + getCodeSimple('img/_gnum.jpg')

    # 识别字母
    print "letter: " + getCodeNumExt('letter.jpg', "img/") # 失败

    # 识别汉字
    # print "zh: " + getCodeNumExt('zh.png', "img/") # 不准确
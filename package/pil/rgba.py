# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw

'''
获取图片每个像素点的rgba值：jpg格式只有rgb(225, 225, 225), png格式有rgba(0, 0, 0, 225), bmp格式只有一位如225(0黑色, 225白色)
'''
def rgba(name):
    # 加载png图片
    img = Image.open(name)
    img = img.convert("L") # 将图片转成灰度，则此时getpixel只能获取到一位整形值

    # 输出图像的基本信息
    print img.format, img.size, img.mode

    # 获取图像的
    width = img.size[0]
    height = img.size[1]

    # 输出图片的像素值
    count = 0
    for i in range(0, width):
        for j in range(0, height):
            # 获取某个坐标的颜色：从图片的左上顶点(0, 0)向右下循环到右下底点(width-1, height-1)
            color = img.getpixel((i, j))
            count += 1
            print str(i) + "-" + str(j) + "：" + color.__str__()
    print count

'''
修改图片像素点RGB
'''
def draw_rgba(imageName, targetName):
    img = Image.open(imageName)
    draw = ImageDraw.Draw(img)

    width = img.size[0]
    height = img.size[1]

    # 黑色
    color = (0, 0, 0)
    for i in range(0, width):
        for j in range(0, height):
            if i < 4 and j < 4:
                draw.point((i, j), color)

    img.save(targetName)

if __name__ == "__main__":
    # rgba("img/bmp.bmp")
    # rgba("img/rgb.jpg")
    rgba("img/rgba.png")
    draw_rgba("img/rgb.jpg", "img/_rgb.jpg")
import os
from PIL import Image
#支持的图片格式
support=('.png','.jpg')
#你想要的目录
mypath=r'/home/huang/图片/test'
images = [x for x in os.listdir(mypath) if os.path.splitext(x)[1] in support]
for x in images:
    pic=os.path.join(mypath,x)
    im=Image.open(pic)
    #如果不能缩放，那不会缩放
    im.thumbnail((1136,640))
    im.save(pic)





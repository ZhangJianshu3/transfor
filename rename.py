import os
path = '/home/zhangjianshu/transfor/pic/2'
for filename in os.listdir(path):
    newname = "%06d"%int(filename[:-4])
    newname = newname+'.jpg'
    print newname
    os.rename(os.path.join(path, filename),os.path.join(path,newname))
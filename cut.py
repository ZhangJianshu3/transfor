import os
import cv2
import numpy



inpath = '/home/zjs/cut/result'
outpath = '/home/zjs/cut/cutresult'
for i in os.listdir(inpath):
    impath = inpath+'/'+i
    im = cv2.imread(impath)
    pic = im[161:823,67:1192]
    cv2.imshow('im',pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    newpath = outpath+'/'+i
    cv2.imwrite(newpath,pic)
import os
import cv2


def main(inpath, outpath):
    num = 1
    filenum = 0
    for videoname in os.listdir(inpath):
        videopath = inpath+'/'+videoname
        print videopath
        outputfolder = outpath+'/'+videoname+'.img'
        print outputfolder
        if os.path.exists(outputfolder) == False:
            filenum = filenum+1
            os.mkdir(outputfolder)
        vcap = cv2.VideoCapture(videopath)
        while True:
            ret,frame = vcap.read()
            #print ret
            if ret:
                num = num+1
                if num%6 == 0:
                    print num
                    picname = str(num/6)+'.jpg'
                    picpath = outputfolder+'/'+picname
                    print picpath
                    cv2.imwrite(picpath,frame)
            else:
                break


if __name__ == '__main__':
    inpath = '/home/wlw/transfor/video'
    outpath = '/home/wlw/transfor/pic'
    main(inpath, outpath)
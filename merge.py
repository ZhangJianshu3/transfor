import os
import cv2
import math



def getCen(t):
    cx = (t[0]+t[2])/2
    cy = t[3]
    return cx,cy


def getdist(start, end):
    dx = start[0]-end[0]
    dy = start[1]-end[1]
    dist = math.sqrt(dx*dx+dy*dy)
    return dist


def judge(f, s):
    #print f
    #print s
    track = []
    for i in f:
        dist = 1000000
        for j in s:
            p1 = i
            p2 = j
            temp = getdist(p1, p2)
            #print p1,p2
            #print temp
            if dist > temp:
                dist = temp
                start = p1
                end = p2
            else:
                continue
        #print 'start,end',start,end
        track.append([start,end])
    print 'track1',track
    for i in track:
        start = i[0]
        end = i[1]
        dist = getdist(start, end)
        if dist > 500:
            i[0] = [0, 0]
            i[1] = [0, 0]
    return track


def gettra(path, num, arr):
    fpicname = num+'.jpg'
    fpicpath = path+fpicname
    spicname = "%06d"%(int(num)+1)+'.jpg'
    spicpath = path+spicname
    fcarlist = []
    scarlist = []
    for item in arr:
        if item[1] == fpicname:
            fcarlist.append(item)
        if item[1] == spicname:
            scarlist.append(item)
    print 'fcarlist',fcarlist
    print 'scarlist',scarlist
    f = []
    s = []
    for car in fcarlist:
        #print car
        t = [float(car[3]),float(car[4]),float(car[5]),float(car[6])]
        fcx, fcy = getCen(t)
        f.append([fcx,fcy])
    for car in scarlist:
        #print car
        t = [float(car[3]),float(car[4]),float(car[5]),float(car[6])]
        scx, scy = getCen(t)
        s.append([scx,scy])
    track = judge(f,s)
    print 'track2',track
    return track


def gettraline(traline, track):
    #print 't',track
    #print 'tl',traline
    if traline == []:
        for i in track:
            if i != [[0, 0], [0, 0]]:
                traline.append(i)
    else:
        for inum in range(len(track)):
            for lnum in range(len(traline)):
                #print track
                if track == []:
                        break
                dist = getdist(track[0][0], traline[lnum][-1])
                if dist < 1 and track[0] != [[0, 0], [0, 0]]:
                    traline[lnum].append(track[0][1])
                    del track[0]
        for i in track:
            traline.append(i)
    return traline


def drawline(imresult, track):
    im = imresult
    for t in track:
        start = (int(t[0][0]),int(t[0][1]))
        end = (int(t[1][0]),int(t[1][1]))
        print 'start',start
        print 'end',end
        if start != (0,0) or end != (0,0):
            im = cv2.line(im, start, end, (0, 0, 255), 5)
    cv2.imshow('im', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return im


def getlines(lines, traline):
    for line in traline:
        if line != [[0, 0], [0, 0]]:
            lines.append(line)
    return lines


def writetxt(txtpath, lines):
    for line in lines:
        print line
        if os.path.exists(txtpath):
            f = open(txtpath, 'a')
            f.write(str(line)+'\n')
            f.close()
        else:
            f = open(txtpath, 'w')
            f.write(str(line)+'\n')
            f.close


def trans(lines):
    w1 = 0.247318942688
    w2 = 0.147631138991
    b1 = -50.5199595296
    w3 = -0.0512959401626
    w4 = 0.597593136776
    b2 = -51.5823786355
    for i in lines:
        for j in i:
            j[0] = w1*j[0]+w2*j[1]+b1
            j[1] = w3*j[0]+w4*j[1]+b2
    return lines


def main(path):
    txtpath = path+'data.txt'
    fp = open(txtpath)
    arr = []
    for lines in fp.readlines():
        lines = lines.replace("\n","").split(" ")
        lines = [str(i) for i in lines]
        lines = list(lines)
        arr.append(lines)
    fp.close()
    arr = sorted(arr, key=lambda arr : arr[1][:-4])
    num = arr[0][1][:6]
    resnum = -4
    for i in os.listdir(path):
        resnum += 1
    print resnum
    traline = []
    print path+num+'.jpg'
    imresult = cv2.imread(path+num+'.jpg')
    while True:
        if resnum > 0:
            #print num
            track = gettra(path, num, arr)
            imname = num+'.jpg'
            impath = path+imname
            imresult = drawline(imresult, track)
            traline = gettraline(traline, track)
            num = "%06d"%(int(num)+1)
            resnum = resnum-1
            print resnum
        else:
            break
    resultpath = path+'/result/result_all.jpg'
    #cv2.imwrite(resultpath, imresult)
    lines = []
    lines = getlines(lines, traline)
    #print traline
    print lines
    lines = trans(lines)
    print lines
    txtpath = path+'/result/result.txt'
    writetxt(txtpath, lines)



if __name__ == '__main__':
    path = '/home/zhangjianshu/transfor/pic/2/'
    main(path)
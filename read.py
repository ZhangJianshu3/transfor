

def main(path):
    txtpath = path
    fp = open(txtpath)
    arr = []
    for lines in fp.readlines():
        lines = lines.replace("\n","").split(" ")
        lines = [int(i) for i in lines]
        #lines[0] = int(lines[0])
        print lines
        arr.append(lines)
    fp.close()
    print arr


if __name__ == '__main__':
    path = '/home/wlw/transfor/pic_coordinator'
    main(path)

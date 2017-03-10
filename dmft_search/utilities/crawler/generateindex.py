import sys
import getfilesystem
sys.path.append("..")
from keystore import keystorefile


def generateindex():
    store = keystorefile.create()
    pathlist = getfilesystem.getall()
    index = {}
    for item in pathlist:
        for pattern in store:
            if pattern in item:
                if index in pattern:
                    index[pattern].append(item)
                else:
                    temp = []
                    temp.append(item)
                    index[pattern] = temp
    return index

print generateindex()

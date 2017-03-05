import os


def getall():
    pathlist = []
    for root, dirs, files in os.walk("/home/raghav/Desktop/test", topdown=True):
        for name in files:
            pathlist.append(os.path.join(root, name))
        for name in dirs:
            pathlist.append(os.path.join(root, name))
    return pathlist
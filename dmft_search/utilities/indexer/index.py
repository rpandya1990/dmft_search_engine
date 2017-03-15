from tqdm import *
from utilities.keystore import keystorefile
from utilities.crawler import fileSystemDumps


def generate(dump):
    """Generate an inverted index.

    Args:
        location: path of the filesystem
    Returns:
        Inverted Index(keyword->[path,..])
    """
    keywords, inverted_keywords = keystorefile.create()
    filesystem = fileSystemDumps.load(dump)
    index = {}
    print "Building indexes :"
    for item in tqdm(filesystem.keys()[1:1000]):
        for keyword in keywords.keys():
            if keyword in item.split("/")[-1]:
                if keyword in index:
                    index[keyword].append(item)
                else:
                    temp = []
                    temp.append(item)
                    index[keyword] = temp
    return index, filesystem

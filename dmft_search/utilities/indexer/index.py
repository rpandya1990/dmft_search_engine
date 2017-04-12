from tqdm import *
import re
from utilities.keystore import keystorefile
from utilities.crawler import fileSystemDumps


def findpattern(pattern, string):
    """Check for pattern in string.

    Args:
        pattern: pattern to look for
        string: string

    Returns:
        List containing index at which pattern exists
    """
    filtered_string = ''.join([i for i in string if not i.isdigit()])
    pattern_in_string = [x.start() for x in re.finditer(pattern.lower(), filtered_string.lower())]
    return pattern_in_string


def generate(dump):
    """Generate an inverted index.

    Inverted index dictionary is formed with every bigram to paths pair

    Example:
        index = {
            'AgFe': {'path1': {'root_path': [1, 2], file1: [2, 8]....}, 'path2':...)}
        }
    'AgFe' keyword is present in path1 and path2, in path1, keyword occurs at indices [1, 2]
    in folder name and at indices [2, 8] in file1 name

    Args:
        location: path of the filesystem dump

    Returns:
        Inverted Index(keyword: {'path1': {'root_path': [], file1: []....}, 'path2':...)
    """

    keywords, inverted_keywords = keystorefile.create()
    crawlobj = fileSystemDumps.Crawler()
    filesystem = crawlobj.load(dump)
    index = {}
    print "Building indexes :"
    for item in tqdm(filesystem.keys()[1:1000]):
        for keyword in keywords.keys():
            frequency = 0
            inner_temp = {}
            pattern_in_root = findpattern(keyword, item.split("/")[-1])
            if len(pattern_in_root) > 0:
                inner_temp[item.split("/")[-1]] = pattern_in_root
                frequency += len(pattern_in_root)

            for file in filesystem[item]['files']:
                pattern_in_file = findpattern(keyword, file.split(".")[0])
                if len(pattern_in_file) > 0:
                    inner_temp[file] = pattern_in_file
                    frequency += len(pattern_in_file)

            if frequency > 0:
                if keyword not in index:
                    index[keyword] = {}
                index[keyword][item] = inner_temp

    # Printing index to file for analysis
    with open('index.txt', 'w') as f1:
        for k, v in index.items():
            print>>f1, (k, '-->', v)
            print>>f1
    return index, filesystem

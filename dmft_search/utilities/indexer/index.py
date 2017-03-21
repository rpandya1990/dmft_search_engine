from tqdm import *
from utilities.keystore import keystorefile
from utilities.crawler import fileSystemDumps


def findpattern(pattern, string_list):
    """Check for bigram of elements in list of strings.

    Args:
        pattern: pattern to look for
        string_list: list of strings
    Returns:
        Tuple containing if pattern is present and pattern frequency
    """
    occurence = 0
    for string in string_list:
        filtered_string = ''.join([i for i in string if not i.isdigit()])
        # if pattern in filtered_string:
        if pattern.lower() in filtered_string.lower():
            occurence += 1

    if occurence >= 4:
        return True, occurence
    else:
        return False, occurence


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
    for item in tqdm(filesystem.keys()[1:100]):
        for keyword in keywords.keys():
            current_key = item.split("/")[-1]
            current_key_files = filesystem[item]['files']
            string_list = []
            string_list.append(current_key)
            string_list.extend(current_key_files)
            ispresent, tf = findpattern(keyword, string_list)
            if ispresent:
                if keyword in index:
                    index[keyword].append((item, tf))
                else:
                    temp = []
                    temp.append((item, tf))
                    index[keyword] = temp
    # Printing index to file for analysis
    with open('index.txt', 'w') as f1:
        for k, v in index.items():
            print>>f1, (k, '-->', v)
    return index, filesystem

import json
from tqdm import *
from periodictable import *


def create():
    """Generate all keywords.

    Generate keywords which are combinations of 2 elements(symbols)
    and their mapping to names
    Returns:
        Keyword(combinations of 2 elements) and
        inverted keyword(mapping of keyword to element names)
    """
    keyword = {}
    for element in elements:
        for other_element in elements:
            if other_element == element:
                continue
            elements_in_compound = []
            elements_in_compound.append(element.name)
            elements_in_compound.append(other_element.name)
            temp = element.symbol + other_element.symbol
            keyword[temp] = elements_in_compound

    inverted_keyword = {}
    for key, values in keyword.iteritems():
        for item in values:
            if item in inverted_keyword:
                inverted_keyword[item].append(key)
            else:
                inverted_keyword[item] = []
                inverted_keyword[item].append(key)

    return keyword, inverted_keyword


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
        # if pattern.lower() in filtered_string.lower():
        if pattern in filtered_string:
            occurence += 1

    if occurence >= 2:
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
    keywords, inverted_keywords = create()
    # filesystem = fileSystemDumps.load(dump)
    filesystem = {'/home/xiaoyu/tmp/CaCdGe/SOC/CaCdGe': {'files': ['CaCdGe.in0_st', 'runjob.scr',
        'CaCdGe.scf0', 'CaCdGe.inc_st', 'abcdef', '123cdgg', 'Ca23cf']}}
    index = {}
    print "Building indexes :"
    # for item in tqdm(filesystem.keys()[1:1000]):
    for item in tqdm(filesystem.keys()):
        keyword = 'CdGe'
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
    with open('index.json', 'w') as f:
        json.dump(index, f)
    return index, filesystem

generate("filesystem.pickle")

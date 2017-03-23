import os
import time
import pickle


def create(location):
    """Create a filesystem dump(dictionary) by crawling.

    Every entry in the dictionary is an entry as below
    Every folder is tokenized and stored as
    'Path to folder': {
        'files': [Names of the files],
        'folders': [Names of the folders],
        'last_modified': 'Weekday Month Day hh:mm:ss Year'
    }

    Example:
    '/home/Public/Soft: {
        'files': ['a.html', 'b.txt'],
        'folders': ['var', 'www'],
        'last_modified': 'Fri May 22 17:29:42 2015'
    },

    Args:
        location: path of the filesystem
    """
    for root, dirs, files in os.walk(location, topdown=True):
        folders = {}
        temp_dict = {}
        temp_dict["last_modified"] = time.ctime(os.path.getmtime(root))
        temp_dict["files"] = files
        temp_dict["folders"] = dirs
        folders[root] = temp_dict
        for name in files:
            os.path.join(root, name)
        for name in dirs:
            os.path.join(root, name)
    with open(location, 'wb') as handle:
        pickle.dump(folders, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load(name):
    """Load a filesystem dump from the given loation.

    Args:
        location: Path of the dump already created
    """
    name = "dmft_search/utilities/crawler/dumps/" + name
    with open(name, 'rb') as handle:
        b = pickle.load(handle)
    return b


def test_load(name):
    """Load a filesystem dump from the given loation.

    Args:
        location: Path of the dump already created
    """
    with open(name, 'rb') as handle:
        b = pickle.load(handle)
    return b

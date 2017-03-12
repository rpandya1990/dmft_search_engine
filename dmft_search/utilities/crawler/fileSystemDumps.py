import os
import time
import pickle


def create(location):
    """Create a filesystem dump by crawling.

    Args:
        location: path of the filesystem
    """
    for root, dirs, files in os.walk(location, topdown=True):
        folders = {}
        temp_dict = {}
        temp_dict["Last modified"] = time.ctime(os.path.getmtime(root))
        temp_dict["Files"] = files
        temp_dict["Folders"] = dirs
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
    print os.getcwd()
    name = "dmft_search/utilities/crawler/dumps/" + name
    with open(name, 'rb') as handle:
        b = pickle.load(handle)
    return b

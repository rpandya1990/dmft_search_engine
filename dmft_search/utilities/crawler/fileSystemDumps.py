import os
import numpy as np
import time
import pickle
import re
from periodictable import *
from utilities.keystore import keystorefile


class Crawler(object):
    """Crawler class which intelligently crawls and includes probable candidates."""

    def __init__(self):
        keywords, inverted_keywords = keystorefile.create()
        self.keywords = map(lambda x: x.lower(), keywords.keys())

    def filter(self, name):
        """Check whether a given string has valid token.

        A string is tokenized and checked if there is a token which only contains consecutive bigrams
        Args:
            name: a string
        """
        tokens = re.split(r"[^a-zA-Z0-9\s]", name)
        for token in tokens:
            if len(token) == 0:
                continue
            filtered_token = re.sub("\d+", "", token).lower()
            bitmap = np.zeros((len(filtered_token)), dtype=np.int)

            # Form element candidates with the token and mark the bitmap if it's an element
            for x in range(1, 6):
                for i in xrange(len(filtered_token) - x):
                    if filtered_token[i: i + x + 1] in self.keywords:
                        bitmap[i: i + x + 1] = 1
            # If bitmap contains only non-zero accept the token
            if np.count_nonzero(bitmap) == len(bitmap):
                return True
        return False

    def create(self, location):
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
        folders = {}
        for root, dirs, files in os.walk(location, topdown=True):
            count_valid_token = 0
            temp_dict = {}
            temp_dict["last_modified"] = time.ctime(os.path.getmtime(root))
            print "Crawling directory: " + root
            if(self.filter(root.split('/')[-1])):
                count_valid_token += 1

            temp_files = []
            for name in files:
                if(self.filter(name)):
                    count_valid_token += 1
                    temp_files.append(name)
                os.path.join(root, name)
            temp_dict["files"] = temp_files

            for name in dirs:
                if(self.filter(name)):
                    count_valid_token += 1
                os.path.join(root, name)

            if(count_valid_token > 0):
                folders[root] = temp_dict

        with open("dumps/filesystem.pickle", 'wb') as handle:
            pickle.dump(folders, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, name):
        """Load a filesystem dump from the given loation.

        Args:
            location: Path of the dump already created
        """
        name = "dmft_search/utilities/crawler/dumps/" + name
        with open(name, 'rb') as handle:
            b = pickle.load(handle)
        return b

# obj = Crawler()
# obj.create('/home/xiaoyu')
# obj.load('filesystem.pickle')

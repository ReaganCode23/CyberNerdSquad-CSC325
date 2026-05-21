'''
Source Code:
https://docs.python.org/3/library/hashlib.html
https://www.geeksforgeeks.org/python/python-how-to-get-the-last-element-of-list/
'''

import hashlib

class MerkleTree:
    def __init__(self, data_list):
        self.data_list = data_list
        self.hashed_data = self._first_hash(self.data_list)
        self.root = self._build_tree(self.hashed_data)

    def _hash(self, data):
        """
        this is for hashing the data
        we chose sha256 because it is the most common type of hashing
        you can choose other types if you want
        """
        data = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return data

    def _first_hash(self, nodes):

        nodes_copy = []

        for i in range(len(nodes)):
            nodes_copy.append(nodes[i])

        #debug
        print(nodes)
        print(nodes_copy)

        if len(nodes) == 1:
            return self._hash(str(nodes[0]))

        if len(nodes) % 2 != 0:
            nodes_copy.append(nodes[-1])

        #debug
        print(nodes)
        print(nodes_copy)

        #create a new list for the hashed leaf nodes
        hashed_data = []

        for i in range(len(nodes_copy)):
            hashed_data.append(self._hash(str(nodes_copy[i])))

        #debug
        print(hashed_data)

        self.hashed_data = hashed_data
        return hashed_data

    def _build_tree(self, hashed_data):

        if len(hashed_data) == 1:
            self.root = hashed_data[0]
            return hashed_data[0]

        #create new list for the next level of the tree
        next_level = []

        #iterate through the leaves and hash every 2 nodes together
        for i in range(0, len(hashed_data), 2):
            combined_hashed_data = self._hash(hashed_data[i] + hashed_data[i+1])
            next_level.append(combined_hashed_data)

        #debug
        print(next_level)

        return self._build_tree(next_level)

    def print_tree(self):
        print(self.root)

    def insert(self, new_data):
        self.data_list.append(new_data)
        self._first_hash(self.data_list)
        self.root = self._build_tree(self.hashed_data)

    '''def delete(self, data):

    def search(self, data):

    def get(self, data):'''

if __name__ == '__main__':
    L = [0, 1]
    m = MerkleTree(L)
    m.insert(2)
    m.insert(3)
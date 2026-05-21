'''
Source Code:
https://docs.python.org/3/library/hashlib.html
https://www.geeksforgeeks.org/python/python-how-to-get-the-last-element-of-list/
'''

import hashlib

class MerkleTree:
    def __init__(self, data_list):
        self.data_list = data_list
        self.root = self._build_tree(self.data_list)

    def _hash(self, data):
        """
        this is for hashing the data
        we chose sha256 because it is the most common type of hashing
        you can choose other types if you want
        """
        data = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return data

    def _build_tree(self, nodes):

        #base case: return the root node once the tree is built
        if len(nodes) == 1:
            return nodes[0]

        #this ensures that there is an even number of elements
        if len(nodes) % 2 != 0:
            nodes.append(nodes[-1])

        #create a new list for the next level of the tree
        next_level = []

        #iterate through the leaves and hash every 2 nodes together
        for i in range(0, len(nodes), 2):
            hashed_data = self._hash(nodes[i] + nodes[i+1])
            next_level.append(hashed_data)

        return self._build_tree(next_level)

    def print_tree(self):
        print(self._build_tree(self.data_list))

    def insert(self, new_data):
        new_data = self._hash(new_data)
        self.data_list.append(new_data)
        self._build_tree(self.data_list)

    '''def delete(self, data):

    def search(self, data):

    def get(self, data):'''

if __name__ == '__main__':
    L = [0, 1, 2, 3, 4]
    m = MerkleTree(L)

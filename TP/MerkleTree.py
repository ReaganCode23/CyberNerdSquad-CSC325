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
        self.tree = self._build_tree(self.hashed_data)
        self.root = self.tree[0]

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

        if len(nodes) == 1:
            return self._hash(str(nodes[0]))

        if len(nodes) % 2 != 0:
            nodes_copy.append(nodes[-1])

        #create a new list for the hashed leaf nodes
        hashed_data = []

        for i in range(len(nodes_copy)):
            hashed_data.append(self._hash(str(nodes_copy[i])))

        self.hashed_data = hashed_data
        return hashed_data

    def _build_tree(self, hashed_data):

        #a place to put the whole tree
        self.tree = []

        current_level = []

        for i in range(len(hashed_data)):
            current_level.append(hashed_data[i])

        self.tree.append(current_level)

        while len(current_level) > 1:

            if len(current_level) % 2 != 0:
                current_level.append(current_level[-1])

            #create new list for the next level of the tree
            next_level = []

            #iterate through the leaves and hash every 2 nodes together
            for i in range(0, len(current_level), 2):
                combined_hashed_data = self._hash(current_level[i] + current_level[i+1])
                next_level.append(combined_hashed_data)

            self.tree.append(next_level)
            current_level = next_level

        self.root = current_level[0]
        return self.tree

    def _update_tree(self):
        self._first_hash(self.data_list)
        self.root = self._build_tree(self.hashed_data)

    def get_root(self):
        print(self.root)
        return self.root

    def print_tree(self):
        print(self.data_list)
        for i in range(len(self.tree)):
            print(self.tree[i])

    def get_proof(self, data):
        data_hash = self._hash(str(data))

        if data_hash not in self.tree[0]:
            print("no proof")
            return None

        proof = []
        index = self.tree[0].index(data_hash)

        for level in self.tree[:-1]:
            level_copy = []

            for i in range(len(level)):
                level_copy.append(level[i])

            if len(level_copy) % 2 != 0:
                level_copy.append(level_copy[-1])

            if index % 2 == 0:
                sibling_index = index + 1
                direction = "right"
            else:
                sibling_index = index - 1
                direction = "left"

            proof.append((direction, level_copy[sibling_index]))

            index = index // 2

        print("proof:", proof)
        return proof

    def insert(self, new_data):
        self.data_list.append(new_data)
        self._update_tree()

    def delete(self, data):
        self.data_list.remove(data)
        self._update_tree()

if __name__ == '__main__':
    L = [0, 1, 2]
    m = MerkleTree(L)
    m.print_tree()
    m.get_root()
    m.get_proof(1)
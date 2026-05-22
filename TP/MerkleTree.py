'''
Source Code:
https://docs.python.org/3/library/hashlib.html
https://www.geeksforgeeks.org/python/python-how-to-get-the-last-element-of-list/
https://dev.to/craig_solomon/walking-up-a-merkle-tree-sha-256-proof-validation-in-python-2fg9
https://stackoverflow.com/questions/15535205/what-does-1-mean-do-in-python
https://alexandercodes.hashnode.dev/verifying-merkle-proofs-on-algorand
'''

import hashlib

class MerkleTree:
    def __init__(self, leaf_list):
        self.leaf_list = leaf_list
        self.hashed_data = self._first_hash(self.leaf_list)
        self.tree = self._build_tree(self.hashed_data)

    def _hash(self, data):
        """
        this is for hashing the data
        we chose sha256 because it is the most common type of hashing
        you can choose other types if you want
        :param data: something to hash
        :return: the hashed data
        """

        data = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return data

    def _first_hash(self, nodes):
        """
        this is for the first hashing needed to start the merkle tree
        :param nodes: the original data; the leaves of the tree
        :return: the hashed leaves of the tree
        """

        #make a copy of the nodes list in case we need to copy an element
        nodes_copy = []
        for i in range(len(nodes)):
            nodes_copy.append(nodes[i])

        #if we only have one node, we are at the root, so return its hash value
        if len(nodes) == 1:
            return self._hash(str(nodes[0]))

        #merkle trees have to have an even number of elements on all levels, so if it's not even, copy the last element
        if len(nodes) % 2 != 0:
            nodes_copy.append(nodes[-1])

        #create a new list for the hashed nodes
        hashed_data = []
        for i in range(len(nodes_copy)):
            hashed_data.append(self._hash(str(nodes_copy[i])))

        return hashed_data

    def _build_tree(self, hashed_nodes):
        """
        build the merkle tree
        :param hashed_nodes: the hashed leaf list
        :return: the tree as a list of lists
        """

        #a place to put the whole tree
        tree = []

        #a place-holder for each level of the tree
        current_level = []
        for i in range(len(hashed_nodes)):
            current_level.append(hashed_nodes[i])

        #put each level in the tree list
        tree.append(current_level)

        #continue until we get to the root
        while len(current_level) > 1:

            #if the current level has an odd number of elements, duplicate the last element
            if len(current_level) % 2 != 0:
                current_level.append(current_level[-1])

            #create new place-holder for the next level of the tree
            next_level = []

            #iterate through the current level and hash every 2 nodes together
            for i in range(0, len(current_level), 2):
                combined_hashed_data = self._hash(current_level[i] + current_level[i+1])
                next_level.append(combined_hashed_data)

            tree.append(next_level)
            current_level = next_level

        self.root = current_level[0]
        return tree

    def get_root(self):
        """
        return the root of the merkle tree
        :return: the hash value of the root of the merkle tree
        """
        return self.root

    def print_tree(self):
        """
        print the merkle tree as a list of lists
        """
        for i in range(len(self.tree)):
            print(self.tree[i])

    def get_proof(self, data):
        """
        check if the data is in the merkle tree
        :param data: the data we are looking for
        :return: None if data not present; list of directions and sibling hashes if data is present
        """

        #hash the data we are looking for
        data_hash = self._hash(str(data))

        #if the data is not present in the leaf nodes, return None
        if data_hash not in self.tree[0]:
            return None

        #create a list for the proof
        gproof = []

        #note the index of the leaf node that matches the data we are looking for
        index = self.tree[0].index(data_hash)

        #iterate through the levels of the tree except for the root node
        for level in self.tree[:-1]:
            #make a copy of each level
            level_copy = []

            #iterate through each node in the level
            for i in range(len(level)):
                level_copy.append(level[i])

            #if the index value is even, it means the data has a sibling to the right
            #note the index of the sibling
            if index % 2 == 0:
                sibling_index = index + 1
                direction = "right"

            #if the index value is odd, it means the data has a sibling to the left
            #note the index of the sibling
            else:
                sibling_index = index - 1
                direction = "left"

            #add the direction and hash value of the sibling to the proof list and update the index before moving to the next level
            gproof.append((direction, level_copy[sibling_index]))
            index = index // 2

        return gproof

    def verify_proof(self, data, vproof, root):
        """
        check if the proof is valid based on the hash value of the root of the merkle tree
        :param data: the data we are looking for
        :param vproof: the list of directions and sibling hashes we found using get_proof
        :param root: the root of the merkle tree
        :return: True if the proof is correct; False if the proof is not correct
        """

        #if the proof we got from get_proof is none, the proof cannot be valid
        if vproof is None:
            return False

        #hash the data we are looking for
        current_hash = self._hash(str(data))

        #iterate through the proof list
        for direction, sibling in vproof:

            #if the sibling is to the right, hash current_hash + sibling
            if direction == "right":
                current_hash = self._hash(current_hash + sibling)

            #if the sibling is to the left, hash sibling + current_hash
            else:
                current_hash = self._hash(sibling + current_hash)

        #if the current_hash equals the root hash, the proof is valid
        if current_hash == root:
            return True
        else:
            return False

    def _update_tree(self):
        """
        for use in insert and delete methods
        """
        self.hashed_data = self._first_hash(self.leaf_list)
        self.tree = self._build_tree(self.hashed_data)

    def insert(self, new_data):
        """
        add new data to the merkle tree
        re-hash the data
        remake the tree
        :param new_data: the new data
        """
        self.leaf_list.append(new_data)
        self._update_tree()

    def delete(self, data):
        """
        remove the data from the merkle tree
        re-hash the data
        remake the tree
        :param data: the data to be removed
        """
        self.leaf_list.remove(data)
        self._update_tree()

if __name__ == '__main__':
    L = [0, 1, 2]
    m1 = MerkleTree(L)

    m1.print_tree()
    print("\n")

    root1 = m1.get_root()
    proof1 = m1.get_proof(0)
    print(proof1)
    print(m1.verify_proof(0, proof1, root1))
    print("\n")

    proof2 = m1.get_proof(3)
    print(proof2)
    print(m1.verify_proof(3, proof2, root1))
    print("\n")

    m1.insert(3)
    m1.insert(4)
    m1.insert(5)
    m1.insert(6)
    m1.print_tree()
    print("\n")

    root2 = m1.get_root()
    proof3 = m1.get_proof(3)
    print(proof3)
    print(m1.verify_proof(3, proof3, root2))
    print("\n")

    m1.delete(1)
    m1.delete(3)
    m1.delete(5)
    m1.print_tree()
    print("\n")

    root3 = m1.get_root()
    proof4 = m1.get_proof(5)
    print(proof4)
    print(m1.verify_proof(5, proof4, root3))
    print("\n")

    '''
    Calculations from: https://merkle-tree-visualizer.vercel.app/
    
    Expected Output:
    ['5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35']
    ['fa13bb36c022a6943f37c638126a2c88fc8d008eb5a9fe8fcde17026807feae4', '32ee78186a3407f4f288673b1a7dca6154c294f435f444ee3ba054356a88a1e8']
    ['d32c0dae8492cecc66b77c89843c6c92dbedded6642ef9985f86edf6b5494a8f']
    
    [('right', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b'), ('right', 32ee78186a3407f4f288673b1a7dca6154c294f435f444ee3ba054356a88a1e8')]
    True
    
    None
    False
    
    ['5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', 'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d', 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683']
    ['fa13bb36c022a6943f37c638126a2c88fc8d008eb5a9fe8fcde17026807feae4', '70311d9d203b2d7e4ff70d7fce219f82a4fcf73a110dc80187dfefb7c6e4bb87', '67d62ee831ff99506ce1cd9435351408c3a845fca2dc0f34d085cdb51a37ec40', 'fffb4e1fe8e65e5cb2b79bc4c9fb36a73ecf24bf7ddcc83c3c16a2ab7e4a4eb6']
    ['862532e6a3c9aafc2016810598ed0cc3025af5640db73224f586b6f1138385f4', '2b5ad3840b128467887e99c725f65ac3748b8d9606d661ac165e140d403380b2']
    ['90fc4f35337ba5b81dabf61a3b2673b1209cf511e501898876ab46ed3bb7d63b']
    
    [('left', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35'), ('left', 'fa13bb36c022a6943f37c638126a2c88fc8d008eb5a9fe8fcde17026807feae4'), ('right', '2b5ad3840b128467887e99c725f65ac3748b8d9606d661ac165e140d403380b2')]
    True
    
    ['5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683']
    ['81b6ebd5fef6337923d48304e3984c2161790615b004fd473b903cbcd0251d56', 'cc8d9b1291bf3d8bef5c268c92d705d0961c68972fcc8e046333dfeaf8d14c1c']
    ['2a5adf79b3522cfe9e6408b7f05ac423f5e2f519ecf58eb35bbf12fbbd945c2d']
    
    None
    False
    '''
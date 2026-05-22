class Trie(object):

    def __init__(self):
        self._trie = {'': False}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        trie_node = self._trie
        for c in word:
            if c not in trie_node:
                trie_node[c] = {'': False}
            trie_node = trie_node[c]
        trie_node[''] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
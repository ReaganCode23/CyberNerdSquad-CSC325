class Trie:
    def __init__(self):
        # Initialize the trie as an empty dictionary
        self._trie = {}

    def insert(self, word: str) -> None:
        """
        Insert the word into the trie and increment the 
        count at each character node it passes through.
        """
        trie_node = self._trie
        for c in word:
            if c not in trie_node:
                # Initialize a new dictionary for the character
                # with a starting count of 0
                trie_node[c] = {'#count': 0}
            
            # Move to the child node and increment its prefix count
            trie_node = trie_node[c]
            trie_node['#count'] += 1

    def prefixCount(self, pref: str) -> int:
        """
        Traverses the trie following the characters in 'pref'.
        Returns the count stored at the final character's node.
        """
        trie_node = self._trie
        for c in pref:
            # If a character in the prefix doesn't exist, 
            # no words contain this prefix.
            if c not in trie_node:
                return 0
            trie_node = trie_node[c]
        
        # Return the number of words that passed through this specific node
        return trie_node['#count']

def prefixCount(words, pref):
    # 1. Create the Trie instance
    obj = Trie()
    
    # 2. Build the trie by inserting all words
    for word in words:
        obj.insert(word)
        
    # 3. Use the logic to count the occurrences of the prefix
    return obj.prefixCount(pref)


words = ["pay", "attention", "practice", "attend"]
pref = "at"
print(prefixCount(words, pref)) # Output: 2
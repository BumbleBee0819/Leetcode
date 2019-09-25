# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode(object):
    def __init__(self):
        self.tnlst = {}
        self.terminal = False

        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        r = self.root
        for w in word:
            if w not in r.tnlst:
                r.tnlst[w] = TrieNode()
            r = r.tnlst[w]
        r.terminal = True
        
        
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        r = self.root
        
        for w in word:
            if w in r.tnlst:
                r = r.tnlst[w]
            else:
                return False
        return r.terminal
        
        
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        r = self.root
        for w in prefix:
            if w in r.tnlst:
                r = r.tnlst[w]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# https://leetcode.com/problems/implement-trie-prefix-tree/


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = -1

        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        
        thisTree = self.root
        
        for i in word:
            if i not in thisTree:
                thisTree[i] = {}
                
            thisTree = thisTree[i]
            
        thisTree[self.end] = True
            
        
        
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        thisTree = self.root
        
        for i in word:
            if i not in thisTree:
                return False
            thisTree = thisTree[i]
        
        if self.end not in thisTree:
            return False
        
        return True
        
        
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        thisTree = self.root
        
        for i in prefix:
            if i not in thisTree:
                return False
            thisTree = thisTree[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

from sympy import false


class TrieNode:
    def __init__(self):
        self.child = {}
        self.endOfWord = False
        #children["a"] = TrieNode()

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pointed = self.root
        for chr in word:
            if chr not in pointed.children:
                pointed.children[chr] = TrieNode()
            ptd = ptd.children[chr]
        pointed.endOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for chr in word:
            if chr not in cur.children:
                return False
            cur = cur.children[chr]
        return cur.endOfWord
    def startsWith(self, prefix:str) -> bool:
        """
        Returns if the word starts with the given prefix.
        """
        cur = self.root
        for chr in prefix:
            if chr not in cur.children:
                return False
            cur = cur.children[chr]
        return True
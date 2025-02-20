# Time complexity - 1) insert - O(n), 2) search - O(n), 3) startWith - O(n)
# Space complexity - 1) insert - O(n), 2) search - O(1), 3) startWith - O(1)

# Approach - Initiate a TrieNode which keeps track is char is end of the word and it's children. During
# insert, check if there exists a TrieNode at the char's int index in curr char's children and if it doesn't
# initiate the Node. Go to that Node, check its children and so on. Similar logic implemented in search and
# startsWith.

class Trie:
    class TrieNode:
        def __init__(self):
            self.isEnd = False
            self.children = [None for i in range(26)]

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            ch_int = ord(ch) - ord('a')
            if curr.children[ch_int] == None:
                curr.children[ch_int] = self.TrieNode()
            curr = curr.children[ch_int]
        curr.isEnd = True 

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            ch_int = ord(ch) - ord('a')
            if curr.children[ch_int] == None:
                return False
            curr = curr.children[ch_int]
        return curr.isEnd        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            ch_int = ord(ch) - ord('a')
            if curr.children[ch_int] == None:
                return False
            curr = curr.children[ch_int]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
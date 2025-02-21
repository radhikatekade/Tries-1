# Time complexity - O(mk + nl) # m - len(sentence), k - avg len(word) in sentence, n - len(dictionary)
# l - avg len(word) in dictionary
# Space complexity - O(nl + l) # Extra l for the replacement string for word that we're maintaining

# Approach - Create a Trie from the dictionary. Split the sentence to get the list of all the words, compare
# each char in the word against the word in Trie and keep adding the char in replacement. 
# Once out of loop, check if we isEnd=True, put the replacement into our result, else put the original word
# in result. Finally join the result list to output desired sentence.

from typing import List
class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None for i in range(26)]
            self.isEnd = False
            
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            ch_int = ord(ch) - ord('a')
            if curr.children[ch_int] == None:
                curr.children[ch_int] = self.TrieNode()
            curr = curr.children[ch_int]
        curr.isEnd = True

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        if sentence == None or len(sentence) == 0:
            return sentence
        self.root = self.TrieNode()
        for word in dictionary:
            self.insert(word)
        split_sentence = sentence.split(" ")
        result = []
        for word in split_sentence:
            replacement = []
            curr = self.root
            for ch in word:
                ch_int = ord(ch) - ord('a')
                if curr.children[ch_int] == None or curr.isEnd == True:
                    break
                replacement.append(ch)
                curr = curr.children[ch_int]
            if curr.isEnd == True:
                result.append("".join(replacement))
            else:
                result.append(word)
        return " ".join(result)
from typing import Dict, List, Optional


class TreeNode:
    children: List[Optional["TreeNode"]]
    def __init__(self, letter: str):
        self.letter = letter
        self.children = [None for _ in range(26)]
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TreeNode("")

    def insert(self, word: str) -> None:
        ptr: TreeNode = self.root
        for char in word:
            charIdx = ord(char) - ord("a")
            if ptr.children[charIdx] is None:
                ptr.children[charIdx] = TreeNode(char)
            ptr = ptr.children[charIdx]
        ptr.isEnd = True

    def search(self, word: str) -> bool:
        ptr: TreeNode = self.root
        for char in word:
            charIdx = ord(char) - ord("a")
            if ptr.children[charIdx] is not None:
                ptr = ptr.children[charIdx]
            else:
                return False
        return ptr.isEnd

    def startsWith(self, prefix: str) -> bool:
        ptr: TreeNode = self.root
        for char in prefix:
            charIdx = ord(char) - ord("a")
            if ptr.children[charIdx] is not None:
                ptr = ptr.children[charIdx]
            else:
                return False
        return True
        
trie = Trie()
trie.insert("apple")
assert trie.search("apple")
assert not trie.search("app")
assert trie.startsWith("app")
trie.insert("app")
assert trie.search("app")
trie.insert("air")

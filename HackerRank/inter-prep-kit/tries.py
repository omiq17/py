class TrieNode:
    def __init__(self):
        self.noOfChild = 0
        self.child = [None]*26
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _charToInt(self, char):
        return ord(char)-ord("a")

    def insert(self, word):
        current = self.root
        length = len(word)

        for i in range(length):
            letter = self._charToInt(word[i])
            if not current.child[letter]:
                current.child[letter] = TrieNode()
            current = current.child[letter]
            current.noOfChild = current.noOfChild + 1
            

        current.endOfWord = True

    def search(self, word):
        current = self.root
        length = len(word)
        self.count = 0

        for i in range(length):
            letter = self._charToInt(word[i])
            if not current.child[letter]:
                return 0
            
            current = current.child[letter]
        
        return current.noOfChild


def main():
    n = int(input())

    trieObj = Trie()

    for i in range(n):
        op, value = map(str, input().split())

        if op=="add":
            trieObj.insert(value)
        else:
            count = trieObj.search(value)
            print(count)

main()
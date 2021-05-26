class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[None] = None

    def search(self, word):
        print("new search: ", word)
        def find(word, node):
            if not word:
                return None in node
            char, word = word[0], word[1:]
            print(char, "remaining: ", word)
            if char != '.':
                return char in node and find(word, node[char])

            for kid in node.values():
                if kid:
                    return find(word, kid)
            # return any(find(word, kid) for kid in node.values() if kid)

        return find(word, self.root)


wdic = WordDictionary()
wdic.addWord("bad")
wdic.addWord("dad")
wdic.addWord("mad")
assert wdic.search("pad") is False
wdic.addWord("bad")
assert wdic.search("b..") is True
assert wdic.search(".ad") is True

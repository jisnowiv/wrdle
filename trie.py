class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # O(n) time complexity
    def insert(self, word) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True

    # O(n) time complexity
    def check_word_exists(self, word) -> bool:
        node = self.root

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.end_of_word

    """
    def suggest_corrections(self, word):
        # Generate possible variations of the word
        # Check each variation against the Trie
        # Return valid suggestions
    """
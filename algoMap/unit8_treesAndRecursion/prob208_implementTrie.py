# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

#     Trie() Initializes the trie object.
#     void insert(String word) Inserts the string word into the trie.
#     boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#     boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

class Trie:

    def __init__(self):
        # Making disctionary of dictionaries
        self.trie = {}
        
    def insert(self, word: str) -> None:
        # Grab upper dictionary
        d = self.trie
        
        # Loop over char in word
        for char in word:
            # If char currently not current spot in d, add it
            if char not in d:
                d[char] = {}
            
            # Set current spot into nested dictionary
            d = d[char]
        
        # After word is made, make a "stop" entry to denote word is done 
        d['.'] = '.'

    def search(self, word: str) -> bool:
        # Grab upper dictionary
        d = self.trie
        
        # Loop over char in word
        for char in word:
            if char not in d:
                return False
            
            d = d[char]
        
        # If end of word was found, then full word was inserted
        return '.' in d

    def startsWith(self, prefix: str) -> bool:
        # Same as search method above, only difference is returning True after finding all prefix.
        # Does not matter if end of word was found or not
        d = self.trie
        
        for char in prefix:
            if char not in d:
                return False
            
            d = d[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
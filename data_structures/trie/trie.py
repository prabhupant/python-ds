class TrieNode:
    def __init__(self): 
          
        self.children = {} 
        self.last = False


class Trie:
    def __init__(self): 
          
        self.root = TrieNode() 
        self.word_list = [] 
  
    def form_trie(self, keys):
          
        for key in keys: 
            self.insert(key)
  
    def insert(self, key): 
          
        node = self.root 
  
        for a in list(key): 
            if not node.children.get(a): 
                node.children[a] = TrieNode() 
  
            node = node.children[a] 
  
        node.last = True
  
    def search(self, key): 
          
        node = self.root 
        found = True
  
        for a in list(key): 
            if not node.children.get(a): 
                found = False
                break
  
            node = node.children[a] 
  
        return node and node.last and found 
  
    def suggestions_rec(self, node, word):
          
        if node.last: 
            self.word_list.append(word) 
  
        for a, n in node.children.items():
            self.suggestions_rec(n, word + a)
  
    def print_auto_suggestions(self, key):
          
        node = self.root 
        not_found = False
        temp_word = '' 
  
        for a in list(key): 
            if not node.children.get(a): 
                not_found = True
                break
  
            temp_word += a 
            node = node.children[a] 
  
        if not_found: 
            return 0
        elif node.last and not node.children: 
            return -1
  
        self.suggestions_rec(node, temp_word)
  
        for s in self.word_list: 
            print(s) 
        return 1


# TESTING
KEYS = ["hello", "dog", "hell", "cat", "a",
        "hel", "help", "helps", "helping"]
KEY = "hel"
status = ["Not found", "Found"] 
  
t = Trie() 
  
t.form_trie(KEYS)
  
comp = t.print_auto_suggestions(KEY)
  
if comp == -1: 
    print("No other strings found with this prefix\n") 
elif comp == 0: 
    print("No string found with this prefix\n") 

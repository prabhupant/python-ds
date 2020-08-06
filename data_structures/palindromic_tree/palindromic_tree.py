import typing


class Node:
    def __init__(self):
        self.next: typing.Dict[str, Node] = {}
        self.frequency = 0
        self.length = 0
        self.suffix = None


class PalindromicTree:
    def __init__(self):
        self.null_root = Node()
        self.imaginary_root = Node()

        self.null_root.length = 0
        self.null_root.suffix = self.imaginary_root
        self.imaginary_root.length = -1
        self.imaginary_root.suffix = self.imaginary_root

        self.counter = 0
        self.all_palindromes: list[Node] = []
        self.previous = self.imaginary_root

    def add_letter(self, string, index):
        while index - 1 - self.previous.length < 0 or string[index - 1 - self.previous.length] != string[index]:
            self.previous = self.previous.suffix

        if self.previous.next.get(string[index]) is not None:
            node = self.previous.next.get(string[index])
            node.frequency += 1
            self.previous = node
            return

        new_node = Node()

        self.counter += 1
        new_node.frequency = 1
        new_node.length = self.previous.length + 2
        self.previous.next[string[index]] = new_node

        if new_node.length == 1:
            new_node.suffix = self.null_root
            self.previous = new_node
        else:
            self.previous = self.previous.suffix
            while index - 1 - self.previous.length < 0 or string[index - 1 - self.previous.length] != string[index]:
                self.previous = self.previous.suffix
            new_node.suffix = self.previous.next[string[index]]
            self.previous = new_node
        self.all_palindromes.append(new_node)

    def how_many_palindromes(self):
        all_nr = 0
        for node in reversed(self.all_palindromes):
            node.suffix.frequency += node.frequency
            all_nr += node.frequency
        print(f"There are {self.counter} unique palindromes and {all_nr} in total")


tree = PalindromicTree()

s = "abaxxaba"
for i in range(len(s)):
    tree.add_letter(s, i)
tree.how_many_palindromes()


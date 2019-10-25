# python3

import sys, threading, os
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:

    def __init__(self):
        self.n = 0
        self.parent = None
        self.cache = [0]

    def set(self, file):
        with open(file) as source:
            self.n = int(source.readline())
            self.parent = list(map(int, source.readline().split()))
            self.cache = [0] * self.n

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.cache = [0] * self.n

    def cached_len(self, node_id):
        parent = self.parent[node_id]
        if parent == -1:
            return 1
        if self.cache[node_id]:
            return self.cache[node_id]
        self.cache[node_id] = 1 + self.cached_len(self.parent[node_id])
        return self.cache[node_id]

    def compute_height(self):
        """Computes the tree height."""
        return max([self.cached_len(i) for i in range(self.n)])

def main():
    def prod():
        tree = TreeHeight()
        tree.read()
        print(tree.compute_height())

    def test():
        test_input = [name for name in os.listdir('./tests') if 'a' not in name]
        test_output = [name for name in os.listdir('./tests') if 'a' in name]
        for input_val, output_val in zip(test_input,test_output):
            tree = TreeHeight()
            tree.set('./tests/' + input_val)
            with open('./tests/' + output_val) as result_file:
                result = int(result_file.readline())
                print(result)
                print(tree.compute_height())
                assert(result == tree.compute_height())
    prod()

threading.Thread(target=main).start()

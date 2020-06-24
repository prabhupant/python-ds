class Stack():
    """
    Stack follows Last-In-First-Out methodology
    """

    def __init__(self):
        self.entries = []

    def size(self):
        return len(self.entries)

    def push(self, val):
        self.entries.append(val)

    def pop(self):
        if self.size() > 0:
            self.entries.pop(self.size() - 1)

    




    
    
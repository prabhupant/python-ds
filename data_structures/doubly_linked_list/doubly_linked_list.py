class Node:
    def __init__(self, data=None, nxt=None, previous=None):
        self.data = data
        self.next = nxt
        self.previous = previous


class Lista:
    
    def __init__(self):
        self.first = self.last = Node()

    def empty(self):
        return self.first.data == self.last.data
    
    def search(self, data):
        if self.empty():
            return None
        
        auxiliary = self.first.next
        while auxiliary.next is not None and auxiliary.data != data:
            auxiliary = auxiliary.next

        if auxiliary.data == data:
            return auxiliary.data

        return None
        
    def append(self, data):
        self.last.next = Node(data=data, next=None, previous=self.last)
        self.last = self.last.next

    def __str__(self):
        
        if self.empty():
            return ""

        aux = self.first
        format_ = ""
        
        while aux.next is not None:
            if aux.data is not None:
                format_ += str(aux.data) + " "
            aux = aux.next
        format_ += str(aux.data) + ""
        
        return format_

    def remove(self, data):
        if self.empty():
            return None

        auxiliary = self.first.next

        while auxiliary is not None and auxiliary.data != data:
            auxiliary = auxiliary.next

        if auxiliary is None:
            return None
        else:
            item = auxiliary.data

            if auxiliary.previous is not None:
                auxiliary.previous.next = auxiliary.next
            if auxiliary.next is not None:
                auxiliary.next.previous = auxiliary.previous

        if self.empty():
            self.last = self.first = Node()
        elif auxiliary.next is None:
            self.last = auxiliary.previous

        del auxiliary
        return item


# the auxiliary variable is to help like a flag in the code, like aux too
# If something isn't right, or in another language it is bc I am a native
# portuguese speaker, so I translated my code

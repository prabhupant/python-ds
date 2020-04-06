class Node:
    def __init__(self, data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

class Lista:
    
    def __init__(self):
        self.first = self.last = Node()

    def empty(self):
        return self.first.data == self.last.data

    
    def search(self, data):
        if self.empty(): return None
        
        auxiliar = self.first.next
        while auxiliar.next != None and auxiliar.data != data:
                auxiliar = auxiliar.next

        if auxiliar.data == data:
            return auxiliar.data

        return None
        
    def append(self, data):
        self.last.next = Node(data = data, next = None, previous = self.last)
        self.last = self.last.next


    def __str__(self):
        
        if self.empty():
            return ""

        aux = self.first
        format_ = ""
        
        while aux.next != None:
            if aux.data!= None:
                format_ += str(aux.data) + " "
            aux = aux.next
        format_ += str(aux.data) + ""
        
        return format_

    def remove(self, data):
        if self.empty(): return None

        auxiliar = self.first.next

        while auxiliar != None and auxiliar.data != data:
            auxiliar = auxiliar.next

        if auxiliar == None: return None
        else:
            item = auxiliar.data

            if auxiliar.previous != None:
                auxiliar.previous.next = auxiliar.next
            if auxiliar.next != None:
                auxiliar.next.previous = auxiliar.previous

        if self.empty(): self.last = self.first = Node()
        elif auxiliar.next == None: self.last = auxiliar.previous

        del auxiliar
        return item



        #the auxiliar variable is to help like a flag in the code, like aux too
        #If something isn't right, or in another language it is bc I am a native portuguese speaker, so I translated my code

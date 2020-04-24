class Deque():
    def __init__(self):
        self.data = list()

    def push_front(self, elem):
        temp = list()
        temp.append(elem)

        for i in self.data:
            temp.append(i)
        
        self.data = temp

    def push_back(self, elem):
        self.data.append(elem)

    def pop_front(self):
        temp = list()

        for i in range(0, len(self.data)):
            if not i==0:
                temp.append(self.data[i])
        
        self.data = temp
    
    def pop_back(self):
        temp = list()

        for i in range(0, len(self.data)):
            if not i==len(self.data)-1:
                temp.append(self.data[i])
        
        self.data = temp

    def get_first(self):
        if(len(self.data)>0):
            return self.data[0]
        else:
            return "Deque is empty"

    def get_last(self):
        if(len(self.data)>0):
            return self.data[len(self.data)-1]
        else:
            return "Deque is empty"

    def size(self):
        return len(self.data)

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False

    def contains(self, elem):
        for i in self.data:
            if i==elem:
                return True
        
        return False

    def printElems(self):
        result = ""

        for i in self.data:
            result += str(i) + " | "
        
        print(result)
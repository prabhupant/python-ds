# The explanation has been taken from GeeksforGeeks

'''
Circular Queue is a linear data structure in which the operations
are performed based on FIFO (First In First Out) principle and the
last position is connected back to the first position to make a circle.
It is also called ‘Ring Buffer’.
Applications:

    Memory Management: The unused memory locations in the case of ordinary
    queues can be utilized in circular queues.
    Traffic system: In computer controlled traffic system, circular queues
    are used to switch on the traffic lights one by one repeatedly as per the time set.
    CPU Scheduling: Operating systems often maintain a queue of processes
    that are ready to execute or that are waiting for a particular event to occur.
'''



class circularQueue:
    #First created a constructor and took some input from user
    def __init__(self, MaxSize):
        self.cqueue = list()
        self.MaxSize = MaxSize
        self.rear = 0
        self.front = 0
    #define the size of the queue
    def size(self):
            if(self.rear >= self.front):
                cqSize = self.rear - self.front
            else:
                cqSize = self.MaxSize - (self.front - self.rear)
            return cqSize
    
    #Now let's add some elements in our queue..!!
    def insert(self, data):
        if(self.size() == self.MaxSize-1):
            return("Queue is full..!!")
        else:
            self.cqueue.append(data)
            self.rear = (self.rear+1) % self.MaxSize
            return True
    #Now if we want to remove any element from the queue, then-
    def remove(self):
        if(self.size() == 0):
            return("Queue is empty..!!")
        else:
            data = self.cqueue[self.front]
            self.front = (self.front+1) % self.MaxSize
            return data
        
size = input("Enter the size of the Circular Queue - ")
c = circularQueue(int(size))
print(c.insert(1))
print(c.insert(2))
print(c.insert(3))
print(c.insert("COD"))
print(c.insert("PUBG"))
print(c.insert(4))
print(c.insert(5))
print(c.insert(6))
print("***Now Removing all***")
print(c.remove())
print(c.remove())
print(c.remove())
print(c.remove())
print(c.remove())
print(c.remove())
print(c.remove())
print(c.remove())
print(c.remove())

#A basic queue has the following operations:
#Enqueue: add a new element to the end of the queue.
#Dequeue: remove the element from the front of the queue and return it.
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def pop(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()

    def put(self, value):
        self.stack1.append(value)
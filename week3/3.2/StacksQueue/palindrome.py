from collections import deque
from queue import Queue

class Stack:
    def __init__(self):
        self.dataStack = []

    def pushData(self, data):
        self.dataStack.append(data)
    
    def popData(self):
        return self.dataStack.pop()
    
    def size(self):
        return len(self.dataStack)

    def isEmpty(self):
        return True if self.size() == 0 else False
    
    def peek(self):
        return self.dataStack[-1]

class Queue:
    def __init__(self):
        self.dataQueue = deque()

    def enqueue(self, data):
        self.dataQueue.append(data)
    
    def dequeue(self):
        return self.dataQueue.popleft()
    
    def peek(self):
        return self.dataQueue[0]
    
    def isEmpty(self):
        return len(self.dataQueue) == 0
    
    def size(self):
        return len(self.dataQueue)

    def __str__(self):
        return str(self.dataQueue)


def isPalindrome(self):
        for x in self:
            True if x == x[::-1] else False

stack = Stack()
stack.pushData('racecar')
stack.pushData('noon')
stack.pushData('python')
stack.pushData('madam')
print(stack.popData())
print(stack.size())
print(stack.isEmpty())
print(stack.peek())
print(stack.dataStack)
print(isPalindrome(stack.dataStack))

queue = Queue()
queue.enqueue('racecar')
queue.enqueue('noon')
queue.enqueue('python')
queue.enqueue('madam')
print(queue.size())
print(queue.dequeue())
print(queue.peek())
print(queue.isEmpty())
print(isPalindrome(queue))

from queue import Queue


class Stack:
    def __init__(self):
        self.dataStack = []

    def push(self, data):
        self.dataStack.append(data)
    
    def pop(self):
        return self.dataStack.pop()
    
    def size(self):
        return len(self.dataStack)

    def isEmpty(self):
        return True if self.size() == 0 else False
    
    def peek(self):
        return self.dataStack[-1]
    
    def __str__(self):
        return str(self.dataStack)

class Queue:
    def __init__(self):
        self.dataQueue = []

    def enqueue(self, data):
        self.dataQueue.insert(0,data)
    
    def dequeue(self):
        return self.dataQueue.pop()
    
    def peek(self):
        return self.dataQueue[-1]
    
    def isEmpty(self):
        return len(self.dataQueue) == 0
    
    def size(self):
        return len(self.dataQueue)

    def __str__(self):
        return str(self.dataQueue)


def isPalindrome(str):
        stack = Stack()
        queue = Queue()

        for e in str:
            stack.push(e)
            queue.enqueue(e)

        while not stack.isEmpty():
            if stack.pop() != queue.dequeue():
                return False

        return True

print(isPalindrome('racecar'))
print(isPalindrome('noon'))
print(isPalindrome('python'))
print(isPalindrome('madam'))


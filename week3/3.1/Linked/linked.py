class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0
    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
    def size(self) -> int:
        return self.count

    def addFirst(self, data) -> None:
        newNode = Node(data)
        self.count += 1

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def addLast(self, data) -> None:
        newNode = Node(data)
        self.count += 1

        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        


    def addAtIndex(self, data, index):
        newNode = Node(data)

        if (index < 1):
            print('Invalid Index')
        elif (index == 1):
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, index-1):
                if(temp != None):
                    temp = temp.next
        
            if(temp != None):
                newNode.next = temp.next
                temp.next = newNode
            else:
                print('Previous node is null')

        


    def indexOf(self, data):
        temp = self.head
        found = 0
        i = 0
        if(temp != 0):
            while (temp != None):
                i += 1
                if(temp.data == data):
                    found += 1
                    break
                temp = temp.next
            if (found == 1):
                print(data, 'is at index', i)
            else:
                print(data, 'is not in the list.')
        else:
            print('List is empty.')


    # def add(self, data) -> None:
    
    #     self.addLast(data)



    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0



    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.
        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head
        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1
        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       
        return
    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

            
    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data
    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value
    def __str__(self):
        myStr = ""
        for node in self.iter():
            myStr += str(node)+ " "
        return myStr



doubleLink = DoublyLinkedList()
doubleLink.addFirst('May')
doubleLink.addLast('You')
doubleLink.addAtIndex('The', 2)
doubleLink.addAtIndex('Force', 3)
doubleLink.addAtIndex('Be', 4)
doubleLink.addAtIndex('With', 5)
doubleLink.indexOf('May')
print(doubleLink)
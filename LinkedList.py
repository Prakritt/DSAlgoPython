class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = newNode
            return 
        
    def printList(self):
        if self.head is None:
            return
        else:
            currentNode = self.head
            while(currentNode):
                print(currentNode.data,end=" ")
                currentNode = currentNode.next
            print()

    def deleteElement(self, data):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.data == data:
            self.head = self.head.next
        else:
            prevNode = self.head
            currentNode = prevNode.next
            while(currentNode):
                if currentNode.data == data:
                    prevNode.next = currentNode.next
                    break
                else:
                    prevNode = currentNode
                    currentNode = currentNode.next

                


ll  = LinkedList()
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(4)
ll.insertAtEnd(5)
ll.deleteElement(6)
ll.printList()

    


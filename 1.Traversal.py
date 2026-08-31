class Node:

    def _init_(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def _init_(self):

        self.head = None


    def printList(self):

        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if _name_ == '_main_':

    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()

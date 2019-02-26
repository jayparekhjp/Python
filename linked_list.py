class Node:
    def __init__(self,value):
        self.data = value
        self.link = None
class SingleLinkedList:
    def __init__(self):
        self.start = None
    def display_list(self):
        if self.start == None:
            print('List Empty')
        else:
            p = self.start
            while p != None:
                print(p.data)
                p = p.link
    def count_nodes(self):
        p = self.start
        count = 0
        while p != None:
            count +=1
            p = p.link
        return count
    def find_node(self,val):
        position = 1
        p = self.start
        while p != None:
            if p.data == val:
                print('Value at Node',position)
                return True
            position += 1
            p = p.link
        print('Value not found')
        return False
    def insert_at_beginning(self,data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
    def insert_at_end(self,data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
        else:
            p = self.start
            while p.link is not None:
                p = p.link
            p.link = temp
    def create_list(self):
        n = int(input('Number of nodes:'))
        for _ in range(n):
            data = input('Node data:')
            self.insert_at_end(data)

##################################################################################################################################################################

mylist = SingleLinkedList()
mylist.create_list()

while True:
    print('1. Display list')
    print('2. Count number of nodes in list')
    print('3. Search element in list')
    print('4. Insert a node in beginning of the list')
    print('5. Insert a node at the end of the list')
    print('6. Insert a node after specific node')
    print('7. Insert a node before specific node')
    print('8. Insert a node at given position')
    print('9. Delete first node')
    print('10. Delete last node')
    print('11. Delete any node')
    print('12. Reverse list')
    print('13. Bubble sort by exchanging data')
    print('14. Bubble sort by exchanging links')
    print('15. Merge sort')
    print('16. Insert cycle')
    print('17. Delete cycle')
    print('18. Remove cycle')
    print('100. Quit')

    option = int(input('Enter your choice:'))
    if option == 1:
        mylist.display_list()
    elif option == 2:
        mylist.count_nodes()
    elif option == 3:
        data = input('Enter value to be searched')
        mylist.find_node(data)
    elif option == 4:
        data = input('Enter the element to be inserted:')
        mylist.insert_at_beginning(data)
    elif option == 5:
        data = input('Enter the element to be inserted:')
        mylist.insert_at_end(data)
    elif option == 100:
        break

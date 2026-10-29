
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        newnode = Node(data)

        if self.head is not None:
            newnode.next = self.head
            self.head.prev = newnode

        self.head = newnode
        print("Value inserted at beginning")

    # Insert at end
    def insert_end(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = newnode
            newnode.prev = temp

        print("Value inserted at end")

    # Insert at specific position (1-based)
    def insert_position(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.insert_begin(data)
            return

        temp = self.head
        i = 1

        while temp is not None and i < pos - 1:
            temp = temp.next
            i += 1

        if temp is None:
            print("Invalid position")
            return

        newnode = Node(data)

        newnode.next = temp.next
        newnode.prev = temp

        if temp.next is not None:
            temp.next.prev = newnode

        temp.next = newnode
        print("Value inserted at position", pos)

    # Delete from beginning
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None

            print("Value deleted from beginning")

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.next is None:
            self.head = None
            print("Value deleted from end")
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.prev.next = None
            print("Value deleted from end")

    # Delete from specific position
    def delete_position(self, pos):
        if self.head is None:
            print("Linked list is empty")
            return

        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.delete_begin()
            return

        temp = self.head
        i = 1

        while temp is not None and i < pos:
            temp = temp.next
            i += 1

        if temp is None:
            print("Invalid position")
        else:
            temp.prev.next = temp.next

            if temp.next is not None:
                temp.next.prev = temp.prev

            print("Node deleted from position", pos)

    # Display the list
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head

            while temp is not None:
                print(temp.data, end=" <-> ")
                temp = temp.next

            print("None")

    # Count nodes
    def count(self):
        temp = self.head
        c = 0

        while temp is not None:
            c += 1
            temp = temp.next

        print("Total number of nodes:", c)

    # Search a value
    def search(self, key):
        temp = self.head
        pos = 1

        while temp is not None:
            if temp.data == key:
                print("Value found at position", pos)
                return

            temp = temp.next
            pos += 1

        print("Value not found")

    # Reverse the doubly linked list
    def reverse(self):
        temp = self.head
        prev = None

        while temp is not None:
            nextnode = temp.next

            temp.next = temp.prev
            temp.prev = nextnode

            prev = temp
            temp = nextnode

        self.head = prev
        print("Linked list reversed")


s = DLL()

while True:
    print("\n--- DOUBLY LINKED LIST MENU ---")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at specific position")
    print("4. Delete from beginning")
    print("5. Delete from end")
    print("6. Delete from specific position")
    print("7. Display")
    print("8. Count the nodes")
    print("9. Search a value")
    print("10. Reverse the linked list")
    print("0. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 0:
        print("Program exited")
        break

    elif ch == 1:
        data = int(input("Enter value: "))
        s.insert_begin(data)

    elif ch == 2:
        data = int(input("Enter value: "))
        s.insert_end(data)

    elif ch == 3:
        data = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        s.insert_position(data, pos)

    elif ch == 4:
        s.delete_begin()

    elif ch == 5:
        s.delete_end()

    elif ch == 6:
        pos = int(input("Enter position to delete: "))
        s.delete_position(pos)

    elif ch == 7:
        s.display()

    elif ch == 8:
        s.count()

    elif ch == 9:
        key = int(input("Enter value to search: "))
        s.search(key)

    elif ch == 10:
        s.reverse()

    else:
        print("Invalid choice")

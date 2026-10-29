
class Stack:
    def __init__(self):
        self.list = []

    # Insert an element
    def push(self, item):
        self.list.append(item)
        print(item, "inserted")

    # Remove an element
    def pop(self):
        if len(self.list) == 0:
            print("Stack is empty")
        else:
            print(self.list.pop(), "removed")

    # Display the top element
    def peek(self):
        if len(self.list) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.list[-1])

    # Display all elements
    def display(self):
        print("Stack:", self.list)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
s.peek()
s.pop()
s.display()

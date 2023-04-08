
"""
Create a Class for Stack using List and make methods for 
 - push
 - pop
 - is_empty
 - is_full
 - empty_stack

Stack takes its size as initialization.
"""
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [size - 1]
        self.stack.clear()

    def push(self, data):
        if len(self.stack) == self.size:
            print("Stack is full!")
            return
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            print("Stack is empty!")
            return
        return self.stack.pop()

    def is_empty(self):
        return not bool(self.stack)

    def is_full(self):
        return len(self.stack) == self.size
    
    def empty_stack(self):
        return self.stack.clear()


# Create a stack with capacity of 5
print("\nStack initialised with size of 5.")
my_stack = Stack(5)

# Push some items onto the stack
print("\nInserting data '1', '2', '3' into the stack using 'push()' function")
print("Inserting 1")
my_stack.push(1)
print("Inserting 2")
my_stack.push(2)
print("Inserting 3")
my_stack.push(3)
print("Stack: ", my_stack.stack)


# Pop an item off the stack
print("\nNow Deleting item last item (which is '3' in our case) using 'pop()' function")
print("Deleting last_item")
popped_item = my_stack.pop()
print("Stack: ", my_stack.stack)

# Check if the stack is empty or full
print("\nNow checking if stack is empty using 'is_empty()' function: ", my_stack.is_empty())  # prints False
print("\nNow checking if stack is full using 'is_full()' function: ", my_stack.is_full())   # prints False
print("Stack: ", my_stack.stack)


# Push some more items onto the stack
print("\nInserting more data into stack '4', '5' using 'push()' function: ")
print("Inserting 3")
my_stack.push(3)
print("Inserting 4")
my_stack.push(4)
print("Inserting 5") 
my_stack.push(5)
print("Stack: ", my_stack.stack)


# Try to push another item onto the full stack
print("\nInserting a data '6' using 'push()' function when the stack is full, gives error!")
print("Inserting 6") 
my_stack.push(6)  # prints "Stack is full!"
print("Stack: ", my_stack.stack, "| Stack size: ", my_stack.size)

# Clear all items off the stack
print("\nEmpty the stack of all datas using 'empty_stack()' function")
print("Emptying all_items") 
my_stack.empty_stack()
print("Stack: ", my_stack.stack)

# Check if the stack is empty using
print("\nNow checking if stack is empty using 'is_empty()' function: ", my_stack.is_empty())  # prints True



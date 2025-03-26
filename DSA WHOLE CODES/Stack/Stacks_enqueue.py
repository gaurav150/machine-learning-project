class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        # Step 1: Move all elements from stack1 to stack2
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

        # Step 2: Push the new element into stack1
        self.stack1.append(value)

        # Step 3: Move all elements back from stack2 to stack1
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
    
    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        
        

# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())


"""
    EXPECTED OUTPUT:
    ----------------
    Front of the queue: 1
    Is the queue empty? False
    
"""

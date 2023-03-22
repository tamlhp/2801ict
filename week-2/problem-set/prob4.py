import heapq

class Call:
    def __init__(self, priority, caller):
        self.priority = priority
        self.caller = caller
    
    def __lt__(self, other):
        return self.priority < other.priority

class CallCenter:
    def __init__(self):
        self.calls = []
    
    def add_call(self, priority, caller):
        heapq.heappush(self.calls, Call(priority, caller))
    
    def answer_call(self):
        if self.calls:
            return heapq.heappop(self.calls).caller
        else:
            return None

class CustomerOrder:
    def __init__(self, order_number, customer):
        self.order_number = order_number
        self.customer = customer

class OrderQueue:
    def __init__(self):
        self.orders = []
    
    def add_order(self, order_number, customer):
        self.orders.append(CustomerOrder(order_number, customer))
    
    def send_order(self):
        if self.orders:
            return self.orders.pop(0).customer
        else:
            return None

class Calculator:
    def __init__(self):
        self.stack = []
    
    def calculate(self, expression):
        stack = []

        for token in expression.split():
            if token.isdigit():
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    stack.append(int(operand1 / operand2))
                else:
                    raise ValueError('Invalid operator')

        if len(stack) != 1:
            raise ValueError('Invalid expression')

        return stack.pop()



# Create a CallCenter object
cc = CallCenter()

# Add some calls to the queue with different priorities
cc.add_call(3, "John")
cc.add_call(1, "Jane")
cc.add_call(2, "Jim")

# Answer the highest priority call
print(cc.answer_call())  # "Jane"
print(cc.answer_call())  # "Jim"
print(cc.answer_call())  # "John"
print(cc.answer_call())  # None (no more calls in queue)

# Create an OrderQueue object
oq = OrderQueue()

# Add some orders to the queue
oq.add_order(1, "John")
oq.add_order(2, "Jane")
oq.add_order(3, "Jim")

# Send the next order in the queue
print(oq.send_order())  # "John"
print(oq.send_order())  # "Jane"
print(oq.send_order())  # "Jim"
print(oq.send_order())  # None (no more orders in queue)

# Create a Calculator object
calc = Calculator()

result = calc.calculate('5 1 2 + 4 * + 3 -') # Evaluates to 14
"""
In this example, we evaluate the expression "5 1 2 + 4 * + 3 -", 
which represents the infix expression "(5 + (1 + 2) * 4) - 3". 
The result should be 14, and this is what is printed to the console.
"""
print(result)


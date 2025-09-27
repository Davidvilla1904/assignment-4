
'''
17. Service Line Simulation
Simulate a line where values are added at one end and removed from the other.
Actions: add("A"), add("B"), serve()
Output: "A"

'''

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Line:
  def __init__(self):
    self.front = None
    self.rear = None

  def add(self, value):
    new_value = Node(value)
    if not self.front:
      self.front = new_value
      self.rear = new_value
    else:
      self.rear.next = new_value
      self.rear = new_value

  def serve(self):
    if not self.front:
      return None
    removed_value = self.front
    self.front = self.front.next
    if not self.front:
      self.rear = None
    return removed_value.value


'''
What structure did I choose and why?

I chose a queue implemented with a linked list because the service line problem is naturally first-in, first-out. 
This structure allows me to add new items at the end and serve from the front efficiently. 
By maintaining references to both the front and rear nodes, each operation occurs in constant time regardless of the number of items. 
This would not be possible with a stack, which is last-in, first-out.

How the time limit shaped my decision:

Since we got only 30 minutes, I looked through all the challenges and looked at which I immediately had a plan for, ready in my head on how to tackle it. 
This took me a little bit, but once I saw this one, I knew how to do it. 
It was a classic queue problem, so I had to write the code we learned in one of the resources and only tweak it a little bit to have the variables be a good name to match the problem. 
Because I knew what to do on forehand, I had plenty of time to edge case it and make sure I did it right.

What trade-offs and compromises did I make under time pressure?

Under the 30-minute time limit, I focused on solving the problem efficiently rather than optimizing for every possible detail. 
I reused the standard queue implementation we had learned instead of designing a more elaborate solution, like a deque that could add or remove from both ends. 
I also prioritized getting the basic functionality correct over adding extra features. 
This allowed me to finish on time, test edge cases, and ensure the core solution was correct.

'''
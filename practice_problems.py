"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    if len(product_ids) == len(set(product_ids)):
        print("False")
    else:
        print("True")

#Comparing a list with an set is the right data structure, because an set deletes all the duplicates.
#And if the length from a list is longer then the set means there is a duplicate that has been deleted in the set.
#It will run pretty quickly as all it has to do is count the amount of values, will take longer the longer the list is.

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_task(self, task):
        new_task = Node(task)
        if not self.front:
            self.front = new_task
            self.rear = new_task
        else:
            self.rear.next = new_task
            self.rear = new_task

    def remove_oldest_task(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node.task()

#A queue is a perfect solution for this problem, because this is a first-in, first-out kind of problem.
#You also need to be able to add from the front and delete from the back and with a stack that is not possible
#The runtime wont change with the length of list, because the code will only be accessing the front and rear value

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        pass

    def add(self, value):
        pass

    def get_unique_count(self):
        pass

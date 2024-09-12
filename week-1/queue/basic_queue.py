class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item): #adds an element to the end of the queue happens at the rear end of the queue time complexity is O(1)
        self.queue.append(item)

    def dequeue(self):#removes the first element of the queue happens at front end of the queue time complexity is O(1) where n is the size of the queue
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)



queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
print(queue.dequeue())
print(queue.is_empty())





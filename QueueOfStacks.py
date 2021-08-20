# Cristian Aurelio Ramirez Anzaldo
# A01066337

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def last(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.S1 = Stack()
        self.S2 = Stack()

    def isEmpty(self):
        return self.S1.isEmpty() and self.S2.isEmpty()

    def enqueue(self, item):
        self.S1.push(item)

    def dequeue(self):
        for i in range(0, self.S1.size()):
            self.S2.push(self.S1.pop())

        x_dequeue = self.S2.last()

        for i in range(0, self.S2.size()):
            self.S1.push(self.S2.pop())

        return x_dequeue

    def size(self):
        return self.S1.size()


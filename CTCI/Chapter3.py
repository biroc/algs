"""
3.2 Stack min.
"""

class StackMin:

    def __init__(self):
        self.values = []
        self.minStack = []

    def push(self,x):
        self.values.append(x)
        if not self.minStack or x <= self.min():
            self.minStack.append(x)

    def pop(self):
        if self.values:
            removed = self.values.pop()
            if removed == self.minStack[-1]:
                self.minStack.pop()

    def peek(self):
        if self.values:
            return self.values[-1]


    def min(self):
        if self.minStack:
            return self.minStack[-1]
        else:
            return None

"""
3.3 Stack of Plates
"""
class SetOfStacks:
    def __init__(self,limit):
        self.stacks = []
        self.limit = limit

    def push(self,x):
        if not self.stacks:
            self.stacks.append([x])
        else:
            last = self.stacks[-1]
            if len(last) == self.limit:
                self.stacks.append([x])
            else:
                last.append(x)

    def pop(self):
        if self.stacks:
            if len(self.stacks[-1]) == 1:
                self.stacks.pop()
            else:
                self.stacks[-1].pop()

    def peak(self):
        if self.stacks:
            return self.stacks[-1][-1]


    def popAt(self,index):
        if index >= len(self.stacks):
            return
        else:
            if len(self.stacks[index]) == self.limit:
                self.stacks[index].pop()
                while index < len(self.stacks) and len(self.stacks[index]) == self.limit -1:
                    if index + 1< len(self.stacks):
                        self.stacks[index].append(self.stacks[index+1].pop())

                    index += 1
            else:
                self.stacks[index].pop()

        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

"""
3.4 Queue via Stacks. Implement a queue using 2 stacks.
"""

class QueueStack:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self,x):
        self.instack.append(x)

    def dequeue(self):
        if self.outstack:
            return self.outstack.pop()

        else:
            i = len(self.instack) - 1
            for i in range(len(self.instack)):
                self.outstack.append(self.instack.pop())

            if self.outstack:
               return self.outstack.pop()

    def isEmpty(self):
        if not self.outstack and not self.instack:
            return True
        return False


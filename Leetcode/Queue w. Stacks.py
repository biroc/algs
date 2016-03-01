class Queue(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x):
        self.instack.append(x)


    def pop(self):
        if self.outstack:
            self.outstack.pop()
        else:
            for i in range(len(self.instack)):
                peak = self.instack.pop()
                self.outstack.append(peak)
            self.outstack.pop()


    def peek(self):
        if self.outstack:
            return self.outstack[-1]
        else:
            for i in range(len(self.instack)):
                p = self.instack.pop()
                self.outstack.append(p)
            return self.outstack[-1]


    def empty(self):
        if not self.outstack and not self.instack:
            return True
        return False
        
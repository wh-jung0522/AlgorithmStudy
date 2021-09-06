'''Data Structure'''
class myStack():
    def __init__(self) -> None:
        self.stack = []
        pass
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def get(self,Reverse=False):
        if Reverse:
            return self.stack[::-1]
        else:
            return self.stack

class myQueue():
    def __init__(self) -> None:
        from collections import deque
        self.queue = deque()
        pass
    def push(self,element):
        self.queue.append(element)
    def pop(self):
        return self.queue.popleft()
    def get(self,Reverse=False):
        if Reverse:
            return self.queue.reverse()
        else:
            return self.queue

class myPriorityQueue():
    def __init__(self) -> None:
        pass
    def push():
        ## TODO
        return
    def pop():
        ## TODO
        return
    
class Stack:
    '''
    The Stack data structure
    '''

    data = []

    def __init__(self, **kwargs):
        _data = kwargs.get("data")
        if _data and not isinstance(_data, list):
            raise TypeError("Invalid data type, must be a list")
        self.data = _data or []

    def append(self, val):
        '''
        Append an element to the stack

        :param val: Element value
        '''

        self.data.append(val)

    def pop(self):
        '''Pops out the last element from stack'''

        return self.data.pop()

    def __str__(self):
        return str(self.data)


s = Stack(data=[3, 4, 5])
s.append(2)
print(s)
print(s.pop())


class Queue:
    ''' The Queue data structure '''

    data = []

    def __init__(self, **kwargs):
        _data = kwargs.get("data")
        if _data and not isinstance(_data, list):
            raise TypeError("Invalid data type, must be a list")
        self.data = _data or []

    def enqueue(self, val):
        '''
        Add an element to the queue

        :param val: Element value
        '''
        self.data.insert(0, val)

    def dequeue(self):
        '''Pops out the first entered element for the queue'''
        return self.data.pop()


q = Queue(data=[1])

q.enqueue(2)
q.enqueue(3)

print(q.dequeue())

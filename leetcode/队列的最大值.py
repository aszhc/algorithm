import queue

class MaxQueue(object):

    def __init__(self):
        self.deque = queue.deque()

    def max_value(self):
        """
        :rtype: int
        """
        return max(self.deque) if self.deque else -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.deque.append(value)


    def pop_front(self):
        """
        :rtype: int
        """
        return self.deque.popleft() if self.deque else -1



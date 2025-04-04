class MyQueue(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.s1 :
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        

    def pop(self):
        """
        :rtype: int
        """
        return self.s1.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.s1   
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
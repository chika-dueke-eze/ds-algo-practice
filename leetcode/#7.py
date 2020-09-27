#Reverse Integer Problem
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.x = str(x)              #convert input to a string to be able to reverse
        self.x = int(self.x[::-1])   #reverse string and convert back to int
        return self.x

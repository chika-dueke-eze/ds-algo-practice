class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = str(x)
        if self.x == self.x[::-1]:
            return "true"
        else:
            return "false"

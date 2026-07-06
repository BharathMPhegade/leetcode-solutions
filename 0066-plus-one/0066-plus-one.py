class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in digits:
            num =(num*10)+i
        
        num = num+1
        s = str(num)
        n = len(digits) - 1
        res = []
        for i in s:
            res.append(int(i))
        return res


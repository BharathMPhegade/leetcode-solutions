class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        a = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        def backtrack(cur,idx):
            if len(cur) == len(digits):
                ans.append(cur)
                return
            l = a[digits[idx]]
            for i in l:
                backtrack(cur+i,idx+1)
            
        if digits and digits[0] >= '2':
            backtrack("",0)
        return ans
        
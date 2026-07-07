class Solution(object):
    def paths(self,i,j):
        if i == self.m-1 and j == self.n-1:
            return 1
        if i>= self.m or j >= self.n:
            return 0
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        self.dp[i][j] = self.paths(i+1,j)+self.paths(i,j+1)
        return self.dp[i][j]
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.m = m
        self.n = n
        self.dp = [[-1]*n for i in range(m)]
        return self.paths(0,0)
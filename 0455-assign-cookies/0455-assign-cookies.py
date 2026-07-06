class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0#child
        j = 0#cookies
        count = 0
        g_size = len(g)
        s_size = len(s)
        while i < g_size and j < s_size:
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count
        
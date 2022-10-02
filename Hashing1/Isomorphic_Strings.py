class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        visited = set()
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in visited:
                    return False
                d[s[i]] = t[i]
                visited.add(t[i])
            else:
                if d[s[i]] != t[i]:
                    return False
        return True
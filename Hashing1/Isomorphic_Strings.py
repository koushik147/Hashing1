#TimeComplexity: O(n)
#SpaceComplexity: O(n)
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {} # creating the dictionary
        visited = set() # creating the set
        for i in range(len(s)):
            if s[i] not in d: # if not in dictionary
                if t[i] in visited: # if ith value in visited
                    return False
                d[s[i]] = t[i] # adding value to dictionary
                visited.add(t[i]) # adding the ith value in set
            else:
                if d[s[i]] != t[i]: # if value in dictionary is not equal to ith value in t
                    return False
        return True

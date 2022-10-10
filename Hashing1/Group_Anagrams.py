class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={} # creating dictionary
        res = [] # craeting resultant array
        for i in strs:
            key = sorted(i) # sorting the values and store 
            key = "".join(key) # joining the sorted value
            if key not in d:
                d[key] = [str(i)] # storing in dictionary
            else:
                d[key].append(str(i)) # appending string value of i
        for k,v in d.items():
            res.append(v) # appending the value in result array
        return res
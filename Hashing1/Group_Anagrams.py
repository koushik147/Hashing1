class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        res = []
        for i in strs:
            key = sorted(i)
            key = "".join(key)
            if key not in d:
                d[key] = [str(i)]
            else:
                d[key].append(str(i))
        for k,v in d.items():
            res.append(v)
        return res
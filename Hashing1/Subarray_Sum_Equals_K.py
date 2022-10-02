class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Rsum_hash = {0:1}
        count=0
        Rsum=0
        for i in range(len(nums)):
            Rsum += nums[i]
            temp = Rsum - k
            if temp in Rsum_hash:
                count += Rsum_hash[temp]
            if Rsum in Rsum_hash:
                Rsum_hash[Rsum] += 1
            else:
                Rsum_hash[Rsum] = 1
        return count
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Rsum_hash = {0:1} # creating rsum hashmap 
        count=0
        Rsum=0
        for i in range(len(nums)):
            Rsum += nums[i] # calculating rsum
            temp = Rsum - k # calculating temp by subtracting k from rsum
            if temp in Rsum_hash:
                count += Rsum_hash[temp] # adding count with rsum
            if Rsum in Rsum_hash:
                Rsum_hash[Rsum] += 1 # adding rsum value in hashmap
            else:
                Rsum_hash[Rsum] = 1 # assigning rsum value in hashmap
        return count # returning count
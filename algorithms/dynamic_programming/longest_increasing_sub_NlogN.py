'''
1.initial sub = [ ].
2. traversing the nums:
    a) if val > sub's all elements, then subsequence length increased by 1, sub.append(val);
    b) if sub[i-1] < val < sub[i], then we find a smaller value, update sub[i] = val. Some of the elements stored in the sub[ ] are known subsequences, and the other part is elements of other possible new subsequences. However, the length of the known subsequences is unchanged.
3.return the sub[ ]'s length.

'''

#Because of sub[ ] is incremental, we can use a binary search to find the correct insertion position.
# O(nlogn) solution with binary search
def lengthOfLIS(self, nums):

        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo
        
        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)
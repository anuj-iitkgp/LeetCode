class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        max_ele = max(nums)
        min_ele = min(nums)
        
        max_ele_idx = nums.index(max_ele)
        min_ele_idx = nums.index(min_ele)

        # both element deleting from front
        cnt1 = max(max_ele_idx, min_ele_idx) + 1

        # both element deleting from back
        cnt2 = max(n - max_ele_idx, n - min_ele_idx )

        # delete from the front to remove one element and delete from back to remove other element
        cnt3 = min((max_ele_idx + 1) + (n - min_ele_idx), (min_ele_idx + 1) + (n - max_ele_idx))

        return min(cnt1, cnt2, cnt3)


        
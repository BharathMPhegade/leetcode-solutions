class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            # Calculate the sum of elements on the right
            right_sum = total_sum - left_sum - nums[i]

            # Check if left and right sums are equal
            if left_sum == right_sum:
                return i

            # Add current element to left_sum
            left_sum += nums[i]

        # If no pivot index is found
        return -1
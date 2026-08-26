class Solution(object):

    def plusOne(self, digits):

        for i in range(len(digits) - 1, -1, -1):

            # If the digit is less than 9
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If the digit is 9, make it 0
            digits[i] = 0

        # If all digits were 9, for example [9,9] → [1,0,0]
        return [1] + digits
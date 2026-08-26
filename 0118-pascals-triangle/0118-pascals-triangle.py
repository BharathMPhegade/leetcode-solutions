class Solution(object):

    def generate(self, numRows):

        result = []

        for i in range(numRows):

            # Create a row with all 1s
            row = [1] * (i + 1)

            # Calculate the middle elements
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            # Add the row to the result
            result.append(row)

        return result
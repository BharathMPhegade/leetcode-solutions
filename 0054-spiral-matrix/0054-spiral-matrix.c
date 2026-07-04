/**
 * Note: The returned array must be malloced.
 */

int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize)
{
    int rows = matrixSize;
    int cols = matrixColSize[0];

    int *ans = (int *)malloc(rows * cols * sizeof(int));
    int k = 0;

    int top = 0;
    int bottom = rows - 1;
    int left = 0;
    int right = cols - 1;

    while (top <= bottom && left <= right)
    {
        // Left -> Right
        for (int j = left; j <= right; j++)
            ans[k++] = matrix[top][j];
        top++;

        // Top -> Bottom
        for (int i = top; i <= bottom; i++)
            ans[k++] = matrix[i][right];
        right--;

        // Right -> Left
        if (top <= bottom)
        {
            for (int j = right; j >= left; j--)
                ans[k++] = matrix[bottom][j];
            bottom--;
        }

        // Bottom -> Top
        if (left <= right)
        {
            for (int i = bottom; i >= top; i--)
                ans[k++] = matrix[i][left];
            left++;
        }
    }

    *returnSize = k;
    return ans;
}
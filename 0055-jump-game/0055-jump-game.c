bool canJump(int* nums, int numsSize) {
    int maxReach = 0;  // farthest index we can reach
    
    for (int i = 0; i < numsSize; i++) {
        if (i > maxReach) {
            return false;  // stuck, can't reach this index
        }
        if (i + nums[i] > maxReach) {
            maxReach = i + nums[i];  // update farthest reach
        }
        if (maxReach >= numsSize - 1) {
            return true;  // can reach or surpass the last index
        }
    }
    
    return false;
}
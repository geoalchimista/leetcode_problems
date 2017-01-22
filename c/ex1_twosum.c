/*
https://leetcode.com/problems/two-sum/

1. Two Sum

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above
updated description carefully.
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target) {
    /* nums: a pointer to the array
       numsSize: size of the array
       target: the target number
    */
    int i, j;
    int* returnIndex;
    returnIndex = malloc(2 * sizeof(int));
    
    for (i = 0; i < numsSize; i++) {
        for (j = i + 1; j < numsSize; j++) {
            if (*(nums + i) + *(nums + j) == target) {
                *returnIndex = i;
                *(returnIndex + 1) = j;
                return returnIndex;
            }
        }
    }
    
    return returnIndex;
}

/* This is a brute-force implementation
   time complexity O(n^2)
   space complexity O(1) */



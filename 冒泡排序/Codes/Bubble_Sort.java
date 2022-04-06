package com.Bubble_Sort;

import java.util.Arrays;

public class Bubble_Sort {
    public static void main(String[] args) {
        int[] nums = {1, 2, 8, 5, 3, 4, 7};
        bubbleSort(nums);
        System.out.println(Arrays.toString(nums));
    }

    private static void bubbleSort(int[] nums) {
        boolean b = true;
        for (int i = 0, len = nums.length; i < len - 1 && b; ++i) {
            b = false;
//            System.out.println(i);
            for (int j = 0; j < len - i - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    int n = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = n;
                    b = true;
                }
            }
        }
    }
}

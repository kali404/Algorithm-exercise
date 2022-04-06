### 插入排序

插入排序(InsertionSort)，一般也被称为直接插入排序。

对于少量元素的排序，它是一个有效的算法。插入排序是一种最简单的排序方法，它的基本思想是将一个记录插入到已经排好序的有序表中，从而一个新的、记录数增 1 的有序表。在其实现过程使用双层循环，外层循环对除了第一个元素之外的所有元素，内层循环对当前元素前面有序表进行待插入位置查找，并进行移动。

插入排序的平均时间复杂度也是 **O(n^2)**，空间复杂度为常数阶 **O(1)**，具体时间复杂度和数组的有序性也是有关联的。插入排序中，当待排序数组是有序时，是最优的情况，只需当前数跟前一个数比较一下就可以了，这时一共需要比较 **N-1** 次，时间复杂度为 **O(N)**。最坏的情况是待排序数组是逆序的，此时需要比较次数最多，最坏的情况是 **O(n^2)**。

![img](README.assets/insertionSort-9226505.gif)

#### java

```java
package com.Insertion_Sort;


import java.util.Arrays;

public class Insertion_Sort {
    public static void main(String[] args) {
        int[] nums = {1, 2, 7, 9, 5, 8};
        insertionSort(nums);
        System.out.println(Arrays.toString(nums));
    }

    private static void insertionSort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            int tmp = nums[i];
            int j = i - 1;
            while (j >= 0 && tmp < nums[j]) {
                nums[j + 1] = nums[j];
                j--;
            }
            nums[j + 1] = tmp;
        }
    }
}

```

#### python

```python
nums = [1, 2, 7, 9, 5, 8]


def insertion_sort(nums: list):
    n = len(nums)
    for i in range(1, n):
        m = nums[i]
        j = i - 1
        while j >= 0 and m < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = m


if __name__ == '__main__':
    insertion_sort(nums)
    print(nums)

```

#### C#

```c#
```


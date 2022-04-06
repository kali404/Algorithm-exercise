## 冒泡排序

> 冒泡排序的英文**Bubble Sort**，是一种最基础的**交换排序**。之所以叫做冒泡排序，因为每一个元素都可以像小气泡一样，根据自身大小一点一点向数组的一侧移动。

#### 冒泡排序的原理：
每一趟只能确定将一个数归位。即第一趟只能确定将末位上的数归位，第二趟只能将倒数第 2 位上的数归位，依次类推下去。如果有 n 个数进行排序，只需将 n-1 个数归位，也就是要进行 n-1 趟操作。
而 “每一趟 ” 都需要从第一位开始进行相邻的两个数的比较，将较大的数放后面，比较完毕之后向后挪一位继续比较下面两个相邻的两个数大小关系，重复此步骤，直到最后一个还没归位的数。

![在这里插入图片描述](README.assets/20210611113132421-9138595-9138598.gif)

#### Java

```java
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
```

#### Python

```python
nums = [1, 2, 8, 5, 3, 4, 7]


def bubblesort(nums: list):
    n = len(nums)
    b = True
    for i in range(n - 1):
        if b:
            b = False
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    b = True


bubblesort(nums)
print(nums)
```

#### C#

```c#
using System;

namespace AlgorithmExercise
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] nums = { 1, 2, 8, 5, 3, 4, 7 };
            bubbleSourt(nums);
            foreach (int item in nums)
            {
                Console.WriteLine(item.ToString());
            }
            Console.ReadKey();
        }
        public static void bubbleSourt(int[] nums)
        {
            bool B = true;
            int len = nums.Length; 
            for (int i = 0; i < len -1 && B; i++)
            {
                B = false;
                for (int j =0;j<len-i-1; j++)
                {
                    if (nums[j] > nums[j + 1])
                    {
                        int temp = nums[j];
                        nums[j] = nums[j+1];
                        nums[j+1] = temp;
                        B = true;
                    }
                }
            }
        }
    }
}

```


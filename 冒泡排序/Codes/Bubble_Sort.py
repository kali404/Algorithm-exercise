nums = [1, 2, 8, 5, 3, 4, 7]


def bubblesort(nums: list):
    n = len(nums)
    b = True
    for i in range(n - 1):
        if b:
            b = False
            print(i)
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    b = True


bubblesort(nums)
print(nums)

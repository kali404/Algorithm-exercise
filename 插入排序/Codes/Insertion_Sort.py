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

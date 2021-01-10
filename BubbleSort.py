
def BubbleSort(nums):
    length = len(nums)
    for rows in range(length-1,-1,-1):
        for idx in range(rows):
            if nums[idx]> nums[idx+1]:
                nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
        times = length - rows
        print(f'第{times}次排序後結果為：{nums}')
    print(f'排序後結果為：{nums}')


if __name__ == '__main__':
    n = list(map(int, input('（氣泡排序）初始值為：').rstrip().split()))
    BubbleSort(n)
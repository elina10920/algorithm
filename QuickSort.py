
def QuickSort(nums, left, right):
    if left >= right:
        return
    i = left
    j = right
    key = nums[left] #假設k值為左邊第一個
    while i!=j:
        while nums[j] > key and i < j: #找出比基準小的值
            j-=1
        while nums[i] <= key and i < j: #找出比基準大的值
            i+=1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[left] = nums[j]
    nums[j] = key
    QuickSort(nums, left, j-1)
    QuickSort(nums, j+1, right)

if __name__ == '__main__':
    n = list(map(int, input('（快速排序）初始值為：').rstrip().split()))
    QuickSort(n, 0, len(n)-1)
    print(n)
# 冒泡排序
# [9,4,6,2,1,3,4] 6
def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数 6
        for j in range(len(nums) - i - 1):  # j为列表下标 6
            if nums[j] > nums[j + 1]:
                t=(nums[j + 1], nums[j])
                nums[j]=t[0]
                nums[j + 1] = t[1]
                # 交换
                # nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums      
print(bubble_sort([9,5,6,8,1,3,2]))


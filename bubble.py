def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
nums=[5,7,2,9,1,8]
sort(nums)
print(nums)

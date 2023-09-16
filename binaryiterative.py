def binary(array,target):
    low=0
    high=len(array)-1
    while low<=high:
        mid=(low+high)//2
        mid_value=array[mid]
        if mid_value==target:
            return  mid
        elif mid_value<target:
            low=mid+1
        else:
            high=mid-1
    return -1
sortedarray=[2,4,7,9,11,14,18,22]
target=22
result=binary(sortedarray,target)
if result!=-1:
    print("element",target,"found at index",result)
else:
    print("element",target,"not found at index")
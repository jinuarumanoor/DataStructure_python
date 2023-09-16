def binaryrecursive(array,target,low,high):
    if low>high:
        return  -1

    mid=(low+high)//2
    mid_value=array[mid]
    if mid_value==target:
        return mid
    elif mid_value<target:
        return binaryrecursive(array,target,low+1,high)
    else:
        return  binaryrecursive(array,target,low,high-1)

sortedarray=[2,5,8,11,13,15,17]
target=17
result=binaryrecursive(sortedarray,target,0,len(sortedarray)-1)
if result!=-1:
    print("elemnets",target,"found at index",result)
else:
    print("elements",target,"not found at index")
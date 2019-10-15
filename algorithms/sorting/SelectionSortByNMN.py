def selection_sort(nums):
    for i in range(len(nums)):
        index=i
        for j in range(i+1,len(nums),1):
            if nums[j]<nums[index]:
                index=j
        if index!=i:
            swap(nums,index,i)
    return nums
def swap(nums,j,i):
    temp=nums[i]
    nums[i]=nums[j]
    nums[j]=temp
nums=[]
n=int(input("enter how many numbers:"))
print("enter numbers to be sorted:")
for i in range(n):
    num=int(input())
    nums.append(num)
print(selection_sort(nums))

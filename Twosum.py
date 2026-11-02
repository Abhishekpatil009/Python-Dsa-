
# # Taking input from user
# n = int(input("Enter array size: "))
# nums = list(map(int, input("Enter array elements: ").split()))
# target = int(input("Enter target: "))

# def twosums(nums, target):

#     freq = {}

#     for i in range(len(nums)):

#         # Calculate the remaining number
#         remaining = target - nums[i]

#         # Check if remaining number exists in dictionary
#         if remaining in freq:
#             return [freq[remaining], i]

#         # Store number as key and index as value
#         freq[nums[i]] = i

#     return []

# # Call the function
# result = twosums(nums, target)

# print("Answer:", result)






nums=[5, 9, 1, 2, 4, 15, 18, 6 ,3]
target=13

def twosums(nums,target):
    n=len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []




print(twosums(nums,target))


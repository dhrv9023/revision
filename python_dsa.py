# VALID ANAGRAM

# def is_anagram(strs,txts):
#     return sorted(strs)==sorted(txts)

# print(is_anagram("anagram","aagarmn"))


# 2 SUM

# def two_sum(nums,target):
#     hshmpp={}
#     for index,value in enumerate(nums):
#         diff= target-value
#         if diff in hshmpp:
#             return {hshmpp[diff],index}
#         hshmpp[value]=index
    
# nums=[2,7,11,15]
# target = 9
# print(two_sum(nums,target))    

#MAXIMUM SUBARRAY

# def sbarr(nums):
#     mxsub=nums[0]
#     cursum=0
#     for i in nums:
#         if cursum < 0:
#             cursum=0
#         cursum+=i
#         mxsub=max(mxsub,cursum)
#     return mxsub    



# nums=[-2,1,-3,4,-1,2,1,-5,4]
# print(sbarr(nums))


#CONTINS DUPLICATE

# def dup(nums):
#     hsset=set()
#     for i in nums:
#         if i in hsset:
#             return True
#         hsset.add(i)
#     return False    


# nums = [1,2,3,6]    
# print(dup(nums))


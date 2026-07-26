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
# print(f"the index of the {target} is ",end=' ')
# print(two_sum(nums,target))    



#contains duplicate

# def dup(nums):
#     hshm=set()
#     for i in nums:
#         if i in hshm:
#             return True
#         hshm.add(i)
#     return False    


# nums=[1,2,3,5,4] 
# print(dup(nums))   


#maxsubarray sum

# def sm(nums):
#     currsum=0
#     maxsm=nums[0]
#     for i in nums:
#         if currsum<0:
#             currsum=0
#         currsum=currsum+i
#         maxsm=max(currsum,maxsm)
#     return maxsm
        
# nums=[-2,1,-3,4,-1,2,1,-5,4]
# print(sm(nums))   
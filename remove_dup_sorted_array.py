# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).



[0,0,1,1,1,2]


def removeDuplicates(nums):

	i = 0

	while i < len(nums)-1:

		if nums[i] == nums[i+1]:

			nums.pop(i+1)

		else:
			
			i += 1

	return nums



print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

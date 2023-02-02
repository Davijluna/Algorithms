def find_duplicate(nums):
    for index in nums:
        if not nums[index] or nums[index] <= 1:
            return False
    return False

"""
Careful edge-case handling (carry-over digits)

"""

nums = [9,9]

left = len(nums)-1

while left >= 0:

    if nums[left]==9:

        nums[left]=0

        left -= 1

    else:

        nums[left]+=1

        break

    if left<0:

        nums.insert(0,1)

print(nums)

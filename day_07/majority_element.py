nums = [2,2,1,1,1,2,2]

n = len(nums)

for  i in nums:

    if nums.count(i)>n/2:

        print(i)

        break   


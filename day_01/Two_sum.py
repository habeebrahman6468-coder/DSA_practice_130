"""

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

"""
#METHOD_1

lst = [3,2,4]

lst.sort()

target =9

first = 0

last = len(lst)-1

while (first<last):

    current_sum = lst[first] + lst[last]

    if current_sum == target and lst[first]!= lst[last]:

        print(lst[first],lst[last])

        break
    elif current_sum > target :

        last -= 1

    elif current_sum < target:

        first +=1 



#METHOD_2

nums = list(map(int,input("Enter the numbers: ").split(",")))

target = int(input("target : "))

for n in nums:

    difference = target - n
    if difference in nums:

        print("the indices of two number such that the add upto target is",nums.index(n),"and",nums.index(difference))

        break

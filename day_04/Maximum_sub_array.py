numbers = [-2,1,-3,4,-1,2,1]

max_sum = numbers[0]

for i in range (0,len(numbers)):

    for j in range(i,len(numbers)):

        current_sum = sum(numbers[i:j+1])

        if current_sum > max_sum:

            max_sum = current_sum

print(max_sum)            

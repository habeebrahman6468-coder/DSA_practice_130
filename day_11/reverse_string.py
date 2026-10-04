w = ["h","e","l","l","o"]

left = 0

right = len(w)-1

while (left<right):

    w[left],w[right] = w[right], w[left] 

    left+=1

    right -=1

print(w)    
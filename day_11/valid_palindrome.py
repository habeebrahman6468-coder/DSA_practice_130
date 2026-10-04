w =input("Enter the string: ")

words_str =""

for ch in w.lower():

    if ch.isalnum():

        words_str += ch

left = 0

right = len(words_str) -1

while(left<right):

    if words_str[left] != words_str[right]:

        print(False)

        break

    else:

        left +=1
        right-=1

else: print(True)        
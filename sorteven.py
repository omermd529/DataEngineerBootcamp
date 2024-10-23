#Write a Python program that uses a for loop to iterate through a list of numbers 
# and create a new list containing only the even numbers.

num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

new_num=[]

for i in num:
    if i % 2 == 0:
        new_num.append(i)
        
print(f"The even numbers are " , new_num)
        
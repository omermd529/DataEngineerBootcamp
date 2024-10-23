#Write a Python program to count the frequency of each element in a list using a for loop.

my_list=[1,1,1,1,2,2,2,3,3,4,4,5,5,5,5,5,5,5,5,6,6,7,7,8,8,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,130723,130723]


frequency={}

for num in my_list:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1


      
for key,value in frequency.items():
    print(f"number {key} occurs {value} times.")
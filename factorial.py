#Write a Python program using a for loop to find the factorial of a number.
num=int(input("Enter the number for factorial: "))

factorial=1

for i in range(1,num+1):
    factorial *= i
    
print(f"The factorial of {num} is {factorial}")
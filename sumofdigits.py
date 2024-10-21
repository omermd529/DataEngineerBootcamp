#Write a Python program using a for loop to find the sum of digits of a given number.

num=input("Enter the number: ")
new_num = 0
for digit in num:
    new_num += int(digit)

print(f"The sum of digits is {new_num}")




#Write a Python program using a for loop to print all prime numbers between 10 and 100.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+ 1):
        if num % i == 0:
            return False
    return True

for number in range(10,101):
    if is_prime(number):
        print(f"{number} is a  prime number ")
        
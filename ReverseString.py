#Write a Python program to reverse a string using a for loop.
word="kuch kuch hota hai"

reve_word=""
for i in range(len(word)-1,-1,-1):
    reve_word += word[i]

print(f"The reversed string is {reve_word}")
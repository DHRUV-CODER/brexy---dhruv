import random

num = int(input("Enter the number of random no.s you want:- "))
max = int(input(("Enter the maximum value of Random no.s:- ")))
print(num,"random numbers between 0 to",max)
for i in range(num):
    print(random.randint(0, max))

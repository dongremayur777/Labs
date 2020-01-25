import random
a=(random.choice([1,2,3,4,5,6,7,8,9]))
b=int(input("Enter the Numer which u think can be"))
print(a)
if(a>b):
    print("Too Low!!")
elif(a==b):
    print("Accurate!!")
else:
    print("Too High!!!")
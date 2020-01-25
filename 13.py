x=input("Enter any String:-")
a=0
b=0
for i in x:
    if(i.isalpha()):
        a+=1
    if(i.isdigit()):
        b+=1
        
        
print("Letters are-",a)
print("Digits are-",b)
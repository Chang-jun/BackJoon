## 2439 별찍기-2 ##

a = int(input())

for i in range(1,a+1):
    for j in range(1,a+1 - i):
        print(" ",end ='')
    for k in range(1,i+1):
        print("*",end ='')
    print()



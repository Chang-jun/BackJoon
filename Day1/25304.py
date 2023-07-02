## 영수증 ##

pay = int(input())
product = int(input())

for i in range(1,product+1):
    p1, p2 = map(int,input().split())
    pay -= p1*p2

if(pay == 0): print("Yes")
else: print("No")
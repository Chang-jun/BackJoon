##10813번 공 바꾸기##

basket, change = map(int, input().split())

arr = [0] * basket

for i in range(basket):
    arr[i] = i+1

for i in range(change):
    a, b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

for i in range(basket):
    print(arr[i],end=" ")


## 최소,최대 ##

n = int(input())

n_list = list(map(int, input().split()))

big_num = n_list[0]
small_num = n_list[0]
for i in range(1, len(n_list)):
    if big_num < n_list[i]:
        big_num = n_list[i]
    if small_num > n_list[i]:
        small_num = n_list[i]

print(small_num, big_num)

## X보다 작은 수 ##

num_count ,compare_num = map(int,input().split())
n_list = list(map(int, input().split()))

for i in range(1,len(n_list)+1):
    if(n_list[i-1] < compare_num):
        print(n_list[i-1],end =' ')
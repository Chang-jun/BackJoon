num = [0] * 9

for i in range(9):
    num[i] = int(input())

max_value = num[0]
locate = 1

for i in range(9):
    if max_value < num[i]:
        max_value = num[i]
        locate = i +1

print(max_value)
print(locate)

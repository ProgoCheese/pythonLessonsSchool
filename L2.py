user_list = input().split()
user_list.sort()
check = ''
ans = ''
for i in range(len(user_list)):
    if user_list[i] != check:
        ans = ans + user_list[i] + ' '
        check = user_list[i]

print(ans)

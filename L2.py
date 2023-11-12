user_list = input().split()
user_list.sort()
check = ''
ans = ''
for i in range(len(user_list)):
    if user_list[i] == check:
        ans=ans+' '+ check
    else:
        check = user_list[i]
print(ans)
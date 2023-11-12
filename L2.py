user_list = input().split()
user_list.sort()
check = ''
ans = ''
for i in range(len(user_list)):
    if user_list[i] == check:
        ans=ans+' '+ check
    else:
        check = user_list[i]
#for i in range(len(user_list)):
#    if user_list[i] != check:
#        check = user_list[i]
#        ans=ans+' '+ check
print(ans)
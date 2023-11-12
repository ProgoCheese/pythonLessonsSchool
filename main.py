user_list = input().split()
ans = ""
if len(user_list) >= 2:
    for i in range(len(user_list)-1):
        sum = int(user_list[i-1])+int(user_list[i+1])
        ans = ans +" " + str(sum)
    sum = int(user_list[0])+int(user_list[len(user_list)-2])
    print(ans,sum)
else:
    print(user_list[0])
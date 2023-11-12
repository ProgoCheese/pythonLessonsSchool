number = int(input())
ans = ''
i = 0
is_end = True
while is_end:
    for j in range(i):
        if len(ans)!= number:
            ans = ans + str(i)
        else:
            print(ans)
            is_end = False
            break
    if is_end == False:
        break
    i = i + 1
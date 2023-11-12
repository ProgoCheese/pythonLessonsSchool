number = int(input())
ans = ''
is_end = False
int i = 0
while is_end:
    for j in range(i):
        if len(ans)!= number:
            ans = ans + str(i)
        else:
            print(ans)
            t = True
            break
    if t == True:
        break
    i=i+1
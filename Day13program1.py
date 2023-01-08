inp=input()
temp=inp.split()
ans=[]
for i in temp:
    ans=[len(i) for i in temp]
print(*ans)

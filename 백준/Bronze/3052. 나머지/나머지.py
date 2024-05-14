naMur=[]
for i in range(10):
    num = int(input())
    if num%42 in naMur:
        continue
    else :
        naMur.append(num%42)
print(len(naMur))
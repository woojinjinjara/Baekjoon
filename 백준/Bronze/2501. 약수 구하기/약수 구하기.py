a, b = input().split(" ")
a= int(a)
b= int(b)
yaksu = []
for i in range(1, a+1):
    if a%i==0:
        yaksu.append(i)
if len(yaksu)<b:
    print("0")
else :
    print(yaksu[b-1])
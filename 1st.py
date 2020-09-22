a,b = input().split()
total=[0,0,0]

if len(a)>=len(b):
    p=len(a)
    for i in range(p):
        x=int(a[-1*(i+1)])
        if i<len(b):
            y=int(b[-1*(i+1)])
            x=x+y
        if x>=10:
            x=x-10
        total[-1*(i+1)]=x
else:
    p=len(b)
    for i in range(p):
        x=int(b[-1*(i+1)])
        if i<len(a):
            y=int(a[-1*(i+1)])
            x=x+y
        if x>=10:
            x=x-10
        total[-1*(i+1)]=x
if p==1:
    print(total[2])
elif p==2:
    print(*total[1:], sep="")
else:
    print(*total, sep="")

     
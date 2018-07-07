a=int(raw_input())
b=int(raw_input())
c=[]
d=0
for i in range(a):
    x=int(input())
    c.insert(i,x)
for j in range(b):
    d=d+c[j]
print(d)    

s = 0 ; a = 0 ; n = 0
x = int(input())
m = x
while (x!=-1):
    n = n + 1
    s = s + x
    if m<=x:
        m = m
    else:
        m = x
    x = int(input())
if n==0:
    a = -1 ; m = -1
else:
    a = s/n
print (s,a,m,n)
# it looks like I learned how to use git today
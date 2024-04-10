number = int(input())
n = number
m = number
matrix = [[0 for _ in range(m)] for _ in range(n)]
cnt = 1
turn=0
x=m
y=n
u = 0
d = 1
r = 1
l = 0
up = 0
right = 0
down =0
left =0

def printer():
    print('Round:', turn)
    print('x =', x)
    print('y =', y)
    print('up =', u)
    print('right =', r)
    print('down =', d)
    print('left =', l)
    print('turn =', turn)
  
  
#printer()
while cnt<=m*n:
    if turn%4==0:
        up+=1
        for i in range (x):
            matrix[u][u+i]=up
            cnt+=1
            if i==x-1:
                y-=1
                u+=1
                turn+=1
      #printer()
    if turn%4==1:
        right+=1
        for j in range (y):
            matrix[r+j][-r]=right
            cnt+=1
            if j==y-1:
                x-=1
                r+=1
                turn+=1
      #printer()
    if turn%4==2:
        down+=1
        for k in range (x):
            matrix[-d][-d-1-k]=down
            cnt+=1
            if k==x-1:
                y-=1
                d+=1
                turn+=1
      #printer()
    if turn%4==3:
        left+=1
        for p in range (y):
            matrix[-l-2-p][l]=left
            cnt+=1
            if p==y-1:
                x-=1
                l+=1
                turn+=1
      #printer()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()
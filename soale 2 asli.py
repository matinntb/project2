import numpy as np
n=int(input("Enter number of row:"))
m=int(input("Enter number of column:"))
k=int(input("Enter number of BOMB:"))

if 1<n<100 and 1<m<100 and 0<k<m*n:
    a=np.full((n,m),'0')        #creating array n*m
    
    for x in range(0,k):
        print("BOMBE ",x+1)
        x=int(input("Enter row of BOMB:"))
        y=int(input("Enter column of BOMB:"))
        a[x-1][y-1]='*'         #set star in a[x-1][y-1]

    
        if a[x-2][y-2]!='*':    #Insert corresponding numbers in adjacent cell 
                        f=int(a[x-2][y-2])
                        
                        f+=1
                        str(f)
                        a[x-2][y-2]=f
        if  a[x-2][y]!='*':
                        f=int(a[x-2][y])
                        f+=1
                        str(f)
                        a[x-2][y]=f
        if  a[x-2][y-1]!='*':
                        f=int(a[x-2][y-1])
                        f+=1
                        str(f)
                        a[x-2][y-1]=f

        if  a[x][y-2]!='*':
                        f=int(a[x][y-2])
                        f+=1
                        str(f)
                        a[x][y-2]=f

        if a[x][y-1]!='*':
                        f=int(a[x][y-1])
                        f+=1
                        str(f)
                        a[x][y-1]=f
        if a[x][y]!='*':
                        f=int(a[x][y])
                        f+=1
                        str(f)
                        a[x][y]=f

        if  a[x-1][y-2]!='*':
                        f=int(a[x-1][y-2])
                        f+=1
                        str(f)
                        a[x-1][y-2]=f
        if  a[x-1][y]!='*':
                        f=int(a[x-1][y])
                        f+=1
                        str(f)
                        a[x-1][y]=f
                         
print(a)


##i=1
##while(i<=5):
##    j=i;
##    k=1
##    while(k<=j):
##        print(k,end="")
##        k=k+1
##    print(end="\n")
##    i=i+1

##Question1:
##for i in range(1,6,1):
##    for j in range(1,i+1,1):
##        print(j,end="")
##    print(end="\n")
##
##for i in range(6,1,-1):
##    for j in range(1,i,1):
##        print(j,end="")
##    print(end="\n")

val = 9
for i in range(1,val,2):
    for k in range(1,val-i+1,2):
            print(" ",end=' ')
    for j in range(1,i+1,1):
        print("*",end=' ')
    print()

for i in range(val,1,-2):
    for k in range(val-i+1,1,-2):
            print(" ",end=' ')
    for j in range(i-1,1,-1):
        print("*",end=' ')
    print()

def bubblesort(nlist):
    for num in range(len(nlist)-1,0,-1):
        for i in range(num):
            if nlist[i]>nlist[i+1]:
                nlist[i],nlist[i+1]=nlist[i+1],nlist[i]
                
                
        
nlist=[4,7,3,2,6,7]
bubblesort(nlist)
print(nlist)

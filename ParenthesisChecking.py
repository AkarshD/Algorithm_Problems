def connectedList(grid, i, j, l, visited):
    if i-1>=0:
        print '1',grid[i-1][j],visited[i-1][j]
        if grid[i-1][j]=='1' and visited[i-1][j]==0:
            print '1f'
            t=(i-1,j)
            visited[i-1][j]=1
            l.append(t)
            print l
            l=connectedList(grid,i-1,j,l,visited)

    if i+1<len(grid):
        print '2',grid[i+1][j],visited[i+1][j]
        if grid[i+1][j]=='1' and visited[i+1][j]==0:
            print '2f'
            t=(i+1,j)
            visited[i+1][j]=1
            l.append(t)
            print l
            l=connectedList(grid,i+1,j,l,visited)

    if j-1>=0:
        print '3',grid[i][j-1],visited[i][j-1]
        if grid[i][j-1]=='1' and visited[i][j-1]==0:
            print '3f'
            t=(i,j-1)
            visited[i][j-1]=1
            l.append(t)
            print l
            l=connectedList(grid,i,j-1,l,visited)

    if j+1<len(grid):
        print '4',grid[i][j+1],visited[i][j+1]
        if grid[i][j+1]=='1' and visited[i][j+1]==0:
            print '4f'
            t=(i,j+1)
            visited[i][j+1]=1
            l.append(t)
            print l
            l=connectedList(grid,i,j+1,l,visited)
    return l


def connectedRegion(grid, visited):
    list=[]
    row=len(grid)
    col=len(grid)
    for i in range(row):
        for j in range(col):
            if grid[i][j]=='1' and visited[i][j]==0:
                l=(i,j)
                print l
                list.append(connectedList(grid,i,j,[l],visited))
    print list
    return list

grid1=[['0','0','1'],['0','1','1'],['1','0','0']]
grid2=[['0','0','1'],['0','1','1'],['1','0','1']]
list1=[]
list2=[]
count=0
size=len(grid1)
visited1=[[0]*size]*size
visited2=[[0]*size]*size

list1=connectedRegion(grid1,visited1)
list2=connectedRegion(grid2,visited2)

for i in list1:
    if i in list2:
        #print i
        count+=1
print count

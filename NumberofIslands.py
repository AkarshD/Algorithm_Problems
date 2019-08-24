from Queue import Queue
A=[[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]


class Pos:
    x=0
    y=0

    def __init__(self,i,j):
        x = i
        y = j


def valid(a,b):
    if a>=0 and b>=0 and a<len(A) and b<len(A[0]):
        return True
    return False
    pass


def countIsland(A):
    q = Queue()
    count=0

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]==1:
                count+=1
                print 'in'
                print i
                print j
                q.put(Pos(si,j))
                A[i][j]=0
                while not q.empty():
                    p=q.get()

                    if(valid(p.x - 1,p.y) and A[p.x-1][p.y]==1):
                        q.put(Pos(p.x-1,p.y))
                        A[p.x-1][p.y]=0
                        print p.x-1
                        print p.y

                    if valid(p.x, p.y + 1) and A[p.x][p.y + 1] == 1:
                        q.put(Pos(p.x, p.y + 1))
                        A[p.x][p.y + 1] = 0
                        print p.x
                        print p.y+1

                    if valid(p.x + 1, p.y) and A[p.x + 1][p.y] == 1:
                        q.put(Pos(p.x + 1, p.y))
                        A[p.x + 1][p.y] = 0
                        print p.x+1
                        print p.y

                    if valid(p.x, p.y - 1) and A[p.x][p.y - 1] == 1:
                        q.put(Pos(p.x, p.y - 1))
                        A[p.x][p.y - 1] = 0
                        print p.x
                        print p.y-1

    return count
    pass


c= countIsland(A)
print c
import sys


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1

    while first<=last:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            return  midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return midpoint

s='hackerrank'
queries=[4,1,6,8]
dic={}
ans=[0]*len(s)
sol=[0]*len(queries)
for i in range(len(s)):
    dic[s[i]]=[]
for i in range(len(s)):
    dic[s[i]].append(i)

for i in range(len(s)):
    l=dic[s[i]]
    if len(l)==1:
        ans[i]=-1
    else:
        j=binarySearch(l,i)
        prev=sys.maxint
        next=sys.maxint
        if j-1>=0:
            prev=l[j-1]
        if j+1<=len(l)-1:
            next=l[j+1]
        if(abs(prev-i)==abs(next-i)):
            ans[i]=prev
        else:
            if abs(prev-i)<abs(next-i):
                ans[i]=prev
            else:
                ans[i]=next

for i in range(len(queries)):
    sol[i]=ans[queries[i]]

for i in range(len(queries)):
    print sol[i]
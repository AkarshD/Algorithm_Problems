def checkifPalindrome(ans):
    rev=ans[::-1]
    return rev==ans

def makeChanges(sstr,key):
    i=0
    j=len(sstr)-1
    l=list(sstr)
    while i<=j and key>0:
        if l[i]==l[j]:
            i+=1
            j-=1
            continue
        else:
            l[j]=l[i]
            i+=1
            j-=1
            key-=1
            a=''.join(l)
            if checkifPalindrome(a):
                return 1
            else:
                continue
    return 0

def palindromeChecker(s, l, r, k):
    # Write your code here
    result = ''
    for i in range(len(l)):
        start = l[i]
        end = r[i]
        key = k[i]
        substr = s[start:end+1]
        if checkifPalindrome(substr):
            result += '1'
        else:
            if makeChanges(substr,key):
                result += '1'
            else:
                result += '0'
    return result

s='bcba'
l=[1,2,1]
r=[3,3,1]
k=[2,0,0]
ans =palindromeChecker(s,l,r,k)
print ans
encoded='23511011501782351112179911801562340161171141148'
s=encoded[::-1]
ans=''
size=len(s)
i=0;
while i<size:
    if i+1<size:
        num=s[i:i+2]
        print num
        if ((num>='65' and num<='90') or (num>='97' and num<='99') or num=='32'):
            ans+=chr(int(num))
            i+=2
            print i
        else :
            if i+2<size:
                num=s[i:i+3]
                if (num>='100' and num<='122'):
                    ans+=chr(int(num))
                    i+=3
                    print i
print ans
class TrieNode(object):

    def __init__(self,c):
        self.val = c
        self.children = []
        self.char=''
        self.word_finished = False


def add(root,word,value):
    node = root
    for v in word:
        found_in_child = False
        for child in node.children:
            if child.val == v:
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(v)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True
    if (value=='[newline]'):
        node.char='\n'
    else:
        node.char=value

ans=''

def decode(root,str):
    flag=False
    node = root
    global ans
    if len(str)==0:
        return
    for i in range(len(str)):
        for child in node.children:
            if child.val == str[i]:
                node = child
                break
        if node.word_finished==True:
            ans+=node.char
            s=str[i+1:len(str)]
            decode(root,s)
            break
    return ans

codes=['a 	100100','b	100101','c	110001','d	100000','[newline]	111111','p	111110','q	000001']
encoded='111110000001100100111111100101110001111110'
dic={}
for s in codes:
    l=s.split()
    dic[l[0]]=l[1]

root = TrieNode('r')
for k,v in dic.iteritems():
    add(root,v,k)

print decode(root,encoded)
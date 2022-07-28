import re
def isValid(s):
    a=s.split(".")
    l=[]
    
    total = len(re.findall('[0-9]',s))
    for i in range(0,256):
        l.append(str(i))
        
    if len(a)==4 and total<=12 and total >=4:
     
        for i in a:
            if i not in l:
                return 0
        return 1
    else:
        return 0
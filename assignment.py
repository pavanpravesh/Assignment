import re
y=[]
d={}
with open('input.txt','r') as file:
    for line in file:
        x= re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
        a = ', '.join(x)
        y.append(a)

file.close()        
del y[-1]        
float_lst = [int(z) for z in y]
float_lst.sort()
k=min(float_lst)
with open('input.txt','r') as file1:
    for line1 in file1:
        (key,val) = line1.split('=')
        d[int(val)]=key

print(d[k])        
        











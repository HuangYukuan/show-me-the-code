import re
with open('test.txt','r') as f:
    s=f.read()

matched=re.findall(r'[a-zA-Z]+-?[a-zA-Z]*',s)
print(len(matched))
import re
from collections import Counter
with open('test.txt','r') as f:
    s=f.read()
    f.close()
filter_word=('am','is','are','was','be','s','re','and','at','on','in','to','m','has','have','with','as','a','an','the','of')
matched=re.findall(r'[a-zA-Z]+-?[a-zA-Z]*',s)
counter=Counter(matched)
for i in filter_word:
    del counter[i]
print(counter.most_common(1)[0][0])
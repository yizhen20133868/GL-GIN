dict = {}
with open('dev.txt', 'r') as f:
    txt = f.read()
    txt = txt.split('\n\n')
    print(len(txt))
    for sent in txt:
        sent = sent.strip()
        if not dict.__contains__(sent):
            dict[sent] = 1
        else:
            dict[sent] = dict[sent] + 1
ans = 0
print(len(dict))
for d in dict:
    if dict[d] >1:
        #print(dict[d])
        ans += dict[d] -1
print(ans)



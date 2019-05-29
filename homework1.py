#排除词库



# excludes = ['the','and','to','of','i','a','in','it','that','is',
#             'you','my','with','not','his','this','but','for',
#             'me','s','he','be','as','so','him','your']
excludes = ['']
def getText():
    # f = open('luomio.txt', 'rt')
    f = open('luomio.txt', 'rt', encoding='ascii', errors='replace')
    txt = f.read()
    txt=txt.lower()
    for ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
        txt=txt.replace(ch,' ')
    return txt

hamletTxt=getText()
words=hamletTxt.split()
counts={}
sumcount = 0
for word in words:
    counts[word]=counts.get(word,0)+1
    sumcount = sumcount + 1

counts_ex = counts.copy()
for key in counts.keys():
    if key in excludes:
        counts_ex.pop(key)
items=list(counts_ex.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print('{0:<10}{1:>5}'.format(word,count))

 #将统计结果写入文本文件中
outfile = open('词频统计结果.txt', "w")
lines = []
lines.append('单词种类：'+str(len(items))+'\n')
lines.append('单词总数：'+str(sumcount)+'\n')
lines.append('词频排序如下:\n')
lines.append('word\tcounts\n')

s= ''
for i in range(len(items)):
    s = '\t'.join([str(items[i][0]), str(items[i][1])])
    s += '\n'
    lines.append(s)
print('\n统计完成！\n')
outfile.writelines(lines)
outfile.close()
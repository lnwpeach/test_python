f = open('sample.csv','r')
f2 = open('ss2.csv','w+')
wordlist = []
for line in f:
    wordlist.append(line.split(','))
len_wordlist = len(wordlist)
f2.write(wordlist[0][0]+',')
f2.write(wordlist[0][1])
for i in range(1,len_wordlist):
    if 's' in wordlist[i][0]:
        f2.write(wordlist[i][0]+','+wordlist[i][1])
f2 = open('ss2.csv','r')
print f2.read()
f2.close()

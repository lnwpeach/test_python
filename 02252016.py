file = 'ss.csv'
f = open(file,'w+')
for l in range(5):
    f.write(str(l+1)+', ')
f.write('\n')
for q in range(5):
    for i in range(5):
        f.write(str(q+1)+', ')
    f.write('\n')
for i in range(5):
    f.write(str(i+1)+', ')
f.close
f = open(file,'r')
print (f.read())
f.close()

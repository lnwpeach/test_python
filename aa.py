f = open('ss1.csv','r')
f2 = open('ss2.csv','w+')
f3 = open('ss3.csv','w+')
f4 = open('02262016.py','r')
wl = []
for i in f:
    wl.append(i)
len_wl = len(wl)
for i in range(len_wl):
    f2.write(wl[i])
for i in f4:
    wl.append(i)
len_wl = len(wl)
for i in range(len_wl):
    f3.write(wl[i])
f2 = open('ss2.csv','r')
print f2.read()
f2.close()
f3 = open('ss3.csv','r')
print f3.read()
f3.close()


buyukler=[]
kucukler=[]
for j in mylist:
    if j > 10:
        buyukler.append(j)
    elif j < 10:
        kucukler.append(j)
    elif j == 100:
        print('equals to 100')
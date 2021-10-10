#convert string to the int

buyukler=[]
kucukler=[]
for j in mylist:
    if int(j) > 10:
        buyukler.append(j)
    elif int(j) < 10:
        kucukler.append(j)
    elif int(j) == 100:
        print('equals to 100')

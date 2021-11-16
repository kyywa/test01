import random

#print("proba1")
#print("proba2")
print("Az összeg: "+ str(int(input("Az első szám:"))+(int(input("A második szám:")))))

def average(tlist):
    tmp = 0
    for i in range(0,len(tlist)-1):
        tmp += tlist[i]
    return float(tmp/len(tlist))


numberlist = []
for i in range(0,10):
    numberlist.append(random.randint(0,100))
print(average(numberlist))


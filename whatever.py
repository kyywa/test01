import random

#print("proba1")
#print("proba2")
print("Az összeg: "+ str(int(input("Az első szám:"))+(int(input("A második szám:")))))

def average(tlist):
    tmp = 0
    for i in range(0,len(tlist)-1):
        tmp += tlist[i]
    return float(tmp/len(tlist))

def min_val(tlist):
    tmp = ""
    for i in range(0,len(tlist)-1):
        if tmp == "":
            tmp = tlist[i]
        elif tmp>tlist[i]:
            tmp =  tlist[i] 
    return tmp


numberlist = []
for i in range(0,10):
    numberlist.append(random.randint(0,100))
print(average(numberlist))
print(min_val(numberlist))
print(min(numberlist))
print(max(numberlist))
testb = False
for i in range(0,len(numberlist)-1):
    if numberlist[i] == 9:
        testb = True
if testb == True:
    print("Van benne 9-es")
else:
    print("Nincs benne 9-es")

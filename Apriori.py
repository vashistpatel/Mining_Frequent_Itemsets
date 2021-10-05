import time
from itertools import combinations

baskets_data = [i.strip().split() for i in open('retail.dat.txt','r').readlines()]
baskets_data.pop(0)
# print()
# --------------------------------------------------------------------------------------------------
firstX_rows = 17633
baskets_data = baskets_data[:firstX_rows]
min_support = 0.05
start = time.time()

def rSubset(array, r):
    return list(combinations(array, r))

C1=[] # all unique items in whole data
for i in range(0,firstX_rows):
    for item in baskets_data[i]:
        if not item in C1:
            C1.append(item)
C1 = [x for x in C1]
print(len(C1))
# print(C1)
# print(baskets_data)
# print(items)
# --------------------------------------------------------------------------------------------------
C1_set = [] #convert c1 to array
count_C1 = [] #hold c1 count
items =[] #each and every since item in the db
start = time.time()

for basket in baskets_data:
    for item in basket:
        items.append(item)
for item in C1:
    C1_set.append(item)

for value in (C1_set):
    count_C1.append((value, items.count(value)))

L1 = []
for i in count_C1:
    support = i[1]/len(baskets_data)
    if support >= min_support:
        L1.append(i[0])
C2 = rSubset(L1,2)
count_C2 = {}

for baskets in baskets_data:
    for i in range(0,len(C2)):
        if set(C2[i]).issubset(set(baskets)):
            if C2[i] not in count_C2:
                count_C2[C2[i]] = 1
            else:
                count_C2[C2[i]] += 1
        if C2[i] not in count_C2:
            count_C2[C2[i]] = 0
        else:
            count_C2[C2[i]] += 0
# print(count_C2)

# --------------------------------------------------------------------------------------------------

L2 = []
for i in count_C2:
    support = count_C2[i]/len(baskets_data)
    if support >= min_support:
        L2.append(i)

# --------------------------------------------------------------------------------------------------
#joining
C3 = []
temp = 0
for i in range(0,len(L2)):
    temp = temp+1
    for k in range(i+1,len(L2)):
        for j in range(0,len(L2[0])):
            if (L2[i][0] != L2[k][j]) and (L2[i][1] != L2[k][j]):
                temp2 = L2[i]+(L2[k][j],)
                C3.append(temp2)
            else:
                pass
C3 = set(C3)
# print(len(C3))

C3 = list(C3)
# print(C3)
# --------------------------------------------------------------------------------------------------
L3 = []
for i in range(0,len(C3)):
    C3Pair1 = C3[i][:2]
    C3Pair2 = C3[i][-2:]
    for x in range(0,len(L2)):
        if(C3Pair1 == L2[x]):
            for y in range(0,len(L2)):
                if(C3Pair2 == L2[y]):
                    L3.append(C3[i])
finish = time.time()
elapsed_Time = (finish-start)
print(elapsed_Time)

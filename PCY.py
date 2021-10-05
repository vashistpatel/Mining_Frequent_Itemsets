from itertools import combinations
import time
baskets_data = [i.strip().split() for i in open('retail.dat.txt','r').readlines()]
baskets_data.pop(0)

firstX_rows = 35265
# 88162-1
baskets_data = baskets_data[:firstX_rows]
min_support = 0.01
support_threshold = min_support
cPair = []
C1=[]
def rSubset(array, r):
    return list(combinations(array, r))

def hashFunction(pair1,pair2,length):
#     print(int(pair1))
    return int((int(pair1)*int(pair2))%(round((length*.30))))


for basket in range(0,firstX_rows-1): #find all unique items
    for item in baskets_data[basket]:
        if not item in C1:
            C1.append(item)


print("1")

C1 = [x for x in C1]

C1_set = [] #convert c1 to array
count_C1 = [] #hold c1 count
items =[] #each and every item in the db
start = time.time()
temp = {}
bucket={}
bucketPairs= []
allPairs = rSubset(C1,2)
print("2")
#Pass 1
for basket in baskets_data: #count for each unique item
    for item in basket:
        if item not in temp:
            temp[item] = 1
        else:
            temp[item] += 1
    a = rSubset(basket,2)
    #print(a)
    for pair in a:
        bucketPairs.append(pair)
        #print(pair)
        for i in range(0,len(a)):
            if hashFunction(pair[0],pair[1],len(allPairs)) not in bucket:
                bucket[hashFunction(pair[0],pair[1],len(allPairs))] = 1
            else:
                bucket[hashFunction(pair[0],pair[1],len(allPairs))] += 1

print("3")
#Bit vector map for second pass
for x in bucket.keys():
   #print(x)
    #print(bucket[x])
    if (bucket[x]/len(baskets_data)) > support_threshold:
        #print(bucket[x]/len(baskets_data))
        bucket[x] = 1
    else:
        bucket[x] = 0

#Finding frequentItems list for second pass
frequentItems = []
for x in temp.keys():
    if (temp[x]/firstX_rows)>= min_support:
        frequentItems.append(x)


print("4")


# #Pass 2
bucketPairs = set(bucketPairs)
for x in bucketPairs:
    if x[0] in frequentItems and x[1] in frequentItems:
        if(bucket[hashFunction(x[0],x[1],len(allPairs))])== 1:
            cPair.append(x)
        else:
            pass
    else:
        pass

print("5")

finish = time.time()
elapsed_Time = (finish-start)
print(elapsed_Time)  

import time
from itertools import combinations
def rSubset(array, r):
    return list(combinations(array, r))


arr = [(0,17632),(17633,35264),(35265,52896),(52897,70528),(70529,88160)]



candidateList = [] #Empty list for candidate pairs.
start = time.time()
for i in range(0,len(arr)):
    baskets_data = [i.strip().split() for i in open('retail.dat.txt','r').readlines()]
    baskets_data.pop(0)
    baskets_data_length = len(baskets_data)
    #First to last rows
    firstX_rows = arr[i][0]
    lastX_rows = arr[i][1]
    #Calculate the new support threshold.
    percentage = (lastX_rows-firstX_rows)/baskets_data_length
    #Loading in the data based on the  chunks.
    baskets_data = baskets_data[firstX_rows:lastX_rows]
    #calculate the length of the range
    length = lastX_rows - firstX_rows

    #original min support threshold
    min_support = 0.01
    #new min support threshold
    min_support = percentage*min_support #new min suppot depending on the sample size



    C1=[] # all unique items in whole data
    for i in range(0,length):
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
    candidateList.append(i)

    # --------------------------------------------------------------------------------------------------
#Pass 2
finalCandidateList = []
for i in range(0,5):
    for j in range(0,len(candidateList[i])):
        count = 0
        for k in range(0,5):

            temp = [candidateList[i][j]]
            if (set(temp).issubset(candidateList[k])):
                count += 1
        if count> 1:
            finalCandidateList.append(candidateList[i][j])
finalCandidateList = set(finalCandidateList)
finish = time.time()
elapsed_Time = (finish-start)
print(elapsed_Time)

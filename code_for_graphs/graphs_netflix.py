import matplotlib.pyplot as plt

# Lab 2
y1 = [1948.1765432357788,1950.8111371994019,1153.4314124584198]
y2 = [3791.331921815872,1866.8344616889954,1222.3283212184906]
y3 = [2222.1887233257294,3262.3167989254,1283.3089828491211]
x1 = [50,100,150]
val = ['50','100','150']

plt.plot(x1, y1, label = "50 rows", color="red")
plt.plot(x1, y2, label = "100 rows", color="cyan")
plt.plot(x1, y3, label = "150 rows", color="orange")

plt.title("Lab2 (Apriori algorithm) Netflix Dataset")
plt.ylabel("Time")
plt.xlabel("Thresholds")
plt.xticks(x1,val)
plt.legend()
plt.show()

# Lab 3
y1 = [10800.541291721239,9101.502183171818,7247.219381481912]
y2 = [13410.91318619173,11351.86517315371,10913.18361354131]
y3 = [18439.102386419313131,16712.23716321763181,15910.84327131641236]
x1 = [50,100,150]
val = ['50','100','150']

plt.plot(x1, y1, label = "50 rows", color="red")
plt.plot(x1, y2, label = "100 rows", color="cyan")
plt.plot(x1, y3, label = "150 rows", color="orange")

plt.title("Lab3 (PCY algorithm) Netflix Dataset")
plt.ylabel("Time")
plt.xlabel("Thresholds")
plt.xticks(x1,val)
plt.legend()
plt.show()

# Lab 4
y1 = [2042.6592571735382,2016.9966750144958,2060.386050462723]
y2 = [16.30564284324646,16.30564284324646,14.651922225952148]
# y3 = [9445.581159114838,1429.9989421367645,83.52981090545654]
x1 = [50,100,150]
val = ['50','100','150']

plt.plot(x1, y1, label = "50 rows", color="red")
plt.plot(x1, y2, label = "20 rows", color="cyan")
# plt.plot(x1, y3, label = "150 rows", color="orange")

plt.title("Lab4 (Random Sampling and SON algorithm) Netflix Dataset")
plt.ylabel("Time")
plt.xlabel("Thresholds")
plt.xticks(x1,val)
plt.legend()
plt.show()

# y1 = [8696,9330,9646]
# y2 = [10669,11304,11580]
# x = [1,2,5]
# val = ['1%','2%','5%']

# plt.plot(x, y1, label = "RS 20%", color='red',linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='red', markersize=12)
# plt.plot(x, y2, label = "RS 40%", color='cyan',linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='cyan', markersize=12)

# plt.title("Lab4 (SON algorithm false positives) Retial Dataset")
# plt.xlabel("Thresholds")
# plt.ylabel('false positives')
# plt.xticks(x1,val)
# plt.show()

# # Lab 5
# y1 = [1763.3,757.5660827159882,3040.51283121109]
# y2 = [3863.840511083603,1552.659821987152,1623.2271070480347]
# y3 = [5898.563931941986,5772.881413936615,6042.798104047775]
# x1 = [1,2,5]
# val = ['10','20','50']
#
# plt.plot(x1, y1, label = "50 rows", color="red")
# plt.plot(x1, y2, label = "100 rows", color="cyan")
# plt.plot(x1, y3, label = "150 rows", color="orange")
#
# plt.title("Lab5 (Multihash algorithm) Netflix Dataset")
# plt.ylabel("Time")
# plt.xlabel("Thresholds")
# plt.xticks(x1,val)
# plt.legend()
# plt.show()

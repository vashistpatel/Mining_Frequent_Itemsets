import matplotlib.pyplot as plt

# Lab 2
y1 = [87.85148906707764,43.15798902511597,37.648133754730225]
y2 = [188.72590708732605,96.07246017456055,88.68516802787781]
y3 = [569.5612027645111,297.0979721546173,279.563364982605]
x1 = [1,2,5]
val = ['1%','2%','5%']

plt.plot(x1, y1, label = "20%", color="red")
plt.plot(x1, y2, label = "40%", color="cyan")
plt.plot(x1, y3, label = "100%", color="orange")

plt.title("Lab2 (Apriori algorithm) Retial Dataset")
plt.ylabel("Time")
plt.xlabel("Thresholds")
plt.xticks(x1,val)
plt.legend()
plt.show()

# Lab 3
y1 = [1175.704993724823,2178.8956530094147,4944.136512041092]
y2 = [7201.932584762573,4061.829230070114,5126.223035812378]
y3 = [5829.338021993637,5855.584828138351,5532.798664331436]
x1 = [1,2,5]
val = ['1%','2%','5%']

plt.plot(x1, y1, label = "20%", color="red")
plt.plot(x1, y2, label = "40%", color="cyan")
plt.plot(x1, y3, label = "100%", color="orange")

plt.title("Lab3 (PCY algorithm) Retial Dataset")
plt.ylabel("Time")
plt.xlabel("Thresholds")
plt.xticks(x1,val)
plt.legend()
plt.show()

# Lab 4
y1 = [8756.51905798912,1095.2271716594696,68.42206597328186]
y2 = [18515.274991750717,2289.7488062381744,169.24907326698303]
y3 = [9445.581159114838,1429.9989421367645,83.52981090545654]
x1 = [1,2,5]
val = ['1%','2%','5%']

plt.plot(x1, y1, label = "RS 20%", color="red")
plt.plot(x1, y2, label = "RS 40%", color="cyan")
plt.plot(x1, y3, label = "SON 100%", color="orange")

plt.title("Lab4 (Random Sampling and SON algorithm) Retial Dataset")
plt.ylabel("Time")
plt.xlabel("Thresholds")
plt.xticks(x1,val)
plt.legend()
plt.show()

y1 = [8696,9330,9646]
y2 = [10669,11304,11580]
x = [1,2,5]
val = ['1%','2%','5%']

plt.plot(x, y1, label = "RS 20%", color='red',linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='red', markersize=12)
plt.plot(x, y2, label = "RS 40%", color='cyan',linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='cyan', markersize=12)

plt.title("Lab4 (SON algorithm false positives) Retial Dataset")
plt.xlabel("Thresholds")
plt.ylabel('false positives')
plt.xticks(x1,val)
plt.show()

# Lab 5
y1 = [1763.3,757.5660827159882,3040.51283121109]
y2 = [3863.840511083603,1552.659821987152,1623.2271070480347]
y3 = [5898.563931941986,5772.881413936615,6042.798104047775]
x1 = [1,2,5]
val = ['1%','2%','5%']

plt.plot(x1, y1, label = "20%", color="red")
plt.plot(x1, y2, label = "40%", color="cyan")
plt.plot(x1, y3, label = "100%", color="orange")

plt.title("Lab5 (Multihash algorithm) Retial Dataset")
plt.ylabel("Time")
plt.xlabel("Thresholds")
plt.xticks(x1,val)
plt.legend()
plt.show()

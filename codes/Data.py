import matplotlib.pyplot as plt
X = [29,32,48,50,62,64,72,78,84,95]
Y=[1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5]
plt.figure(figsize=(8, 2))
ax = plt.subplot(8, 1, 6)
plt.xlabel("Observations")
ax = plt.gca()
ax.tick_params(which='major', width=1.00)
ax.tick_params(which='major', length=10)
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=1.05)
plt.xticks(range(28,96))
plt.yticks([])
ax.axes.yaxis.set_visible(False)
ax.set_xlim(28, 96)
ax.set_ylim(0, 10)
ax.set_xticks(ax.get_xticks()[::2])
ax.scatter(X,Y,alpha=0.9,c='blue',edgecolors='none',s=30,label='Observations')
ax.scatter([63],[1.5],alpha=0.9,c='red',edgecolors='none',s=30,label='Median')
plt.legend()
plt.show()
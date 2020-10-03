#---------MATPLOTLIB---------

#Subplots
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(nrows=1, ncols=2)

x = [1,2,3]
y = [1,2,3]
ax[0].plot(x, y, color='r', label='0th axis')
ax[1].plot(x, y, color='g', label='1st axis')
ax[0].set_xlim(1,4)
ax[1].set_xlim(1,4)

fig.legend()
fig.tight_layout()
plt.show()

#Two plot in same plot
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.9,0.9]) #[how much away from left, how amount away from bottom, length, width]
ax2 = fig.add_axes([0.3,0.5,0.3,0.3])
ax1.plot([1,2,3],[1,2,3])
ax2.plot([1,2,3],[1,2,3])
plt.show()

#-------------SEABORN------------

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
plt.rcParams["patch.force_edgecolor"] = True #Declared True so Histogram plots have edge lines

#Distribution Plot
sns.distplot(tips['total_bill'])
plt.show()

#Joint Plot(uses x and y to create 2 types of plots in one)
sns.jointplot(x='total_bill', y='tip', data=tips)
plt.show()

#Pair Plot(uses whole dataset to create all types of plots)
sns.pairplot(tips)
plt.show()

#Bar plot(Can put x as a non-integer num)
sns.barplot(x='sex', y='tip', data=tips)
plt.show()

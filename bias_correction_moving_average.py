import numpy as np
import random
import matplotlib.pyplot as plt
# generate data
random.seed(2)
data_y = [random.random()*100 + 10 for x in range(1,200)]
data_x = [x for x in range(1,200)]


#  exponentially weighted averages (moving average) for ccurve smoothening
beta = 0.9
v = 0
vlist=[]
for i in range(0,len(data_x)):
    v = beta*v + (1-beta)*data_y[i]
    vlist.append(v)
np.array(vlist)
len(data_y)
len(vlist)

data_y[0]
vlist[0]
# bias correction in exponentially weighted averages
beta = 0.8
v = 0
vlist_bias_correction = []
for i in range(0,len(data_x)):
    v = (beta*v + (1-beta)*data_y[i])
    v = v/(1 - (beta ** (i+1)))
    vlist_bias_correction.append(v)
np.array(vlist_bias_correction)
len(vlist_bias_correction)


# orignal lineplot
plt.plot(data_x, data_y, label = "Orignal",color = "green")
plt.xlabel("time")
plt.ylabel("value")
plt.title("Curve smoothening")
# adding exponentially weighted averages to the plot
plt.plot(data_x,vlist, label = "Exponentially weighted average")
# adding bias correction in exponentially weighted averages
plt.plot(data_x,vlist_bias_correction, label = "Bias correction")
plt.legend()
plt.show()
#plt.savefig("plot_momentum.png")

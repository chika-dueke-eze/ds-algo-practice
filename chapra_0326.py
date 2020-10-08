"""
[chapra_0326.py]
[Chika Dueke-Eze]
[10-03-2020]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [cgd19]
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

#%% 
m = [2]
n = [1]

def scaled(val, minval, maxval):
    return (val-minval)/(maxval-minval)

for i in range(10000):
    q=np.random.uniform(0,3)
    if q < 1:
        m.append(m[-1]/2)
        n.append(n[-1]/2)
    elif q < 2:
        m.append(m[-1]/2)
        n.append((300 + n[-1])/2)
    else:
        m.append((300 + m[-1])/2)
        n.append((300 + n[-1])/2)
        
m = np.array(m)  #convert from list to numpy array 
n = np.array(n)       

#%% plot figure 1 
fig, ax = plt.subplots(num=1, clear=True)
for k in range(10000):
    ax.plot(m[k], n[k], '.', 
            color=('blue'))

ax.set(
    xlabel = "m",
    ylabel = "n",
    title = "n vs m -plot 1 (cgd19 )",
) 
fig.savefig('chapra03p26plot1.eps.eps')

#%% plot figure 2 
fig, ax = plt.subplots(num=2, clear=True)
for k in range(10000):
    ax.plot(m[k], n[k], '.', 
            color=(0, 0, scaled(n[k], n.min(), n.max())))
ax.set(
    xlabel = "m",
    ylabel = "n",
    title = "n vs m -plot 2 (cgd19 )",
) 
fig.savefig('chapra03p26plot2.eps.eps')

#%% plot figure 3 
fig, ax = plt.subplots(num=3, clear=True)

for k in range(10000):
    r = np.random.uniform(0, 1)
    g = np.random.uniform(0, 1)
    b = np.random.uniform(0, 1)
    ax.plot(m[k], n[k], '.', 
            color=(r, g, b))
ax.set(
    xlabel = "m",
    ylabel = "n",
    title = "n vs m -plot 3 (cgd19 )",
) 
fig.savefig('chapra03p26plot3.eps.eps')

#%% plot figure 4
fig, ax = plt.subplots(num=4, clear=True)

for k in range(10000):
    r = np.random.uniform(0, 1)
    g = np.random.uniform(0, 1)
    b = np.random.uniform(0, 1)
    if m[k] < 150 and n[k]<150:
        ax.plot(m[k], n[k], '.', 
            color=(0, 1, 0))          #get green coloyr
    elif m[k] < 150 and 150<n[k]<300:
        ax.plot(m[k], n[k], '.', 
            color=(.95, 0.95, .95))    #get greyish color
    elif m[k] > 150 and 150<n[k]<300:
        ax.plot(m[k], n[k], '.', 
            color=(0, 1, 0))
ax.set(
    xlabel = "m",
    ylabel = "n",
    title = "n vs m -plot 4 (cgd19 )",
) 

fig.savefig('chapra03p26plot4.eps.eps')
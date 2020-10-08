"""
[chapra_0227.py]
[Chika Dueke-Eze]
[10-03-2020]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [cgd19]
"""

#%% initialize workspace
import numpy as np
import matplotlib.pyplot as plt

#%% define function
def butterfly(t):
    x = np.sin(t)*(np.exp(np.cos(t)) - 2*np.cos(4*t) - (np.sin(t/12))**5)
    y = np.cos(t)*(np.exp(np.cos(t)) - 2*np.cos(4*t) - (np.sin(t/12))**5)
    
    return x, y
#%% start plots
t = np.linspace(0,100,1600)
x, y = butterfly(t)

fig = plt.figure(num=1, clear=True)
ax1 = fig.add_subplot(2, 2, 1)  #create subplot for 1st row and 1st column
ax2 = fig.add_subplot(2, 2, 2)  #create subplot for 1st row and 2nd column
ax3 = fig.add_subplot(2, 2, 4)  #create subplot for 2nd row and 1st column
 
# plot y as a function of t
ax1.plot(t,y)
ax1.grid(True)
ax1.set(
    xlabel = "t",
    ylabel = "y",
    title = "y as a function of t (cgd19)",
)

# plot y as a function of x
ax2.plot(x,y)
ax2.grid(True)
ax2.set(
    xlabel = "x",
    ylabel = "y",
    title = "y as a function of x (cgd19)",
)

# plot t as a function of x
ax3.plot(x,t)
ax3.grid(True)
ax3.set(
    xlabel = "x",
    ylabel = "t",
    title = "t as a function of x (cgd19)",
)
fig.set_size_inches(8, 8, forward=True)

# Save the graph as EPS and PDF
fig.savefig('chapra02p27plot.eps')

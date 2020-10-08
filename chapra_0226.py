"""
[chapra_0226.py]
[Chika Dueke-Eze]
[10-03-2020]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [cgd19]
"""
#%% Initialize workspace
import numpy as np
import matplotlib.pyplot as plt

#%% get values and set equations
E = 50000
L = 600
I = 30000
w_0 = 2.5

x = np.arange(0,610,10.0)
y1 = (w_0/(120*E*I*L)) * (-x**5 + 2*L**2*x**3 - L**4*x)
y2 = (w_0/(120*E*I*L)) * ((-5*x**4) + (6*L**2)*(x**2) - L**4)
y3 = (E*I) * (w_0/(120*E*I*L)) * (-20*x**3 + 12*L**2*x)
y4 = (E*I) * (w_0/(120*E*I*L)) * (-60*x**2 + 12*L**2)
y5 = (-E*I) * (w_0/(120*E*I*L)) * (-120*x)

#%%start plotting
fig = plt.figure(num=1, clear=True)
ax = fig.subplots(5, 1, sharex=True)

fig.set_size_inches(6, 8, forward=True)


# plot x,y1
ax[0].plot(x,y1)
ax[0].grid(True)
ax[0].set(ylabel = "Displacement (cm)") 

#plot x,y2
ax[1].plot(x,y2)
ax[1].grid(True)
ax[1].set(ylabel = "Slope (cm/cm)")

#plot x,y3
ax[2].plot(x,y3)
ax[2].grid(True)
ax[2].set(ylabel = "Moment (kN-cm)")

#plot x,y4
ax[3].plot(x,y4)
ax[3].grid(True)
ax[3].set(ylabel = "Shear (kN)")

#plot x,y5
ax[4].plot(x,y5)
ax[4].grid(True)
ax[4].set(ylabel = "Distributed Load (kN/cm)")
ax[4].set(xlabel="Distance Along Beam (cm)")

plt.tight_layout()
# Save the graph as EPS and PDF
fig.savefig('chapra02p26plot.eps')
import numpy as np
import math

#get rid of the first 4 lines
import glob 
myfiles = glob.glob('*.dat') 
for file in myfiles: 
    lines = open(file).readlines() 
    open(file, 'w').writelines(lines[3:]) 

#load the three files
data_total=np.genfromtxt('MSD_water_O_traj_total.dat',delimiter='')
data_XY_plane=np.genfromtxt('MSD_water_O_traj_XY.dat',delimiter='')
data_Z_dir=np.genfromtxt('MSD_water_O_traj_Z.dat',delimiter='')

#ploting the three lines
import matplotlib
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

font1 = {'family':'Times New Roman','weight':'normal','size': 9} 

#plot the total MSD
plt.plot(data_total[:,0], data_total[:,1],linestyle='solid', color='green',linewidth=1,label = 'G_W_MXene_W_G_1p_per_W_layer (Total)')
hl=plt.legend(loc='upper left', prop=font1, frameon=False)  
#plot the XY-plane MSD
plt.plot(data_XY_plane[:,0], data_XY_plane[:,1],linestyle='dashed', color='green',linewidth=1,label = 'G_W_MXene_W_G_1p_per_W_layer (XY-plane)')
h2=plt.legend(loc='upper left', prop=font1, frameon=False)  
#plot the Z-dir MSD
plt.plot(data_Z_dir[:,0], data_Z_dir[:,1], linestyle='dotted',color='green',linewidth=1,label = 'G_W_MXene_W_G_1p_per_W_layer (Z-direction)')
h2=plt.legend(loc='upper left', prop=font1, frameon=False)  

plt.xticks(np.arange(0, 21, 1))
plt.yticks(np.arange(-1, 1.5, 0.05))
plt.ylim(-0.01, 0.85)
plt.xlim(0, 15)
#plt.xlim(0, 7)
#plt.ylim(-0.01, 0.35)
plt.xlabel('Time [ps]',font1)
plt.ylabel('MSD [n$\mathregular{m^2}$]',font1)
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300
plt.tick_params(axis="x",direction="in")
plt.tick_params(axis="y",direction="in")
plt.rcParams['xtick.labelsize']=8
plt.rcParams['ytick.labelsize']=8
figgca=plt.gca()
figgca.spines['bottom'].set_linewidth(1.2)
figgca.spines['top'].set_linewidth(1.2)
figgca.spines['left'].set_linewidth(1.2)
figgca.spines['right'].set_linewidth(1.2)
figgca.tick_params(width=1.2)

fig=plt.gcf()
fig.set_size_inches(5, 5)
fig.show()
fig.savefig('Figure1.png', dpi=300)	

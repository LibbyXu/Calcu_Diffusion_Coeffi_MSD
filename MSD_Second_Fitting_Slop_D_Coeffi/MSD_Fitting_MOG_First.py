import numpy as np
import math

start_point=1000 #As of total points num is 15000, you can modify
real_strat=start_point-1 # python start from 0

#load the three files
data_total=np.genfromtxt('MSD_water_O_traj_total.dat',delimiter='')
data_XY_plane=np.genfromtxt('MSD_water_O_traj_XY.dat',delimiter='')
data_Z_dir=np.genfromtxt('MSD_water_O_traj_Z.dat',delimiter='')

len_all=len(data_total[:,0])
#fitting certain points of the whole data
from scipy import optimize

#fitting differnt length obtain different fitting number and R-square
fitting_para=np.zeros(shape=(len_all-start_point,7))
for nn in range(start_point,len_all):
    fitting_para[nn-start_point,0]=data_total[nn,0]

fitting_int=np.zeros(shape=(len_all-start_point,4))
for uu in range(start_point,len_all):
    fitting_int[uu-start_point,0]=data_total[uu,0]
	
############################################
#fitting total data
############################################
def f_total(x, coeff_total,intercept):
    return coeff_total*x+intercept

def fit_total(x_temp,y_temp):
   popt,pcov=optimize.curve_fit(f_total,x_temp,y_temp)
   return popt
   
for i in range(start_point,len_all):
    x_temp=data_total[0:i,0]
    y_temp=data_total[0:i,1]
    te=fit_total(x_temp,y_temp)
    fitting_para[i-start_point,1]=te[0]
    fitting_int[i-start_point,1]=te[1]
    slop_temp=te[0]
    y_inter=te[1]
    residuals=y_temp-f_total(x_temp,slop_temp,y_inter)
    ss_res=np.sum(residuals**2)
    ss_tot=np.sum((y_temp-np.mean(y_temp))**2)
    r_squared_temp = 1 - (ss_res / ss_tot)
    fitting_para[i-start_point,2]=r_squared_temp

############################################
#fitting xy-plane data
############################################
def f_XY_plane(x, coeff_total,intercept):
    return coeff_total*x+intercept

def fit_XY_plane(x_temp,y_temp):
   popt,pcov=optimize.curve_fit(f_XY_plane,x_temp,y_temp)
   return popt
   
for i in range(start_point,len_all):
    x_temp=data_XY_plane[0:i,0]
    y_temp=data_XY_plane[0:i,1]
    te=fit_XY_plane(x_temp,y_temp)
    fitting_para[i-start_point,3]=te[0]
    fitting_int[i-start_point,2]=te[1]
    slop_temp=te[0]
    y_inter=te[1]
    residuals=y_temp-f_XY_plane(x_temp,slop_temp,y_inter)
    ss_res=np.sum(residuals**2)
    ss_tot=np.sum((y_temp-np.mean(y_temp))**2)
    r_squared_temp = 1 - (ss_res / ss_tot)
    fitting_para[i-start_point,4]=r_squared_temp

############################################
#fitting Z-direction data
############################################
def f_Z_dir(x, coeff_total,intercept):
    return coeff_total*x+intercept

def fit_Z_dir(x_temp,y_temp):
   popt,pcov=optimize.curve_fit(f_Z_dir,x_temp,y_temp)
   return popt
   
for i in range(start_point,len_all):
    x_temp=data_Z_dir[0:i,0]
    y_temp=data_Z_dir[0:i,1]
    te=fit_Z_dir(x_temp,y_temp)
    fitting_para[i-start_point,5]=te[0]
    fitting_int[i-start_point,3]=te[1]
    slop_temp=te[0]
    y_inter=te[1]
    residuals=y_temp-f_Z_dir(x_temp,slop_temp,y_inter)
    ss_res=np.sum(residuals**2)
    ss_tot=np.sum((y_temp-np.mean(y_temp))**2)
    r_squared_temp = 1 - (ss_res / ss_tot)
    fitting_para[i-start_point,6]=r_squared_temp

np.savetxt('parameter_slop_R2_total_xy_Z.dat', fitting_para, delimiter = '   ')
np.savetxt('intercept_t_xy_z.dat', fitting_int, delimiter = '   ')

########################################################################
#Plot dMSD(t)/6dt VS t (the dynamic diffusion coefficient vs time) (total data)
########################################################################
import matplotlib
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

font1 = {'family':'Times New Roman','weight':'normal','size': 9} 
#plot the total MSD
plt.plot(fitting_para[:,0], fitting_para[:,1]/6*1000,linestyle='solid', color='green',linewidth=1,label = 'G_W_MXene_W_G_1p_per_W_layer (Total)')
hl=plt.legend(loc='upper right', prop=font1, frameon=False)  
#plot the XY-plane MSD
plt.xticks(np.arange(0, 21, 1))
plt.yticks(np.arange(-1, 40, 1))
plt.ylim(0, 25)
plt.xlim(0, 15)

plt.xlabel('Time [ps]',font1)
plt.ylabel('RDC [$\mathregular{m^2}$/s]',font1) #running diffusion coeeficient
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
fig.savefig('RDC_T_water_O_msd_WHOLE.png', dpi=300)	

#calculate the diffusion coefficient only for total
################################################
#grab all R-square value > 0.8 step out
################################################
aa=0
time_period_pre=np.zeros(shape=(len_all-start_point,7))
for ii in range(0,len_all-start_point):
    if fitting_para[ii,2]>=0.8: #Here, I define, the slop larger than 0.8 will be used, you can modify
        time_period_pre[aa,0:7]=fitting_para[ii,0:7]
        aa=aa+1

time_period_better_pre=time_period_pre[np.all(time_period_pre != 0, axis=1)]
len_right=len(time_period_better_pre[:,0])
time_period_better=np.zeros(shape=(len_right,8))
time_period_better[:,0:7]=time_period_better_pre
time_period_better[:,0]=np.around(time_period_better[:,0]*1000) #Transfer picosecond to fs

#1 fs per step, which is 0.001ps
len_better=len(time_period_better[:,0])
start_time=time_period_better[0,0]
for mm in range(0,len_better):
    time_temp=time_period_better[mm,0]
    if time_temp!=(start_time+mm):
        print("Time step not continues for {} step in line {} in file time_period_better".format(time_temp,mm)) #mm here is python line which start from 0
    time_period_better[mm,7]=time_period_better[mm,0]/1000
        
np.savetxt('better_time_period_total_MSD_0.8.dat', time_period_better, delimiter = '   ')
#the file was saved using the fs as the first column,the last column is the ps


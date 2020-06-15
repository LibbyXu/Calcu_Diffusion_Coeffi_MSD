import numpy as np
import math

###################################
#set_variables 
###################################
#the two time value are the fs in the first column
start_time=1500 #You can modify
end_time=4500  #You can modify
#load the file
data_file=np.genfromtxt('better_time_period_total_MSD_0.8.dat',delimiter='')

################################################
#grab the corresponding period of time
################################################
len_file=len(data_file[:,0])
line_se=[]
for line in range(0,len_file):
    if data_file[line,0]==start_time:
        line_se.append(line)
    if data_file[line,0]==end_time:
        line_se.append(line)
line_se=np.asarray(line_se)

len_new_file=line_se[1]-line_se[0]+1
corr_data=np.zeros(shape=(len_new_file,7))
for row in range(0,len_new_file):
    corr_data[row,:]=data_file[line_se[0]+row,0:7]

np.savetxt('calcu_diffucion_coeff.dat', corr_data, delimiter = '   ')
print('\nFor protons:')

#Total
print('\nTotal:')
mean_slop_total=np.mean(corr_data[:,1]/6*1000)
var=np.std(corr_data[:,1]/6*1000)
print("The averaged slop between the start time: {} fs and the end time: {} fs is {}.".format(start_time,end_time,mean_slop_total))
averaged_diffusion_coeffi_temp_total=mean_slop_total
#transfer (nm^2/ps) to (10**-9 m^2/s)
averaged_diffusion_coeffi_total=averaged_diffusion_coeffi_temp_total  
var_total=var   
#As it is easier to track the proton binded O not the proton
print("The corresponding averaged diffusion coefficient is {}. (unit:10**-9 m^2/s)".format(averaged_diffusion_coeffi_total))
print("The corresponding standard deviation is {}. (unit:10**-9 m^2/s)".format(var_total))
#Remember when plotting the averaged value, please add the error bar
#plotting please use the save script

#xy-plane
print('\nXY-plane:')
mean_slop_xy=np.mean(corr_data[:,3]/4*1000)
var=np.std(corr_data[:,3]/4*1000)
print("The averaged slop between the start time: {} fs and the end time: {} fs is {}.".format(start_time,end_time,mean_slop_xy))
averaged_diffusion_coeffi_temp_xy=mean_slop_xy
var_xy=var
#transfer (nm^2/ps) to (10**-9 m^2/s)
averaged_diffusion_coeffi_xy=averaged_diffusion_coeffi_temp_xy
#As it is easier to track the proton binded O not the proton
print("The corresponding averaged diffusion coefficient is {}. (unit:10**-9 m^2/s)".format(averaged_diffusion_coeffi_xy))
print("The corresponding standard deviation is {}. (unit:10**-9 m^2/s)".format(var_xy))

#Z-dir
print('\nZ-dir:')
mean_slop_z=np.mean(corr_data[:,5]/2*1000)
var=np.std(corr_data[:,5]/2*1000)
print("The averaged slop between the start time: {} fs and the end time: {} fs is {}.".format(start_time,end_time,mean_slop_z))
averaged_diffusion_coeffi_temp_z=mean_slop_z
var_Z=var
#transfer (nm^2/ps) to (10**-9 m^2/s)
averaged_diffusion_coeffi_z=averaged_diffusion_coeffi_temp_z   
#As it is easier to track the proton binded O not the proton
print("The corresponding averaged diffusion coefficient is {}. (unit:10**-9 m^2/s)".format(averaged_diffusion_coeffi_z))
print("The corresponding standard deviation is {}. (unit:10**-9 m^2/s)".format(var_Z))


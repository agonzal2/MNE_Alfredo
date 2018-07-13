# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:26:07 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
import glob
import os
import parameters
from OpenEphys import *
import matplotlib.pyplot as plt
from numpy import *
from initial_processes import *
from power_spectrum import *
import scipy.fftpack
from scipy import signal
from filters import *
import xlrd
prm = parameters.Parameters()


def init_params(): #Defines initial parameters used throughout.
    prm.set_filepath('D:\\ERUK\\tethered Recordings\\ERUK Animals\\180705\\2018-07-05_10-37-59\\')
    prm.set_filename('E17.txt')
    prm.set_excelpath('D:\\ERUK\\tethered Recordings\\ERUK Animals\\180705\\')
    prm.set_excelname('180705_VGATCRE_390.xls')
    prm.set_sampling_rate(1000)
    prm.set_starttime(1036) #using as experiment
    prm.set_endtime(1046)   
    prm.set_starttime2(994) #using as control.
    prm.set_endtime2(1004)
    prm.set_windowtype('hamming')
    prm.set_stimfreq(10)
    
    
        

def main (): #runs stuff.
    
    init_params()
    
#    
init_params()
print(prm.get_filepath())

analysis_times=import_spreadsheet(prm.get_excelpath() + prm.get_excelname())

#events=np.array([[1,2,3], [4,5,6]])
#print(analysis_times)


stim=create_epochs(analysis_times, prm.get_sampling_rate())



#Load Open Ephys Data
data=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'CH', dtype = float, session = '0', source = '100')#######load file
#
#Load Opto Stim Data
data_adc=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'ADC', dtype = float, session = '0', source = '100')#######load file8


#Add Opto Stim Channel to Data
data= np.append(data, (np.zeros((data.shape[0],1), dtype=int64)), axis=1)
data[:,16]=(data_adc[:,1]*1000)


##Stuff to get precise stimulation times.
#stimulations=130 
#test1= data_adc[:,1]*1000
#stim_times=[]
#for range in stimulations:
#    test2=np.where(test1 > -200)
#    test3=np.array(test2)
#    test4=np.where(test3[0] > (test3[0][0]+15000))
#test5=np.array(test4)
#test3=np.where(test2[])
#np.where(test2[0][1])


#plt.plot(data_adc[:,1]*1000)



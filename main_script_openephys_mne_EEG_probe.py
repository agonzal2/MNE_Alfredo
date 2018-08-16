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
    prm.set_filepath('C:\\Users\\agonzal2\\Desktop\\Ingrid\\DATA\\OPEN EPHIS DATA\\S7001_D2_2018-06-21_09-58-00\\')
    prm.set_filename('E17.txt')
    prm.set_excelpath('C:\\Users\\agonzal2\\Desktop\\Ingrid\\DATA\\')
    prm.set_excelname('events.xls')
    prm.set_sampling_rate(1000)
    prm.set_starttime(1036) #using as experiment
    prm.set_endtime(1046)   
    prm.set_starttime2(994) #using as control.
    prm.set_endtime2(1004)
    prm.set_windowtype('hamming')
    prm.set_stimfreq(10)
    
    
        

def main (): #runs stuff.
    
    init_params()
    
    
init_params()
print(prm.get_filepath())


##If you have specific times to analyse, load excel spreadsheet of them below.
#analysis_times=import_spreadsheet(prm.get_excelpath() + prm.get_excelname())



##Creates epoch file. Creates epochs from analysis times.
#stim=create_epochs(analysis_times, prm.get_sampling_rate())



#Load Open Ephys Data
data=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'CH', dtype = float, session = '0', source = '101')#######load file


data_aux=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'AUX', dtype = float, session = '0', source = '101')#######load file8




##Stuff to get precise stimulation times. Ignore this for now.
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



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
    prm.set_filepath('C:\\Users\\agonzal2\\Desktop\\FVBX_Osterweil\\180816\\2018-08-16_16-06-33\\')
    prm.set_filename('E17.txt')
    prm.set_excelpath('D:\\ERUK\\Tethered Recordings\\ERUK Animals\\180814\\')
    prm.set_excelname('180814_Stimulations.xls')
    prm.set_sampling_rate(1000)
    prm.set_starttime(1036) #using as experiment
    prm.set_endtime(1046)   
    prm.set_starttime2(994) #using as control.
    prm.set_endtime2(1004)
    prm.set_windowtype('hamming')
    prm.set_stimfreq(10)
    
    
        

def main (): #runs the entire program, synchronize functions from different scripts.
    
    init_params() # not in use yet
    
# run the initiate parameters
init_params()


##Get the analysis times from spreadsheet.
#analysis_times=import_spreadsheet(prm.get_excelpath() + prm.get_excelname())
#
#
##Creates epoch file.
#stim=create_epochs(analysis_times, prm.get_sampling_rate())



#Load Open Ephys Data
data=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'CH', dtype = float, session = '0', source = '100')#######load file
#
#Load Opto Stim Data
data_adc=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'ADC', dtype = float, session = '0', source = '100')#######load file8


#Add Opto Stim Channel to Data
data= np.append(data, (np.zeros((data.shape[0],1), dtype=int64)), axis=1)
data[:,48]=(data_adc[:,0]*1000)

# After this go to create_MNE_Data.






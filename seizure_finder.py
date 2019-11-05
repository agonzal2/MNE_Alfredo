# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:45:42 2018

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""

from numpy import *
import parameters
import matplotlib.pyplot as plt
prm = parameters.Parameters()
from OpenEphys import *
import mne
import xlrd


"""
Seizure_times function below gets times of seizures by looking at a threshold, of sigmas,
this can then be plotted with MNE epochs to check. 
"""
def seizure_times(channel, mne_data_array, sampling_rate, stdev_thresh):##for use with normal opto
    
    times=[]
    data=mne_data_array.get_data(channel) # Gets data of channel out from array
    data_abs=absolute(data) #Make data absolute.
    stdev_calc=std(data_abs) #Get standard deviation from data.
    print("Standard deviation is " + str(stdev_calc)) #Print what this, on first data set it was 97.
    times=data_abs > (stdev_thresh*stdev_calc)  #Set threshold to see seizures here
    times_list=times.tolist() #Had to make it back from a numpy array into a list in order to test True below
    start_times=[]
    for n in range(len(times_list[0])): 
        if times_list[0][n] == True: #Times list second index is a list of booleans (Trues or falses), this tests that 
            start_times.append(n) #and appends if true
    
    stim_times=[]    
    
    for n in range(len(start_times)):  #Now here we get the exact time from the sampling rate. 
        x=n-1
        if n ==0:
            stim_times.append(start_times[n]/sampling_rate)
        elif start_times[n]-start_times[n-1]>(sampling_rate*1):
            stim_times.append(start_times[n]/sampling_rate)
    
    
    stimulations= asarray(stim_times)
    
    return stimulations
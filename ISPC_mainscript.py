# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:25:05 2020

@author: Alfredo
@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk

This makes the objects for MNE.
"""







import glob
import os

import mne
from OpenEphys import *
from initial_processes import *
from numpy import transpose, angle, mean, abs, average, concatenate
from matplotlib import pyplot as plt
from mne.time_frequency import (tfr_multitaper, tfr_stockwell, tfr_morlet,
                                tfr_array_morlet)
from filters import *
from seizure_finder import *
from power_spectrum import *
from Multi_channel_analysis import *
import parameters
prm = parameters.Parameters()
import xlsxwriter

#global w



def init_params(): #Defines initial parameters used throughout.
    prm.set_filepath('C:\\Users\\Alfredo\\Desktop\\Tethered Recordings\\190911\\2019-09-11_13-26-04\\')
    prm.set_filename('E17.txt')
    prm.set_excelpath('C:\\MNE_Alfredo\\')
    prm.set_excelname('ISPC_Trials_electrodes.xls')
    prm.set_channel_combo_name('ISPC_Trials_electrodes.xls')
    prm.set_sampling_rate(1000)
    prm.set_starttime(1036) #using as experiment
    prm.set_endtime(1046)   
    prm.set_starttime2(994) #using as control.
    prm.set_endtime2(1004)
    prm.set_windowtype('hann')
    prm.set_stimfreq(10)
    prm.set_headstages(4)
    prm.set_stimduration(30)
    

'Initialize the parameters'
init_params()
prm.set_excelpath('C:\\MNE_Alfredo\\')
print(prm.get_excelpath())

'This loads data in numpy to get stim times'
data=load_16channel_opto(prm.get_headstages())
stimulations = actual_stim_times(data,  prm.get_sampling_rate(), prm.get_headstages())  
stim=create_epochs(stimulations, prm.get_sampling_rate()) #Creates stim time array that MNE can read.
channel_combo=import_channel_combo(prm.get_excelpath() + prm.get_channel_combo_name())
del(data)
picks=[0, 14, 6, 8, 10, 64] #a[16, 30, 22, 24, 26, 64]#b [32, 46, 38, 40, 42, 64] #c[48, 62, 54, 56, 58, 64] #d     [48, 62, 54, 56, 58, 64] #d 


'This loads data in MNE to analyze and applies hilbert transform'
custom_raw=load_16_channel_opto_mne(4)

'picks below should be ipsi-inter, ipsi-caud, contra-ros, contra-inter, contra-caud, opto'
custom_raw.apply_hilbert(picks) #Apply hilbert transform.


'This makes epochs to analyze'
baseline_epochs=mne.Epochs(custom_raw, stim, baseline= None, 
       detrend=None, tmin=-30, tmax=0)

stim_epochs=mne.Epochs(custom_raw, stim, baseline= None, 
       detrend=None, tmin=0, tmax=30)


"Extract data to numpy from MNE"
hil_data_baseline=baseline_epochs.get_data(picks) #Produces numpy array from picks.
hil_data_stim=stim_epochs.get_data(picks)


'Up to here have hilbert transformed epochs per channel picks, in array'
custom_raw.close
'Now function to get IPSC per trials over time.'

ext_times_1j_alltrodes_baseline_1st, ext_times_1j_alltrodes_stim_1st = ispc_trials_return_exponential_1j_over_time(hil_data_baseline, hil_data_stim, channel_combo)

'Run for second animal'

'This loads data in numpy to get stim times'
#
#prm.set_filepath('C:\\Users\\Alfredo\\Desktop\\Tethered Recordings\\190607\\2019-06-07_17-44-43\\')
#picks=[16, 30, 22, 24, 26, 64]
#
#data=load_16channel_opto(prm.get_headstages())
#stimulations = actual_stim_times(data,  prm.get_sampling_rate(), prm.get_headstages())  
#stim=create_epochs(stimulations, prm.get_sampling_rate()) #Creates stim time array that MNE can read.
#channel_combo=import_channel_combo(prm.get_excelpath() + prm.get_channel_combo_name())
#del(data)
#
#'This loads data in MNE to analyze and applies hilbert transform'
#custom_raw=load_16_channel_opto_mne(4)
#
#'picks below should be ipsi-inter, ipsi-caud, contra-ros, contra-inter, contra-caud, opto'
#custom_raw.apply_hilbert(picks) #Apply hilbert transform.
#
#
#'This makes epochs to analyze'
#baseline_epochs=mne.Epochs(custom_raw, stim, baseline= None, 
#       detrend=None, tmin=-30, tmax=0)
#
#stim_epochs=mne.Epochs(custom_raw, stim, baseline= None, 
#       detrend=None, tmin=0, tmax=30)
#
#
#"Extract data to numpy from MNE"
#hil_data_baseline=baseline_epochs.get_data(picks) #Produces numpy array from picks.
#hil_data_stim=stim_epochs.get_data(picks)
#
#
#'Up to here have hilbert transformed epochs per channel picks, in array'
#
#'Close to save memory'
#custom_raw.close
#'Now function to get IPSC per trials over time.'
##
#ext_times_1j_alltrodes_baseline_2nd, ext_times_1j_alltrodes_stim_2nd = ispc_trials_return_exponential_1j_over_time(hil_data_baseline, hil_data_stim, channel_combo)
##
##
##
#'concatenate arrays here'
#all_epochs_baseline=concatenate((ext_times_1j_alltrodes_baseline_1st, ext_times_1j_alltrodes_baseline_2nd), axis=0)
#all_epochs_stim=concatenate((ext_times_1j_alltrodes_stim_1st, ext_times_1j_alltrodes_stim_2nd), axis=0)
"Function to average at individual time points and across entire epoch"

abs_avg_baseline, ipsc_metric_baseline, abs_avg_stim, ipsc_metric_stim = calculate_ispc_trials(ext_times_1j_alltrodes_baseline_1st, ext_times_1j_alltrodes_stim_1st)





#baselined=abs_avg_stim-abs_avg_baseline


#plot_all(abs_avg_stim[4,:], prm.get_sampling_rate(),'k')
#plot_all(abs_avg_stim[8,:]-1, prm.get_sampling_rate(),'g')
#plot_all(abs_avg_stim[11,:]-2, prm.get_sampling_rate(),'g')
#plot_all(abs_avg_stim[13,:]-3, prm.get_sampling_rate(),'k')
#plot_all(abs_avg_stim[14,:]-4, prm.get_sampling_rate(),'g')




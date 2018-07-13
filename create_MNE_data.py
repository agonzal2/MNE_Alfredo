# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:54:00 2018

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
import mne
from numpy import transpose


datatp=data.transpose()#Array from openephys has to be trasnposed to match RawArray MNE function to create.
#data comes from openephys.

#set nme parameters
n_channels =17

channel_names=['hpc_mid_deep', 'hpc_mid_sup', 'hpc_ros_deep', 'hpc_ros_sup', 'pfc_deep', 'pfc_sup', 'nothing1', 'nothing2', 'hpc_contra_deep', 'hpc_contra_sup', 'EMG1', 'EMG2', 'cb_deep', 'cb_sup', 'hp_caudal_deep', 'hpc_caudal_sup', 'Opto']
channel_types=['eeg','eeg','eeg','eeg','eeg','eeg','misc','misc','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg','stim']

info = mne.create_info(channel_names, prm.get_sampling_rate(), channel_types)

custom_raw = mne.io.RawArray(datatp, info)

#This below allows to mark bad channels once known.
custom_raw.info['bads']=['nothing1', 'nothing2', 'hpc_ros_deep','EMG1']


###This below adds the epochs to the object.
epochs=mne.Epochs(custom_raw, stim, event_id=[41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59], baseline= None, 
           detrend=None, tmax=10)




###To do a basic plot below

###Dictionary for color of traces:
#colors=dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
#     emg='g', ref_meg='steelblue', misc='k', stim='b',
#     resp='k', chpi='k')
#custom_raw.plot(None, 5, 20, 8,color = colors, scalings = "auto", show_options = "true" )#
###Can put this into raw_plot order=[4, 5, 3, 0, 1, 14, 15, 16]
###If order there it picks which channels to put and in what order



#####To do psd plots of epochs

#epochs.plot_psd(fmin=0., fmax=15, tmin=-10, tmax=10, picks=[14,15])
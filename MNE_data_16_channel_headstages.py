
"""
Created on Tue Jun 26 16:54:00 2018

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk

This makes the objects for MNE.
"""

import glob
import os

import mne
from OpenEphys import *
from initial_processes import *
from numpy import transpose
from matplotlib import pyplot as plt
from mne.time_frequency import (tfr_multitaper, tfr_stockwell, tfr_morlet,
                                tfr_array_morlet)

from power_spectrum import *
import parameters
prm = parameters.Parameters()
import xlsxwriter



def init_params(): #Defines initial parameters used throughout.
    prm.set_filepath('C:\\Users\\sulse\\Desktop\\Tethered Recordings\\180817\\2018-08-17_16-28-14\\')
    prm.set_filename('E17.txt')
    prm.set_excelpath('C:\\Users\\sulse\\Desktop\\Tethered Recordings\\180817\\')
    prm.set_excelname('180817_VGATCRE_390_478_487_10hz.xls')#
    prm.set_sampling_rate(1000)
    prm.set_starttime(1036) #using as experiment
    prm.set_endtime(1046)   
    prm.set_starttime2(994) #using as control.
    prm.set_endtime2(1004)
    prm.set_windowtype('hamming')
    prm.set_stimfreq(10)

'Initialize the parameters'
init_params()

'Function below loads each 16-channel-headstage individually.'
#data=load_16channel_opto_individually(2)


'Function below loads the data in numpy format, no MNE'
#data2=load_16channel_opto(3)

'Function below loads the data and makes the MNE data object, specify how many headstages'

#custom_raw=load_16_channel_opto_mne(3)

'This is to make MNE array of filtered data through MNE filt function.'
#filt=custom_raw.filter(7, 12, fir_design='firwin')
#


'If you have specific times to analyse, load excel spreadsheet of them below.'

analysis_times=import_spreadsheet(prm.get_excelpath() + prm.get_excelname()) #Imports spreadsheet
#stim=create_epochs(analysis_times, prm.get_sampling_rate()) #Creates stim time array that MNE can read.

'This is if brain state epoch array is available'
#analysis_times=import_brain_state(prm.get_excelpath() + prm.get_excelname())

'This is if channel combination array is available for coherence is cross-frequency coupling analyses'
#channel_combo=import_channel_combo(prm.get_excelpath() + prm.get_channel_combo_name())

'This below is a function to get actual stimulation times.'
#stimulations = actual_stim_times(custom_raw,  prm.get_sampling_rate())    


'This outputs the entrainment ratio for one channel'
#multiple_entrainmentratio(analysis_times, data[:, 15])
    

'This outputs theta delta ratio for one channel'
#multiple_theta_delta(analysis_times, data[:, 15])

'This outputs multiple PSD plots for one channel'
#multiple_psds(analysis_times, data[:, 30])





'This below adds the epochs to the object.'
##
#epochs=mne.Epochs(custom_raw, stim, baseline= None, 
#           detrend=None, tmin=-2, tmax=5, )

#epochs=mne.Epochs(custom_raw, stim, event_id=[0], baseline= None, 
          # detrend=None, tmin=-1, tmax=1)

#picks =[14, 15]

'This can average the epochs'
#avgepochs=epochs.average()

'This is to do PSD plots of the epochs'

#epochs.plot_psd(custom_raw, fmin= 1, fmax=15, tmin=-10, tmax=10, picks=[15])

'Dictionary for color of traces'
colors=dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
     emg='g', ref_meg='steelblue', misc='k', stim='b',
     resp='k', chpi='k')

'Creates epoch file. Creates epochs from analysis times.'
#stim=create_brain_state_epochs(analysis_times, prm.get_sampling_rate())

'Functions for evoked plots'
#evoked= epochs.average().pick_types(eeg=True, emg=True)#to average epochs.
#evoked.plot([31], time_unit='s') #to plot these epochs, first array is channel number.
#
#epochs.plot(n_epochs=1, block=True, 
#            scalings= 'auto', picks=[32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,  48]) #block episodes. 


'The following is to create psd plots of epochs'

#epochs.plot_psd( fmin= 0, fmax=15, tmin=-10, tmax=0, picks=[31])

#epochs.plot_image(picks=[31])

'To do a basic plot below. The following can be added for specifc order of channels order=[4, 5, 3, 0, 1, 14, 15, 16]'

#
#custom_raw.plot(None, 5, 20, 8,color = colors, scalings = "auto", order=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,
#                                    14,15,16], show_options = "true" )#
'This is to plot coherence below'
#multiple_coherence(analysis_times, custom_raw)

'The following is to calculate coherence'

#coh_average, coh_std, f= global_coherence(analysis_times, channel_combo, custom_raw)



'The following is to create psd plots of epochs'

#epochs.plot_psd(custom_raw, fmin= 1, fmax=15, tmin=-10, tmax=10, picks=[15])



'Plotting Time frequency representation with DPSS Tapers.'
#
#freqs = np.arange(1., 16., 1.)
#vmin, vmax = 100, 130.  # Define our color limits.
#
#n_cycles = freqs /2.
#time_bandwidth = 2 # Least possible frequency-smoothing (1 taper)
#power = tfr_multitaper(epochs, freqs=freqs, n_cycles=n_cycles,
#                       time_bandwidth=time_bandwidth, return_itc=False, picks=[15])
#
#dir(power)
## Plot results. B,aseline correct based on first 100 ms.
#power.plot([0], vmin=vmin, 
#           vmax=vmax, cmap=('rainbow', 'interactive' ), dB=True)
#
#baseline=(-10., 0), mode='mean', 

'Ploting Time frequency representation with Stockwell (S) transform'
#
#
#fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
#fmin, fmax = freqs[[0, -1]]
#
#for width, ax in zip((0.2, .1, 3.0), axs):
#    power = tfr_stockwell(epochs, fmin=fmin, fmax=fmax, width=width)
#    power.plot(picks=[0], baseline=(-10., 0), mode='mean', axes=ax, show=False,
#               colorbar=False)
#    ax.set_title('Sim: Using S transform, width = {:0.1f}'.format(width))
#plt.tight_layout()

'Plotting TFR with Morlet Waveletes'

#fig, axs = plt.subplots(1,  3, figsize=(15, 5), sharey=True)
#all_n_cycles = [1, freqs/2., 10]
#for n_cycles, ax in zip(all_n_cycles, axs):
#    power = tfr_morlet(epochs, freqs=freqs, n_cycles=n_cycles, zero_mean=True, 
#                       return_itc=False, picks=[14])
#    power.plot( vmin=vmin, vmax=vmax,
#               axes=ax, dB=True, show=False, colorbar=False)#Key was DB as poer of frequencies is very tight.
#    n_cycles = 'scaled by freqs' if not isinstance(n_cycles, int) else n_cycles
#    ax.set_title('Sim: Using Morlet wavelet, n_cycles = %s' % n_cycles)
#plt.tight_layout()














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
from Multi_channel_analysis import *
import parameters
prm = parameters.Parameters()
import xlsxwriter



def init_params(): #Defines initial parameters used throughout.
    prm.set_filepath('C:\\Users\\sulse\\Desktop\\Tethered Recordings\\191019\\2019-10-19_10-59-44\\')#E:\\ERUK\\Tethered Recordings\\ERUK Animals\\180917\\2018-09-17_11-11-58\\
    prm.set_filename('E17.txt')
    prm.set_excelpath('C:\\Users\\sulse\\Desktop\\Ingrid\\CDKL5_October_2018\\S7013\\')
    prm.set_excelname('S7013_D1_NREM.xls')
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


'This loads 4 headstages in numpy, calculates stimulations, plots entrainment, saves an excel of it'
#data=load_16channel_opto(prm.get_headstages())
#stimulations = actual_stim_times(data,  prm.get_sampling_rate(), prm.get_headstages())  
###multiple_entrainmentratio_with_plots(stimulations, data, prm.get_stimduration())
#del(data)

'Function below loads each 16-channel-headstage individually.'
#data=load_16channel_opto_individually(4)


'Function below loads the data in numpy format, no MNE'
#data=load_16channel_opto(prm.get_headstages())

'Functions below load the data and make the MNE data object, specify how many headstages'
#Below loads 16 channel arrays.
custom_raw=load_16_channel_opto_mne(4)

#Below loads 32-channel array.
#custom_raw=load_32_EEG("100")
'This is to make MNE array of filtered data through MNE filt function.'
#filt=custom_raw.filter(0, 480, fir_design='firwin')


'If you have specific times to analyse, load excel spreadsheet of them below.'

#analysis_times=import_spreadsheet(prm.get_excelpath() + prm.get_excelname()) #Imports spreadsheet
#stim=create_epochs(stimulations, prm.get_sampling_rate()) #Creates stim time array that MNE can read.

'This is if brain state epoch array is available'
#analysis_times=import_brain_state(prm.get_excelpath() + prm.get_excelname()) 

'This is if channel combination array is available for coherence is cross-frequency coupling analyses'
#channel_combo=import_channel_combo(prm.get_excelpath() + prm.get_channel_combo_name()) #

'This below is a function to get actual stimulation times. Load one individual headstage, non-MNE format.'
#stimulations = actual_stim_times(data,  prm.get_sampling_rate(), prm.get_headstages())    
#

'This outputs the entrainment ratio for one channel'
#multiple_entrainmentratio_with_plots(stimulations, data, prm.get_stimduration())


#fig, ax = plt.subplots()
#x0=full(len(entrainmentresults), 0.5)
#x1=full(len(entrainmentresults), 1)

#scatter=ax.scatter(x0, entrainmentresults[:,0], c='k')
#scatter=ax.scatter(x1, entrainmentresults[:,1], c='b')



'This outputs theta delta ratio for one channel'
#multiple_theta_delta(analysis_times, data[:, 15])

'This outputs multiple PSD plots for one channel'
#multiple_psds(analysis_times, data[:, 30])

'This function calculates theta_delta ratio and entrainment for all channels in a 16 channel headstage'
'It outputs as excel spreadsheet in file, have to specify animal name as string'
#sixteenchan_thetadelta_entrainment(data, analysis_times, "VGAT_481")


'This below adds the epochs to the object.'
#print(stim)
#epochs=mne.Epochs(custom_raw, stim, baseline= None, 
#           detrend=None, tmin=-0.5, tmax=1, )

#epochs=mne.Epochs(custom_raw, stim, event_id=[0], baseline= None, 
          # detrend=None, tmin=-1, tmax=1)

#picks =[14, 15]

'This can average the epochs'
#avgepochs=epochs.average()
#
#HPC_Cepochs=mne.Epochs(custom_raw, stim, baseline= None, picks=[62, 63],
#           detrend=None, tmin=-0.2, tmax=.7, )# picks=['hp_caud_d_2'],
#
#HPC_Cepochs2=mne.Epochs(custom_raw, stim, baseline= None, picks=[49],
#           detrend=None, tmin=-0.3, tmax=.8, )# picks=['hp_caud_d_2'],
#
#
#HPC_Average=HPC_Cepochs.average()
#HPC_standard_error=HPC_Cepochs.standard_error()
#HPC_Average2=HPC_Cepochs2.average()
#HPC_M=HPC_Mepochs.average()
#
#HPC_Average.plot()
#HPC_standard_error.plot()

'This is to do PSD plots of the epochs'

#epochs.plot_psd(custom_raw, fmin= 1, fmax=15, tmin=-10, tmax=10, picks=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,64])


'Creates epoch file. Creates epochs from analysis times.'
#stim=create_brain_state_epochs(analysis_times, prm.get_sampling_rate())

'Functions for evoked plots'
#evoked= epochs.average().pick_types(eeg=True, emg=True)#to average epochs.
#evoked.plot([31], time_unit='s') #to plot these epochs, first array is channel number.
##
#epochs.plot(n_epochs=1, block=True, 
#            scalings= 'auto', picks=[32,35,37,39,41,44, 47, 64]) #[5,7,9,12,32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 64])
            #[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]) #block episodes. 
#[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46, 47, 48]
#5,7,9,12,21,23,25,28,37,39,41,44,
'The following is to create psd plots of epochs'

#epochs.plot_psd( fmin= 0, fmax=15, tmin=0, tmax=10, low_bias="true", picks=[48])

#epochs.plot_image(picks=[31])

'To do a basic plot below. The following can be added for specifc order of channels order=[4, 5, 3, 0, 1, 14, 15, 16]'
colors=dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
     emg='g', ref_meg='steelblue', misc='k', stim='b',
     resp='k', chpi='k')

custom_raw.plot(None, 5, 20, 8,color = colors, scalings = "auto", order=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46, 47, 48, 49,50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,64], show_options = "true" )#
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
#
#data_sub=data[:,62]-data[:,63]
#plot_all(data_sub, prm.get_sampling_rate(),'k')


#plot_all(data[:,60]-7800, prm.get_sampling_rate(),'k')
#plot_all(data[:,581]-2500, prm.get_sampling_rate(),'k')
#plot_all(data[:,40]-5600, prm.get_sampling_rate(),'k')
#plot_all(data[:,37]-4400, prm.get_sampling_rate(),'k')
#plot_all(data[:,47]-3000, prm.get_sampling_rate(),'k')
#plot_all(data[:,32]-2000, prm.get_sampling_rate(),'k')
#plot_all(data[:,64]*.2-200, prm.get_sampling_rate(),'b')
#










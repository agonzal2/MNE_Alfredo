
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
    prm.set_filepath('C:\\Users\\Alfredo\\Desktop\\Tethered Recordings\\190627\\2019-06-27_15-30-00\\')#E:\\ERUK\\Tethered Recordings\\ERUK Animals\\180917\\2018-09-17_11-11-58\\
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

'This loads 4 headstages in numpy, calculates stimulations, plots entrainment, saves an excel of it'
data=load_16channel_opto(prm.get_headstages())
#filtered_data=Implement_Notch_Filter(prm.get_sampling_rate(), 3, 50, 1, 2, "butter", data)
stimulations = actual_stim_times(data,  prm.get_sampling_rate(), prm.get_headstages())  

'For getting PSD spectrum from 870 in epilepsy 2019-06-27_13-22-41'
#time_axis1, sub_data1=sub_time_data(data[:,32], 5308.33, 5338.33, prm.get_sampling_rate())
#time_axis2, sub_data2=sub_time_data(data[:,32], 5338.33, 5368.33, prm.get_sampling_rate())
#psd_2chan (sub_data1, sub_data2, prm.get_windowtype(), prm.get_sampling_rate(), prm.get_stimfreq())

#multiple_entrainmentratio_with_plots(stimulations, data, prm.get_stimduration())
del(data)

'Function below loads each 16-channel-headstage individually.'
#data=load_16channel_opto_individually(1)


'Function below loads the data in numpy format, no MNE'
#data=load_16channel_opto(prm.get_headstages())

'Functions below load the data and make the MNE data object, specify how many headstages'
#Below loads 16 channel arrays.
#print(prm.get_filepath())
custom_raw=load_16_channel_opto_mne(4)

filt=custom_raw.filter(6, 14, fir_design='firwin')
#
#custom_raw.apply_hilbert(picks=[32, 46, 38, 40, 42, 64])
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
#           detrend=None, tmin=-30, tmax=0, )
#
#

baseline_epochs=mne.Epochs(custom_raw, stim, baseline= None, 
       detrend=None, tmin=-30, tmax=0)

stim_epochs=mne.Epochs(custom_raw, stim, baseline= None, 
       detrend=None, tmin=0, tmax=30)



hil_data_baseline=baseline_epochs.get_data(picks=[32, 46, 38, 40, 42, 64]) #Produces numpy array from picks.
hil_data_stim=stim_epochs.get_data(picks=[32, 46, 38, 40, 42, 64])


'Up to here have hilbert transformed epochs per channel picks, in array'


ext_times_1j_alltrodes_baseline_1st, ext_times_1j_alltrodes_stim_1st = ispc_trials_return_exponential_1j_over_time(hil_data_baseline, hil_data_stim, channel_combo)

ext_times_1j_alltrodes_baseline_2nd, ext_times_1j_alltrodes_stim_2nd = ispc_trials_return_exponential_1j_over_time(hil_data_baseline, hil_data_stim, channel_combo)

custom_raw.close
baseline_epochs.close
stim_epochs.close
'concatenate arrays here'
all_epochs_baseline=concatenate((ext_times_1j_alltrodes_baseline_1st, ext_times_1j_alltrodes_baseline_2nd), axis=0)
all_epochs_stim=concatenate((ext_times_1j_alltrodes_stim_1st, ext_times_1j_alltrodes_stim_2nd), axis=0)




'Then write function to average at individual time points and across entire epoch'

def calculate_ispc_trials(all_epochs_baseline, all_epochs_stim):
    avg_epochs_baseline=all_epochs_baseline.mean(0)
    abs_avg_baseline=abs(avg_epochs_baseline)
    ipsc_metric_baseline=abs_avg_baseline.mean(1)
    
    avg_epochs_stim=all_epochs_stim.mean(0)
    abs_avg_stim=abs(avg_epochs_stim)
    ipsc_metric_stim=abs_avg_stim.mean(1)
    
    return abs_avg_baseline, ipsc_metric_baseline, abs_avg_stim, ipsc_metric_stim

abs_avg_baseline, ipsc_metric_baseline, abs_avg_stim, ipsc_metric_stim = calculate_ispc_trials(all_epochs_baseline, all_epochs_stim)

baselined=abs_avg_stim-abs_avg_baseline


#plot_all(baselined[4,:], prm.get_sampling_rate(),'k')
#plot_all(baselined[8,:], prm.get_sampling_rate(),'g')
#plot_all(baselined[11,:], prm.get_sampling_rate(),'g')
#plot_all(baselined[13,:], prm.get_sampling_rate(),'k')
#plot_all(baselined[14,:], prm.get_sampling_rate(),'g')


    
    




#            avg_exp_1j=exp_times_1j.mean(0) #average the epochs along epoch axis
#            ipsc_avg_across_time=abs(avg_exp_1j) #make absolue.
#            
#            ipsc_metric=average(ipsc_avg_across_time) #average values across trial.  
#
#             array_index=int(n)
##            ispc_metric_array_index=int(n)  #Figure out index of where to place data,
##            ipsc_metric_array[ispc_metric_array_index]=ipsc_metric
#            
#            
#            
#            
#            
##            ipsc_metric_array[ispc_metric_array_index, :]=ipsc_metric



#abs(mean(exp(1j*(phase_diff_32_46[])))


#epochs.plot_image(picks=[32, 46, 38, 40, 42], cmap='inferno')
#
##epochs=mne.Epochs(custom_raw, stim, baseline= None, 
##           detrend=None, tmin=-.5, tmax=1)
##
###picks =[14, 15]
##
##'This can average the epochs'
#avgepochs=epochs.average()
##
#HPC_Cepochs=mne.Epochs(custom_raw, stim, baseline= None, picks=[0,1],
#           detrend=None, tmin=-0.5, tmax=.02, )# picks=['hp_caud_d_2'],
####
####HPC_Cepochs2=mne.Epochs(custom_raw, stim, baseline= None, picks=[49],
####           detrend=None, tmin=-0.3, tmax=.8, )# picks=['hp_caud_d_2'],
####
####
#HPC_Average=HPC_Cepochs.average()
#
#Average_values=HPC_Average.times
###HPC_standard_error=HPC_Cepochs.standard_error()
###HPC_Average2=HPC_Cepochs2.average()
###HPC_M=HPC_Mepochs.average()
###
#HPC_Average.plot()
#HPC_standard_error.plot()

#'Epoch average'
#epochs=mne.Epochs(custom_raw, stim, baseline= None, 
#           detrend=None, tmin=-0.5, tmax=.5, )
##
##epochs=mne.Epochs(custom_raw, stim, baseline= None, 
##           detrend=None, tmin=-0.5, tmax=.6, )
##
##HPC_Average=HPC_Cepochs.average()
#
#
#'This is to do PSD plots of the epochs'
#
##epochs.plot_psd(fmin= 1, fmax=15, tmin=-10, tmax=10, picks=[32, 37, 39, 41])
#
#
#'Creates epoch file. Creates epochs from analysis times.'
##stim=create_brain_state_epochs(analysis_times, prm.get_sampling_rate())
#
#'Functions for evoked plots'
##evoked= epochs.average().pick_types(eeg=True, emg=True)#to average epochs.
#evoked.plot([32], time_unit='s') #to plot these epochs, first array is channel number.
##
#epochs.plot(n_epochs=1, block=True, 
#            scalings= 'auto', picks=[32, 64]) #[5,7,9,12,32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 64])
#            [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]) #block episodes. 
#[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46, 47, 48]
#5,7,9,12,21,23,25,28,37,39,41,44,
'The following is to create psd plots of epochs'

#epochs.plot_psd( fmin= 0, fmax=15, tmin=0, tmax=10, low_bias="true", picks=[48])

#epochs.plot_image(picks=[31])

'To do a basic plot below. The following can be added for specifc order of channels order=[4, 5, 3, 0, 1, 14, 15, 16]'
#colors=dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
#     emg='g', ref_meg='steelblue', misc='k', stim='b',
#     resp='k', chpi='k')
##
#custom_raw.plot(None, 5, 20, 8,color = colors, scalings = "auto", order=[32,33, 37, 38, 39, 40, 41, 42, 43, 47, 64], show_options = "true" )#
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



### Use below for tethered delay plot.

#870Epilepsy - 2019-06-27_13-22-41

#
#plot_all(data[:,32]-1000, prm.get_sampling_rate(),'k')#caudal ipsi
##plot_all(data[:,33]-1000, prm.get_sampling_rate(),'g')#caudal contra
##plot_all(data[:,46]-2000, prm.get_sampling_rate(),'r')#medial contra
#plot_all(data[:,46]-2000, prm.get_sampling_rate(),'g')#rostral contra
##plot_all(data[:,37]-4000, prm.get_sampling_rate(),'r')#medial ipsi
#plot_all(data[:,38]-3000, prm.get_sampling_rate(),'g')#caudal ipsi
##plot_all(data[:,39]-6000, prm.get_sampling_rate(),'g')#caudal contra
#plot_all(data[:,40]-4000, prm.get_sampling_rate(),'k')#medial contra
##plot_all(data[:,41]-8000, prm.get_sampling_rate(),'k')#rostral contra
#plot_all(data[:,42]-5000, prm.get_sampling_rate(),'g')#medial ipsi


#plot_all(data[:,16]-1000, prm.get_sampling_rate(),'k')#caudal ipsi
##plot_all(data[:,33]-1000, prm.get_sampling_rate(),'g')#caudal contra
##plot_all(data[:,46]-2000, prm.get_sampling_rate(),'r')#medial contra
#plot_all(data[:,47]-2000, prm.get_sampling_rate(),'g')#rostral contra
##plot_all(data[:,37]-4000, prm.get_sampling_rate(),'r')#medial ipsi
#plot_all(data[:,37]-3000, prm.get_sampling_rate(),'g')#caudal ipsi
##plot_all(data[:,39]-6000, prm.get_sampling_rate(),'g')#caudal contra
#plot_all(data[:,39]-4000, prm.get_sampling_rate(),'k')#medial contra
##plot_all(data[:,41]-8000, prm.get_sampling_rate(),'k')#rostral contra
#plot_all(data[:,41]-5000, prm.get_sampling_rate(),'g')#medial ipsi


####'F:\\Tethered Recordings\\190607\\2019-06-07_17-44-43 - 874 Pre-epilepsy

#plot_all(filtered_data[:,32]-1000, prm.get_sampling_rate(),'k')#caudal ipsi
##plot_all(data[:,33]-1000, prm.get_sampling_rate(),'g')#caudal contra
##plot_all(data[:,46]-2000, prm.get_sampling_rate(),'r')#medial contra
#plot_all(filtered_data[:,47]-2000, prm.get_sampling_rate(),'g')#rostral contra
##plot_all(data[:,37]-4000, prm.get_sampling_rate(),'r')#medial ipsi
#plot_all(filtered_data[:,37]-3000, prm.get_sampling_rate(),'g')#caudal ipsi
##plot_all(data[:,39]-6000, prm.get_sampling_rate(),'g')#caudal contra
#plot_all(filtered_data[:,39]-4000, prm.get_sampling_rate(),'k')#medial contra
##plot_all(data[:,41]-8000, prm.get_sampling_rate(),'k')#rostral contra
#plot_all(filtered_data[:,41]-5000, prm.get_sampling_rate(),'g')#medial ipsi

####'F:\\Tethered Recordings\\190627\\2019-06-27_15-30-00 - 874 epilepsy
#plot_all(data[:,48]-1000, prm.get_sampling_rate(),'k')#caudal ipsi
##plot_all(data[:,33]-1000, prm.get_sampling_rate(),'g')#caudal contra
##plot_all(data[:,46]-2000, prm.get_sampling_rate(),'r')#medial contra
#plot_all(data[:,62]-2000, prm.get_sampling_rate(),'g')#rostral contra
##plot_all(data[:,37]-4000, prm.get_sampling_rate(),'r')#medial ipsi
#plot_all(data[:,53]-3000, prm.get_sampling_rate(),'g')#caudal ipsi
##plot_all(data[:,39]-6000, prm.get_sampling_rate(),'g')#caudal contra
#plot_all(data[:,55]-4000, prm.get_sampling_rate(),'k')#medial contra
##plot_all(data[:,41]-8000, prm.get_sampling_rate(),'k')#rostral contra
#plot_all(data[:,57]-5000, prm.get_sampling_rate(),'g')#medial ipsi

###Tethered Recordings\\190627\\2019-06-27_13-22-41\\870 - Epilepsy Example
#plot_all(data[:,32]-1000, prm.get_sampling_rate(),'k')#caudal ipsi
##plot_all(data[:,33]-1000, prm.get_sampling_rate(),'g')#caudal contra
##plot_all(data[:,46]-2000, prm.get_sampling_rate(),'r')#medial contra
#plot_all(data[:,46]-2000, prm.get_sampling_rate(),'g')#rostral contra
##plot_all(data[:,37]-4000, prm.get_sampling_rate(),'r')#medial ipsi
#plot_all(data[:,38]-3000, prm.get_sampling_rate(),'g')#caudal ipsi
##plot_all(data[:,39]-6000, prm.get_sampling_rate(),'g')#caudal contra
#plot_all(data[:,40]-4000, prm.get_sampling_rate(),'k')#medial contra
##plot_all(data[:,41]-8000, prm.get_sampling_rate(),'k')#rostral contra
#plot_all(data[:,41]-5000, prm.get_sampling_rate(),'g')#medial ipsi


###870pre-epilepsy2019-06-08_10-57-10
#plot_all(data[:,48]-1000, prm.get_sampling_rate(),'k')#caudal ipsi
##plot_all(data[:,33]-1000, prm.get_sampling_rate(),'g')#caudal contra
##plot_all(data[:,46]-2000, prm.get_sampling_rate(),'r')#medial contra
#plot_all(data[:,62]-2000, prm.get_sampling_rate(),'g')#rostral contra
##plot_all(data[:,37]-4000, prm.get_sampling_rate(),'r')#medial ipsi
#plot_all(data[:,54]-3000, prm.get_sampling_rate(),'g')#caudal ipsi
##plot_all(data[:,39]-6000, prm.get_sampling_rate(),'g')#caudal contra
#plot_all(data[:,56]-4000, prm.get_sampling_rate(),'k')#medial contra
##plot_all(data[:,41]-8000, prm.get_sampling_rate(),'k')#rostral contra
#plot_all(data[:,57]-5000, prm.get_sampling_rate(),'g')#medial ipsi


#plot_all(data[:,64]*.2, prm.get_sampling_rate(),'b')
##
#plot_all(data[:,15], prm.get_sampling_rate(),'g')#caudal ipsi
#plot_all(data[:,9], prm.get_sampling_rate(),'g')#caudal contra
#plot_all(data[:,7], prm.get_sampling_rate(),'r')#medial contra
#plot_all(data[:,2], prm.get_sampling_rate(),'k')#rostral contra
#plot_all(data[:,1], prm.get_sampling_rate(),'r')#medial ipsi
#plot_all(data[:,64]*.2, prm.get_sampling_rate(),'b')



#32,33, 37, 38, 39, 40, 41, 42, 46, 47, 64





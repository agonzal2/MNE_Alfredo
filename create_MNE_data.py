# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:54:00 2018

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk

This makes the objects for MNE.
"""
import mne
from numpy import transpose
from matplotlib import pyplot as plt
from mne.time_frequency import (tfr_multitaper, tfr_stockwell, tfr_morlet,
                                tfr_array_morlet)


#This takes the date generated from main_script_openephys_mne.py and transposes it.


#datatp=data.transpose()#Array from openephys has to be trasnposed to match RawArray MNE function to create.
#del data

#Below I make the channel names and channel types, this should go in the parameteres file later.

channel_names=['hpc_mid_deep', 'hpc_mid_sup', 'hpc_ros_deep', 'hpc_ros_sup', 'pfc_deep', 
               'pfc_sup', 'cx1', 'cx2', 'hpc_contra_deep', 'hpc_contra_sup', 
               'EMG1', 'EMG2', 'cb_deep', 'cb_sup', 'hp_caudal_deep', 'hpc_caudal_sup',
               'hpc_mid_d_2', 'hpc_mid_s_2', 'hpc_ros_d_2', 'hpc_ros_s_2', 'pfc_d_2', 
               'pfc_sup_2', 'cx1_2', 'cx2_2', 'hpc_ct_d_2', 'hpc_ct_s_2', 
               'EMG1_2', 'EMG2_2', 'cb_deep_2', 'cb_sup_2', 'hp_caud_d_2', 'hpc_caud_s_2',
               'hpc_mid_d_3', 'hpc_mid_s_3', 'hpc_ros_d_3', 'hpc_ros_s_3', 'pfc_d_3', 
               'pfc_s_3', 'cx1_3', 'cx2_3', 'hpc_c_d_3', 'hpc_c_s_3', 
               'EMG1_3', 'EMG2_3', 'cb_deep_3', 'cb_sup_3', 'hp_c_d_3', 'hpc_c_s_3',
               'Opto']
channel_types=['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
               'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
               'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
               'stim']


#This creates the info object that includes names, sampling rate, channel types and in the future location.
info = mne.create_info(channel_names, prm.get_sampling_rate(), channel_types)

#This below allows to mark bad channels once known. Uncomment if needed.
custom_raw.info['bads']=['hpc_contra_deep', 'hpc_contra_sup', 'hpc_caudal_sup','hpc_ros_d_2','cx1_2', 'cx2_2'
               'hpc_c_d_3', 'hpc_c_s_3','EMG1_2', 'EMG2_2', 'EMG2_3']

#This creates the data array with the info, so the object for the MNE to work and then we can 
#perform functions made for these EEG objects.

custom_raw = mne.io.RawArray(datatp, info)


#This is to filter.
#filt=custom_raw.filter(1, 100, fir_design='firwin')





#This below adds the epochs to the object.Uncomment if needed.
epochs=mne.Epochs(custom_raw, stim, baseline= None, 
           detrend=None, tmin=-5, tmax=2)


##To do a basic plot is below
#
#Dictionary for color of traces:
colors=dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
     emg='g', ref_meg='steelblue', misc='k', stim='b',
     resp='k', chpi='k')


#This command below makes the plot, change the order to see more channels.
#custom_raw.plot(None, 5, 20, 8,color = colors, scalings = "auto", show_options = "true")#

#order= [1, 48, 5]

#evoked= epochs.average().pick_types(eeg=True, emg=True)#to average epochs.
#evoked.plot([15], time_unit='s') #to plot these epochs, first array is channel number.

##This below plots epochs individually so can go through them. 
epochs.plot(n_epochs=1, block=True, scalings= 'auto') #block episodes. 


###To do psd plots of epochs

#epochs.plot_psd(custom_raw, fmin= 1, fmax=15, tmin=-10, tmax=10, picks=[15])
#
#



#########BELOW IS WORK TO GENERATE WAVELETS AND ALSO TO MAKE THE MAP OF ELECTRODES, IGNORE FOR NOW.

#Plotting Time frequency representation with DPSS Tapers.

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

#baseline=(-10., 0), mode='mean', 

## Ploting Time frequency representation with Stockwell (S) transform
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

### Plotting TFR with Morlet Waveletes

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
##


### Montage of electrodes.

#trode_map = np.zeros(shape=(32,3))  ### Use Hsp with trode_map in
#                                    ### mne.channels.read_dig_montage
#                                    #### https://www.martinos.org/mne/stable/generated/mne.channels.read_dig_montage.html#mne.channels.read_dig_montage
#
#trode_map[0][0]=-3
#trode_map[1][0]=-3
#trode_map[2][0]=-5
#trode_map[3][0]=-5
#trode_map[4][0]=-5
#trode_map[5][0]=-7
#trode_map[6][0]=-7
#trode_map[7][0]=-7
#trode_map[8][0]=-3
#trode_map[9][0]=-1
#trode_map[10][0]=-1
#trode_map[11][0]=0.6
#trode_map[12][0]=1.5
#trode_map[13][0]=1.5
#trode_map[14][0]=3.5
#trode_map[15][0]=3.6
#trode_map[16][0]=3.6
#trode_map[17][0]=3.5
#trode_map[18][0]=1.5
#trode_map[19][0]=1.5
#trode_map[20][0]=0.6
#trode_map[21][0]=-1.0
#trode_map[22][0]=-1.0
#trode_map[23][0]=-3.0
#trode_map[24][0]=-7
#trode_map[25][0]=-7
#trode_map[26][0]=-7
#trode_map[27][0]=-5
#trode_map[28][0]=-5
#trode_map[29][0]=-5
#trode_map[30][0]=-3
#trode_map[31][0]=-3
#
#
#trode_map[0][1]=2.8
#trode_map[1][1]=4
#trode_map[2][1]=1.5
#trode_map[3][1]=3
#trode_map[4][1]=4.4
#trode_map[5][1]=1.5
#trode_map[6][1]=3
#trode_map[7][1]=4.4
#trode_map[8][1]=1.2
#trode_map[9][1]=2.8
#trode_map[10][1]=1.2
#trode_map[11][1]=3.8
#trode_map[12][1]=2.8
#trode_map[13][1]=1.2
#trode_map[14][1]=2.5
#trode_map[15][1]=1.2
#trode_map[16][1]=-1.2
#trode_map[17][1]=-2.5
#trode_map[18][1]=-1.2
#trode_map[19][1]=-2.8
#trode_map[20][1]=-3.8
#trode_map[21][1]=-1.2
#trode_map[22][1]=-2.8
#trode_map[23][1]=-1.2
#trode_map[24][1]=-4.4
#trode_map[25][1]=-3
#trode_map[26][1]=-1.5
#trode_map[27][1]=-4
#trode_map[28][1]=-3
#trode_map[29][1]=-1.5
#trode_map[30][1]=-4
#trode_map[31][1]=-2.8
#print(trode_map)
#
#
#point_names= ('S1Tr_r','S1DZ_S1BF_r','V"MM_RSA_r','V2ML','V2L_r',
#              'V2MM_r','V1M_r','V2L_V1B_r','M2_post_r','S1HL_S1FL_r',
#              'M1_post_r','S1FL_S1DZ_r','M1_ant_r','M2_ant_r',
#              'M1_FrA_r','M2_FrA_r','M2_FRA_l','M1_FRA_l','M2_ant_l',
#              'M1_ant_l','S1FL_S1DZ_l','M1_post_l','S1HL_S1FL_l',
#              'M2_post_l','V2L_V1B_l','V1M_l','V2MM_l','V2L_l','V2MM_l',
#              'V1MM_RSA_l','S1DZ_S1BF_l','S1TR_l')
#
#print(point_names)
#    




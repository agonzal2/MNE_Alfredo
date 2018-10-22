
"""
Created on Tue Jun 26 16:54:00 2018

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk

This makes the objects for MNE.
"""

import glob
import os

import mne
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

init_params()

#####This takes the date generated from main_script_openephys_mne.py and transposes it.
#
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
               '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63',
               'Opto']
channel_types=['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
               'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
               'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
               'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg',
               'stim']


#This creates the info object that includes names, sampling rate, channel types and in the future location.
#info = mne.create_info(channel_names, prm.get_sampling_rate(), channel_types)

##This below allows to mark bad channels once known. Uncomment if needed.
#custom_raw.info['bads']=['hpc_contra_deep', 'hpc_contra_sup', 'hpc_caudal_sup','hpc_ros_d_2','cx1_2', 'cx2_2'
#               'hpc_c_d_3', 'hpc_c_s_3','EMG1_2', 'EMG2_2', 'EMG2_3']

#This creates the data array with the info, so the object for the MNE to work and then we can 
#perform functions made for these EEG objects.

#custom_raw = mne.io.RawArray(datatp, info)


#####This is to filter.
#filt=custom_raw.filter(8, 11, fir_design='firwin')
#




#This below adds the epochs to the object.Uncomment if needed.
#epochs=mne.Epochs(custom_raw, stim, baseline= None, 
#           detrend=None, tmin=-.2, tmax=3)


##To do a basic plot is below
#
#Dictionary for color of traces:
colors=dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
     emg='g', ref_meg='steelblue', misc='k', stim='b',
     resp='k', chpi='k')


###This command below makes the plot, change the order to see more channels.
#custom_raw.plot(None,  5, 20, 8,color = colors, scalings = "auto", 
#                show_options = "true")#

#order= [16, 17, 19, 30, 31, 20, 21, 28, 29, 48]

#evoked= epochs.average().pick_types(eeg=True, emg=True)#to average epochs.
#evoked.plot([15], time_unit='s') #to plot these epochs, first array is channel number.


###epochs average
#avgepochs=epochs.average()
#
####This below plots epochs individually so can go through them. 
epochs.plot(picks=[40, 41, 42, 43, 44, 45, 64], n_epochs=1, block=True, 
            scalings= 'auto') #block episodes picks= [19, 16, 17,  30, 31,  48, 20, 21, 28, 29]


###This below can make a plot of all epochs together. 
#
#epochs.plot_image(picks=[31, 48], combine='mean', group_by='type', sigma=2., cmap="rainbow")
#

###To do psd plots of epochs

#epochs.plot_psd(custom_raw, fmin= 1, fmax=15, tmin=-10, tmax=10, picks=[15])
#
#
###This is to plot coherence below
#
#multiple_coherence(analysis_times, custom_raw)

#t_idx=custom_raw.time_as_index([2070.334, 2080.334])
#data1, times =custom_raw[32, t_idx[0]:t_idx[1]]
#data2, times =custom_raw[48,t_idx[0]:t_idx[1]]
#
#
#wind=scipy.signal.get_window("hann", prm.get_sampling_rate()*2) ###2 second window.
#f, coh = coherence(data1, data2, fs=prm.get_sampling_rate(), window=wind) ##window overlap is half. 
#plt.xlim([0, 15])
#plt.axvline(x=10)
#plt.plot(f, coh[0,:], lw=1.)

#########BELOW IS WORK TO GENERATE WAVELETS AND ALSO TO MAKE THE MAP OF ELECTRODES, IGNORE FOR NOW.

#Plotting Time frequency representation with DPSS Tapers.

#freqs = np.arange(5., 16., 1.)
#vmin, vmax = 112, 128.  # Define our color limits.

#n_cycles = freqs /2.
#time_bandwidth = 2 # Least possible frequency-smoothing (1 taper)
#power = tfr_multitaper(epochs, freqs=freqs, n_cycles=n_cycles,
#                       time_bandwidth=time_bandwidth, return_itc=False, picks=[30])
#
#dir(power)
## Plot results. B,aseline correct based on first 100 ms.
#power.plot([0], vmin=vmin, 
#           vmax=vmax, cmap=('rainbow', 'interactive' ),baseline=(-1., 0), mode='mean', dB=True)


## Ploting Time frequency representation with Stockwell (S) transform
#
#

#fmin, fmax = freqs[[0, -1]]
#
#
#power = tfr_stockwell(epochs, fmin=fmin, fmax=fmax, width=width)
#power.plot(picks=[0], baseline=(-10., 0), mode='mean', axes=ax, show=False,
#               colorbar=True)
#    #ax.set_title('Sim: Using S transform, width = {:0.1f}'.format(width))
#plt.tight_layout()

### Plotting TFR with Morlet Waveletes
#
#


#n_cycles=4.5
#power = tfr_morlet(epochs, freqs=freqs, n_cycles=n_cycles, use_fft= True,
#                       return_itc=False, picks=[31])
#
#
#power.plot( vmin=vmin, vmax=vmax,
#               dB=True, show=False, colorbar=True, cmap='jet')#Key was DB as poer of frequencies is very tight.#
###baseline=(-5, 0), mode='mean',





#n_cycles = 'scaled by freqs' if not isinstance(n_cycles, int) else n_cycles
#ax.set_title('Sim: Using Morlet wavelet, n_cycles = %s' % n_cycles)
#plt.tight_layout()
###
#axes=ax

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




# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:54:00 2018

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
import mne
from numpy import transpose
from matplotlib import pyplot as plt
from mne.time_frequency import (tfr_multitaper, tfr_stockwell, tfr_morlet,
                                tfr_array_morlet)

datatp=data.transpose()#Array from openephys has to be trasnposed to match RawArray MNE function to create.
#data comes from openephys.

#data_aux=data_aux.transpose()

#set nme parameters
n_channels =33

channel_names=['S1Tra', 'S1DZ_S1BFa', 'V2MM_RSAa', 'V2MLa', 'V2La', 'V2MMa', 
               'V1Ma', 'V2L_V1Ba', 'M2_posta', 'S1HL_S1FLa',
               'M1_Posta', 'S1FL_S1DZa', 'M1_anta', 'M2_anta', 'M1_FrAa', 
               'M2_FrAa', 'M2_FRAb', 'M1_FRAb', 'M2_antb', 
               'M1_antb', 'S1FL_S1DZb', 'M1_Postb', 'S1HL_S1FLb',
               'M2_postb', 'V2L_V1Bb', 'V1Mb', 'V2MMb', 'V2Lb',
               'V2MLb', 'V2MM_RSAb', 'S1DZ_S1BFb', 'S1Trb', 'AUX', 'sleep']
channel_types=['eeg','eeg','eeg','eeg','eeg','eeg', 'eeg', 'eeg', 
               'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg'
               ,'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg'
               ,'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg', 'emg', 'misc']


<<<<<<< HEAD
### Montage of electrodes.
#trode_map = np.zeros(shape=(35,3))  ### Use Hsp with trode_map in
#                                    ### mne.channels.read_dig_montage
#                                    #### https://www.martinos.org/mne/stable/generated/mne.channels.read_dig_montage.html#mne.channels.read_dig_montage
#trode_map[0][0]=1
#trode_map[1][0]=2
#trode_map[2][0]=3
#trode_map[3][0]=4
#trode_map[4][0]=5
#trode_map[5][0]=6
#trode_map[6][0]=7
#trode_map[7][0]=8
#trode_map[8][0]=9
#trode_map[9][0]=10
#trode_map[10][0]=11
#trode_map[11][0]=12
#trode_map[12][0]=13
#trode_map[13][0]=14
#trode_map[14][0]=15
#trode_map[15][0]=16
#trode_map[16][0]=17
#trode_map[17][0]=18
#trode_map[18][0]=19
#trode_map[19][0]=20
#trode_map[20][0]=21
#trode_map[21][0]=22
#trode_map[22][0]=23
#trode_map[23][0]=24
#trode_map[24][0]=25
#trode_map[25][0]=26
#trode_map[26][0]=27
#trode_map[27][0]=28
#trode_map[28][0]=29
#trode_map[29][0]=30
#trode_map[30][0]=31
#trode_map[31][0]=32
#trode_map[32][0]=33
#trode_map[33][0]=34
#trode_map[34][0]=35
#
#
#trode_map[0][1]=-3
#trode_map[1][1]=-3
#trode_map[2][1]=-5
#trode_map[3][1]=-5
#trode_map[4][1]=-5
#trode_map[5][1]=-7
#trode_map[6][1]=-7
#trode_map[7][1]=-7
#trode_map[8][1]=-3
#trode_map[9][1]=-1
#trode_map[10][1]=-1
#trode_map[11][1]=0.6
#trode_map[12][1]=1.5
#trode_map[13][1]=1.5
#trode_map[14][1]=3.5
#trode_map[15][1]=3.6
#trode_map[16][1]=3.6
#trode_map[17][1]=3.5
#trode_map[18][1]=1.5
#trode_map[19][1]=1.5
#trode_map[20][1]=0.6
#trode_map[21][1]=-1.0
#trode_map[22][1]=-1.0
#trode_map[23][1]=-3.0
#trode_map[24][1]=-7
#trode_map[25][1]=-7
#trode_map[26][1]=-7
#trode_map[27][1]=-5
#trode_map[28][1]=-5
#trode_map[29][1]=-5
#trode_map[30][1]=-3
#trode_map[31][1]=-3
#trode_map[32][1]=3.8
#trode_map[33][1]=-5
#trode_map[34][1]=-5
#
#trode_map[0][2]=2.8
#trode_map[1][2]=4
#trode_map[2][2]=1.5
#trode_map[3][2]=3
#trode_map[4][2]=4.4
#trode_map[5][2]=1.5
#trode_map[6][2]=3
#trode_map[7][2]=4.4
#trode_map[8][2]=1.2
#trode_map[9][2]=2.8
#trode_map[10][2]=1.2
#trode_map[11][2]=3.8
#trode_map[12][2]=2.8
#trode_map[13][2]=1.2
#trode_map[14][2]=2.5
#trode_map[15][2]=1.2
#trode_map[16][2]=-1.2
#trode_map[17][2]=-2.5
#trode_map[18][2]=-1.2
#trode_map[19][2]=-2.8
#trode_map[20][2]=-3.8
#trode_map[21][2]=-1.2
#trode_map[22][2]=-2.8
#trode_map[23][2]=-1.2
#trode_map[24][2]=-4.4
#trode_map[25][2]=-3
#trode_map[26][2]=-1.5
#trode_map[27][2]=-4
#trode_map[28][2]=-3
#trode_map[29][2]=-1.5
#trode_map[30][2]=-4
#trode_map[31][2]=-2.8
#trode_map[32][2]=0
#trode_map[33][2]=4.6
#trode_map[34][2]=-4.6
#
#
#
#
#point_names= ('CHPI001','CHPI002','CHPI003','CHPI004','CHPI005','CHPI006',
#              'CHPI007','CHPI008','CHPI009','CHPI010','CHPI011',
#              'CHPI012','CHPI013','CHPI014','CHPI015',
#              'CHPI016','CHPI017','CHPI018','CHPI019','CHPI020',
#              'CHPI021','CHPI022','CHPI023','CHPI024',
#              'CHPI025','CHPI026','CHPI027','CHPI028','CHPI029','CHPI030',
#              'CHPI031','CHPI032','nasion', 'lpa', 'rpa')
=======
### Montage of electrodes. Still not working so ignore for now. Doesn't do anything to plotting.
trode_map = np.zeros(shape=(35,3))  ### Use Hsp with trode_map in
                                    ### mne.channels.read_dig_montage
                                    #### https://www.martinos.org/mne/stable/generated/mne.channels.read_dig_montage.html#mne.channels.read_dig_montage
trode_map[0][0]=1
trode_map[1][0]=2
trode_map[2][0]=3
trode_map[3][0]=4
trode_map[4][0]=5
trode_map[5][0]=6
trode_map[6][0]=7
trode_map[7][0]=8
trode_map[8][0]=9
trode_map[9][0]=10
trode_map[10][0]=11
trode_map[11][0]=12
trode_map[12][0]=13
trode_map[13][0]=14
trode_map[14][0]=15
trode_map[15][0]=16
trode_map[16][0]=17
trode_map[17][0]=18
trode_map[18][0]=19
trode_map[19][0]=20
trode_map[20][0]=21
trode_map[21][0]=22
trode_map[22][0]=23
trode_map[23][0]=24
trode_map[24][0]=25
trode_map[25][0]=26
trode_map[26][0]=27
trode_map[27][0]=28
trode_map[28][0]=29
trode_map[29][0]=30
trode_map[30][0]=31
trode_map[31][0]=32
trode_map[32][0]=33
trode_map[33][0]=34
trode_map[34][0]=35


trode_map[0][1]=-3
trode_map[1][1]=-3
trode_map[2][1]=-5
trode_map[3][1]=-5
trode_map[4][1]=-5
trode_map[5][1]=-7
trode_map[6][1]=-7
trode_map[7][1]=-7
trode_map[8][1]=-3
trode_map[9][1]=-1
trode_map[10][1]=-1
trode_map[11][1]=0.6
trode_map[12][1]=1.5
trode_map[13][1]=1.5
trode_map[14][1]=3.5
trode_map[15][1]=3.6
trode_map[16][1]=3.6
trode_map[17][1]=3.5
trode_map[18][1]=1.5
trode_map[19][1]=1.5
trode_map[20][1]=0.6
trode_map[21][1]=-1.0
trode_map[22][1]=-1.0
trode_map[23][1]=-3.0
trode_map[24][1]=-7
trode_map[25][1]=-7
trode_map[26][1]=-7
trode_map[27][1]=-5
trode_map[28][1]=-5
trode_map[29][1]=-5
trode_map[30][1]=-3
trode_map[31][1]=-3
trode_map[32][1]=3.8
trode_map[33][1]=-5
trode_map[34][1]=-5

trode_map[0][2]=2.8
trode_map[1][2]=4
trode_map[2][2]=1.5
trode_map[3][2]=3
trode_map[4][2]=4.4
trode_map[5][2]=1.5
trode_map[6][2]=3
trode_map[7][2]=4.4
trode_map[8][2]=1.2
trode_map[9][2]=2.8
trode_map[10][2]=1.2
trode_map[11][2]=3.8
trode_map[12][2]=2.8
trode_map[13][2]=1.2
trode_map[14][2]=2.5
trode_map[15][2]=1.2
trode_map[16][2]=-1.2
trode_map[17][2]=-2.5
trode_map[18][2]=-1.2
trode_map[19][2]=-2.8
trode_map[20][2]=-3.8
trode_map[21][2]=-1.2
trode_map[22][2]=-2.8
trode_map[23][2]=-1.2
trode_map[24][2]=-4.4
trode_map[25][2]=-3
trode_map[26][2]=-1.5
trode_map[27][2]=-4
trode_map[28][2]=-3
trode_map[29][2]=-1.5
trode_map[30][2]=-4
trode_map[31][2]=-2.8
trode_map[32][2]=0
trode_map[33][2]=4.6
trode_map[34][2]=-4.6




point_names= ('CHPI001','CHPI002','CHPI003','CHPI004','CHPI005','CHPI006',
              'CHPI007','CHPI008','CHPI009','CHPI010','CHPI011',
              'CHPI012','CHPI013','CHPI014','CHPI015',
              'CHPI016','CHPI017','CHPI018','CHPI019','CHPI020',
              'CHPI021','CHPI022','CHPI023','CHPI024',
              'CHPI025','CHPI026','CHPI027','CHPI028','CHPI029','CHPI030',
              'CHPI031','CHPI032','nasion', 'lpa', 'rpa')
>>>>>>> 9c8f0776e90a1064e7af97df161b68dc0a8922ad







#This creates the info that goes with the channels, which is names, sampling rate, and channel types.
info = mne.create_info(channel_names, prm.get_sampling_rate(), channel_types)


#This makes the object that contains all the data and info about the channels.
#Computations like plotting, averaging, power spectrums can be performed on this object.

custom_raw = mne.io.RawArray(datatp, info)



###Below tried to make montages but does not work
#montage= mne.channels.read_dig_montage(elp=trode_map, point_names= point_names, unit='mm', transform=True)
#print(montage)

#montage.plot(scale_factor=10, show_names=True, kind='topomap', show=True)
#This below allows to mark bad channels once known.
#custom_raw.info['bads']=['nothing1', 'nothing2', 'hpc_ros_deep','EMG1']


#This below adds the epochs to the object.
<<<<<<< HEAD
epochs=mne.Epochs(custom_raw, stim, event_id=[0], baseline= None, 
           detrend=None, tmin=-1, tmax=3, )
=======
#epochs=mne.Epochs(custom_raw, stim, event_id=[0], baseline= None, 
          # detrend=None, tmin=-1, tmax=1)
>>>>>>> 9c8f0776e90a1064e7af97df161b68dc0a8922ad




#picks =[14, 15]

##To do a basic plot below
#
#Dictionary for color of traces:
colors=dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
     emg='g', ref_meg='steelblue', misc='k', stim='b',
     resp='k', chpi='k')

<<<<<<< HEAD
evoked= epochs.average().pick_types(eeg=True, emg=True)#to average epochs.
#evoked.plot([0], time_unit='s') #to plot these epochs, first array is channel number.


#epochs.plot(block=True, scalings= 'auto') #block episodes. 

#evoked.plot_topomap(times=np.linspace(0, 0.5, 2), ch_type='mag', time_unit='s')

=======
#evoked= epochs.average().pick_types(eeg=True)
#evoked.plot_topomap(times=np.linspace(0, 0.5, 2), ch_type='mag', time_unit='s')


###This will plot your data. If you want channels in a particular order put the list below of order into the parameters.
>>>>>>> 9c8f0776e90a1064e7af97df161b68dc0a8922ad
custom_raw.plot(None, 5, 20, 8,color = colors, scalings = "auto", show_options = "true" )#


##Can put this into raw_plot order=[4, 5, 3, 0, 1, 14, 15, 16]

##If order there it picks which channels to put and in what order


#
###To do psd plots of epochs

#epochs.plot_psd(custom_raw, fmin= 1, fmax=15, tmin=-10, tmax=10, picks=[15])
#
#


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






#print(point_names)
    




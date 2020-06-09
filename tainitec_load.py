# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:07:45 2020

@author: Alfredo
"""

#!/usr/bin/python
#
# Copyright (c) 2018, 2019 TainiTec Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os.path
import numpy as np
from numpy import *
from initial_processes import *
import parameters
import os
import matplotlib.pyplot as plt
prm = parameters.Parameters()
from OpenEphys import *
import mne
import xlrd

number_of_channels = 16
sample_rate = 1000
sample_datatype = 'int16'
display_decimation = 10

"Specifiy the start time and end times here!!!!" 

start_time=600
end_time=900


fn="C:\\Users\\Alfredo\\Desktop\\Tainitec\\TAINI_1033_1240_Group2_5dpKA-2020_03_02-0000.dat"

def parse_dat(fn):
    '''Load a .dat file by interpreting it as int16 and then de-interlacing the 16 channels'''

    # Load the raw (1-D) data
    dat_raw = np.fromfile(fn, dtype=sample_datatype)

    # Reshape the (2-D) per channel data
    step = number_of_channels * display_decimation
    dat_chans = [dat_raw[c::step] for c in range(number_of_channels)]

    # Build the time array
    t = np.arange(len(dat_chans[0]), dtype=float) / sample_rate

    return dat_chans, t

dat_chans, t = parse_dat(fn)  
    
data=np.array(dat_chans)

del(dat_chans)





n_channels=16

channel_names=['hpc_mid_deep', 'hpc_mid_sup', 'hpc_ros_deep', 'hpc_ros_sup', 'pfc_deep', 
                       'pfc_sup', 'cx1', 'cx2', 'hpc_contra_deep', 'hpc_contra_sup', 
                       'EMG1', 'EMG2', 'cb_deep', 'cb_sup', 'hp_caudal_deep', 'hpc_caudal_sup']
channel_types=['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','eeg','eeg','eeg','eeg','eeg']
        
    
'This creates the info that goes with the channels, which is names, sampling rate, and channel types.'
info = mne.create_info(channel_names, prm.get_sampling_rate(), channel_types)


'This makes the object that contains all the data and info about the channels.'
'Computations like plotting, averaging, power spectrums can be performed on this object'

datatp=data.transpose()

del(data)

time_axis, sub_data = sub_time_data(datatp, start_time, end_time, sample_rate)

sub_datatp=sub_data.transpose()

custom_raw = mne.io.RawArray(sub_datatp, info)

'To do a basic plot below. The following can be added for specifc order of channels order=[4, 5, 3, 0, 1, 14, 15, 16]'
colors=dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
     emg='g', ref_meg='steelblue', misc='k', stim='b',
     resp='k', chpi='k')

custom_raw.plot(None, 5, 20, 8,color = colors, scalings = "auto", order=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], show_options = "true" )#



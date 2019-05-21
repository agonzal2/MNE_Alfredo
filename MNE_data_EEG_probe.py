 # -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:54:00 2018

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.QtWidgets import QWidget, QPushButton, QErrorMessage
from PyQt5.QtCore import pyqtSlot

from mainWindow import *

import glob
import os
from OpenEphys import *
import mne
from initial_processes import *
from numpy import *
from matplotlib import pyplot as plt
from mne.time_frequency import (tfr_multitaper, tfr_stockwell, tfr_morlet,
                                tfr_array_morlet)
from seizure_finder import *

from power_spectrum import *
import parameters

global w

prm = parameters.Parameters()

#prm.set_filepath('C:\\Users\\sulse\\Desktop\\Ingrid\\DATA\\OPEN EPHIS DATA\S7001_D2_2018-06-21_09-58-00\\')#C:\\Users\\sulse\\Desktop\\B_D3_2018-10-16_10-32-56\\'
prm.set_filepath('/media/jorge/Data/Jorge/DATA/OpenEphisData/S7001_D2_2018-06-21_09-58-00')
prm.set_filename('E17.txt')
#prm.set_excelpath('C:\\Users\\sulse\\Desktop\\Ingrid\DATA\\')
prm.set_excelpath('/media/jorge/Data/Jorge/DATA/')
prm.set_excelname('300_abs_thresh.xls') 
prm.set_channel_combo_name('Short_connections.xls') 
prm.set_sampling_rate(1000)
prm.set_sampling_rate(1000)
prm.set_sampling_rate(1000)
prm.set_starttime(1036) #using as experiment
prm.set_endtime(1046)   
prm.set_starttime2(994) #using as control.
prm.set_endtime2(1004)
prm.set_windowtype('hamming')
prm.set_stimfreq(10)
prm.set_channel_1(0)
prm.set_channel_2(1)
'Dictionary for color of traces'
colors=dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m', emg='g', ref_meg='steelblue', misc='k', stim='b', resp='k', chpi='k')


class MyForm(QDialog):
     def __init__(self):
          super().__init__()
          self.ui = Ui_Dialog()
          self.ui.setupUi(self)
          self.ui.ButtonSelectRawDataFolder.clicked.connect(self.getRawDataFolder)
          self.ui.ButtonLoadData.clicked.connect(self.loadData)
          self.ui.ButtonPlotRawData.clicked.connect(self.plotRawData)
          self.ui.ButtonFilterRawData.clicked.connect(self.filterRawData)
          self.ui.ButtonSelectSpreadSheet.clicked.connect(self.openSpreadSheet)
          self.ui.ButtonSpreadsheetTimes.clicked.connect(self.getSpecificTimes)
          self.ui.ButtonCalculateEpochs.clicked.connect(self.getEpochs)
          self.ui.ButtonPlotEpochs.clicked.connect(self.plotEpochs)
          # Error message (it is necessary to initialize it too)
          self.error_msg = QErrorMessage()
          self.error_msg.setWindowTitle("Error")
          self.show()

     
     def getRawDataFolder(self):
          foldername = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
          if foldername:
               AlfredoEEG.getRawDataFolder(foldername)
     
     '(1) Function below loads the data and makes the MNE data object '
     def loadData(self):
          if AlfredoEEG.rawDataFolder:
               AlfredoEEG.load_raw_data()
          else: 
               self.error_msg.showMessage("It is necessary to select an folder")
     
     def LoadingDataProgress(self, progress):
          self.progressRawDataLoading.setValue(progress)

     def plotRawData(self):
          AlfredoEEG.plotRawData()          

     def filterRawData(self):
          AlfredoEEG.filterRawData()          
     
     def openSpreadSheet(self):
          options = QFileDialog.Options()
          filename, _ = QFileDialog.getOpenFileName(self,"Select Spreadsheet", "", "Excel files (*.xls)", options=options)
          if filename:
               AlfredoEEG.loadSpecificTimesFile(filename)
     
     def getSpecificTimes(self):
          if AlfredoEEG.filename:
               AlfredoEEG.getSpecificTimes()
          else:
               self.error_msg.showMessage("It is necessary to select an .xls File")

     def getEpochs(self):
          AlfredoEEG.getEpochs()

     def plotEpochs(self):
          AlfredoEEG.plotEpochs()

class eeg32 ():
     custom_raw = []
     specificTimes = []
     stimatedTimes = []
     epochs = []
     evoked = []     

     def __init__(self, custom_raw=[], specificTimes=[], stimatedTimes=[], epochs=[], evoked=[]):
          self.custom_raw=custom_raw
          self.specificTimes=specificTimes
          self.stimatedTimes=stimatedTimes
          self.filename = ""
          self.rawDataFolder = ""
     
     def getRawDataFolder(self, folder):
          self.rawDataFolder = folder
     
     def load_raw_data(self):
          self.custom_raw=load_32_EEG(self.rawDataFolder)
     
     def plotRawData(self):
          self.custom_raw.plot(None, 5, 20, 8,color = colors, scalings = "auto", order=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,
                                           14,15,16,32,17,18,19,20,21,22,
                                           23,24,25,26,27,28,29,30,31,32], show_options = "true" )

     def loadSpecificTimesFile(self, filename):
          self.filename = filename

     # (3) If you have specific times to analyse, load excel spreadsheet of them below.
     def getSpecificTimes(self):
          self.specificTimes=import_spreadsheet(self.filename) #Imports spreadsheet
          self.stimatedTimes=create_epochs(self.specificTimes, prm.get_sampling_rate()) #Creates stim time array that MNE can read.
     
     def getRawData(self):
          return self.custom_raw
     
     def getEpochs(self):
          self.epochs=mne.Epochs(self.custom_raw, self.stimatedTimes, baseline= None, detrend=None, tmin=-2, tmax=3)

     def plotEpochs(self):
          # picks =[14, 15]
          '(5) Functions for evoked plots '
          self.evoked = self.epochs.average().pick_types(eeg=True, emg=True) #to average epochs.
          self.evoked.plot([0], time_unit='s') #to plot these epochs, first array is channel number.  
     
     def filterRawData(self):
          filt.plot(None, 5, 20, 8,color = colors, scalings = "auto", order=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,
                                    14,15,16,32,17,18,19,20,21,22,
                                    23,24,25,26,27,28,29,30,31,32], show_options = "true" )#

     
AlfredoEEG = eeg32()

if __name__=="__main__":
     app = QApplication(sys.argv)
     w = MyForm()
     w.show
     
     sys.exit(app.exec())

'Initialize the parameters'
#init_params()


'This is if brain state epoch array is available'
#analysis_times=import_brain_state(prm.get_excelpath() + prm.get_excelname())
'This is if channel combination array is available for coherence is cross-frequency coupling analyses'
#channel_combo=import_channel_combo(prm.get_excelpath() + prm.get_channel_combo_name())

'Creates epoch file. Creates epochs from analysis times.'
#event_id = {'Wake': 0, 'NREM': 1, 'REM':2, 'Trans':3}
#stim=create_brain_state_epochs(analysis_times,  prm.get_sampling_rate())
'This below adds the epochs to the object.'


'Still need to get correct channels and maybe a bit more threshold'
#epochs.plot(n_epochs=1, picks=[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 32], block=True, scalings= 'auto') #block episodes. 
#evoked.plot_topomap(times=np.linspace(0, 0.5, 2), ch_type='mag', time_unit='s')
#evoked= epochs.average().pick_types(eeg=True)
#evoked.plot_topomap(times=np.linspace(0, 0.5, 2), ch_type='mag', time_unit='s')
'This is to make MNE array of filtered data through MNE filt function.'
#filt=custom_raw.filter(1, 200, fir_design='firwin')
'This below is a function to get seizure epochs.'
#stimulations= seizure_times(15, filt,  prm.get_sampling_rate(), 5)   
#sub_data1, times =filt[15, 0:21960704]
#
#plt.plot(data_abs[0])
#plt.plot(300)
'To do a basic plot below. The following can be added for specifc order of channels order=[4, 5, 3, 0, 1, 14, 15, 16]'

#
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
#plt.tight_layout() """



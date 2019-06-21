 # -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:54:00 2018

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
import sys
from datetime import datetime
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
import matplotlib.backends.backend_pdf
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
          self.ui.ButtonLoadData.clicked.connect(self.loadData)
          self.ui.ButtonPlotRawData.clicked.connect(self.plotRawData)
          self.ui.ButtonFilterRawData.clicked.connect(self.filterRawData)
          self.ui.ButtonGetEpochs.clicked.connect(self.getEpochs)
          self.ui.ButtonPlotEpochsAverage.clicked.connect(self.plotEpochsAverage)
          self.ui.ButtonPlotEpochs.clicked.connect(self.plotEpochs)
          self.ui.ButtonPlotSingleTopomap.clicked.connect(self.plotSingleTopomap)
          self.ui.ButtonPlotTopomapBetweenEvoked.clicked.connect(self.plotMultipleEpochsTopomap)
          self.ui.SliderSingleTopomap.valueChanged.connect(self.SingleEvokedSliderTopomap)
          self.ui.spinBoxSingleTopomap.valueChanged.connect(self.SingleEvokedForTopomap)
          self.ui.SliderInitialTopomap.valueChanged.connect(self.InitialEvokedSliderTopomap)
          self.ui.spinBoxInitialTopomap.valueChanged.connect(self.InitialEvokedForTopomap)
          self.ui.SliderFinalTopomap.valueChanged.connect(self.FinalEvokedSliderTopomap)
          self.ui.spinBoxFinalTopomap.valueChanged.connect(self.FinalEvokedForTopomap)
          self.ui.doubleSpinBoxTmin.valueChanged.connect(self.EpochMinTime)
          self.ui.doubleSpinBoxTmax.valueChanged.connect(self.EpochMaxTime)
          self.ui.SpinBoxInitialTimeTopomap.valueChanged.connect(self.InitialTimeTopomap)
          self.ui.SpinBoxFinalTimeTopomap.valueChanged.connect(self.FinalTimeTopomap)
          self.ui.SpinBoxIntervalTopomap.valueChanged.connect(self.TimeIntervalTopomap)
          self.ui.doubleSpinBoxVmax.valueChanged.connect(self.VmaxTopomap)
          self.ui.doubleSpinBoxVmin.valueChanged.connect(self.VminTopomap)
          self.ui.radioButtonChNames.toggled.connect(self.ShowChannelNames)
          self.ui.radioButtonBoundary.toggled.connect(self.ShowOutlines)
          self.ui.ButtonClearFigures.clicked.connect(self.closeFigures)
          self.ui.spinBoxTopoSize.valueChanged.connect(self.TopomapSize)
          self.ui.spinBoxContours.valueChanged.connect(self.Contours)
          self.ui.Button2PDF.clicked.connect(self.print2pdf)
          self.ui.Button2PNG.clicked.connect(self.print2png)
          # Error message (it is necessary to initialize it too)
          self.error_msg = QErrorMessage()
          self.error_msg.setWindowTitle("Error")
          self.show()


     '(1) Function below loads the data and makes the MNE data object '
     def loadData(self):
          AlfredoEEG.rawDataFolder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
          if AlfredoEEG.rawDataFolder:
               AlfredoEEG.load_raw_data()
               self.ui.ButtonPlotRawData.setEnabled(True)
               self.ui.ButtonFilterRawData.setEnabled(True)
               self.ui.frameEpochs.setEnabled(True)
               self.ui.ButtonPlotEpochs.setEnabled(False)
               self.ui.ButtonPlotEpochsAverage.setEnabled(False)
          else:
               self.error_msg.showMessage("It is necessary to select a folder")

     def plotRawData(self):
          AlfredoEEG.plotRawData()

     def filterRawData(self):
          AlfredoEEG.filterRawData()

     def getEpochs(self):
          options = QFileDialog.Options()
          AlfredoEEG.filename, _ = QFileDialog.getOpenFileName(self,"Select Spreadsheet", "", "Excel files (*.xls)", options=options)
          if AlfredoEEG.filename:
               AlfredoEEG.getSpecificTimes()
               self.ui.ButtonPlotEpochs.setEnabled(True)
               self.ui.ButtonPlotEpochsAverage.setEnabled(True)
               self.ui.framePlottingEvoked.setEnabled(True)
               self.ui.spinBoxSingleTopomap.setMaximum(AlfredoEEG.specificTimes.shape[0])
               self.ui.spinBoxInitialTopomap.setMaximum(AlfredoEEG.specificTimes.shape[0])
               self.ui.spinBoxFinalTopomap.setMaximum(AlfredoEEG.specificTimes.shape[0])
               self.ui.SliderSingleTopomap.setMaximum(AlfredoEEG.specificTimes.shape[0])
               self.ui.SliderInitialTopomap.setMaximum(AlfredoEEG.specificTimes.shape[0])
               self.ui.SliderFinalTopomap.setMaximum(AlfredoEEG.specificTimes.shape[0])
               self.ui.spinBoxFinalTopomap.setValue(AlfredoEEG.specificTimes.shape[0])

          else:
               self.error_msg.showMessage("It is necessary to select a .xls File")

     def plotEpochs(self):
          AlfredoEEG.plotEpochs(AlfredoEEG.specificTimes.shape[0], self.ui.doubleSpinBoxTmin.value(),
                                        self.ui.doubleSpinBoxTmax.value())

     def plotEpochsAverage(self):
          AlfredoEEG.plotEpochsAverage(0, AlfredoEEG.specificTimes.shape[0], True, self.ui.doubleSpinBoxTmin.value(),
                                        self.ui.doubleSpinBoxTmax.value())

     def plotSingleTopomap(self):
          AlfredoEEG.plotSingleTopomap(self.ui.spinBoxSingleTopomap.value(), self.ui.doubleSpinBoxVmax.value(), 
                                        self.ui.doubleSpinBoxVmin.value(), self.ui.SpinBoxInitialTimeTopomap.value(),
                                        self.ui.SpinBoxFinalTimeTopomap.value(), self.ui.SpinBoxIntervalTopomap.value(),
                                        self.ui.spinBoxTopoSize.value(), self.ui.spinBoxContours.value())

     def plotMultipleEpochsTopomap(self):
          AlfredoEEG.plotMultipleEpochsTopomap(self.ui.spinBoxInitialTopomap.value(), self.ui.spinBoxFinalTopomap.value(), 
                                                  self.ui.doubleSpinBoxVmax.value(), self.ui.doubleSpinBoxVmin.value(),
                                                  self.ui.SpinBoxInitialTimeTopomap.value(), self.ui.SpinBoxFinalTimeTopomap.value(), 
                                                  self.ui.SpinBoxIntervalTopomap.value(), self.ui.spinBoxTopoSize.value(),
                                                  self.ui.spinBoxContours.value())
     
     def ShowChannelNames(self):
          AlfredoEEG.showChNames = self.ui.radioButtonChNames.isChecked()
     
     def ShowOutlines(self):
          AlfredoEEG.showOutlines(self.ui.radioButtonBoundary.isChecked())

     def SingleEvokedSliderTopomap(self, value):
          self.ui.spinBoxSingleTopomap.setValue(value)

     def SingleEvokedForTopomap(self, value):
          self.ui.SliderSingleTopomap.setValue(value)

     def FinalEvokedSliderTopomap(self, value):
          self.ui.spinBoxFinalTopomap.setValue(value)

     def FinalEvokedForTopomap(self, value):
          self.ui.SliderFinalTopomap.setValue(value)

     def InitialEvokedSliderTopomap(self, value):
          self.ui.spinBoxInitialTopomap.setValue(value)

     def InitialEvokedForTopomap(self, value):
          self.ui.SliderInitialTopomap.setValue(value)
     
     def VmaxTopomap(self, value):
          self.ui.doubleSpinBoxVmax.setValue(value)
     
     def VminTopomap(self, value):
          self.ui.doubleSpinBoxVmin.setValue(value)

     def EpochMinTime(self, value):
          self.ui.doubleSpinBoxTmin.setValue(value)
          self.ui.SpinBoxInitialTimeTopomap.setMinimum(value)
          self.ui.SpinBoxFinalTimeTopomap.setMinimum(value)

     def EpochMaxTime(self, value):
          self.ui.doubleSpinBoxTmax.setValue(value)
          self.ui.SpinBoxInitialTimeTopomap.setMaximum(value)
          self.ui.SpinBoxFinalTimeTopomap.setMaximum(value)
     
     def InitialTimeTopomap(self, value):
          self.ui.SpinBoxInitialTimeTopomap.setValue(value)
          self.forceIntervalInRange()

     def FinalTimeTopomap(self, value):
          self.ui.SpinBoxFinalTimeTopomap.setValue(value)
          self.forceIntervalInRange()
     
     def TimeIntervalTopomap(self, value):
          self.ui.SpinBoxIntervalTopomap.setValue(value)
          self.forceIntervalInRange()
     
     def forceIntervalInRange(self):
          range = self.ui.SpinBoxFinalTimeTopomap.value() - self.ui.SpinBoxInitialTimeTopomap.value()
          # mne restricts the number of topomaps than can be plotted in a single figure to 19
          if self.ui.SpinBoxIntervalTopomap.value() < (range/19):
               self.ui.SpinBoxIntervalTopomap.setValue(range/19)

     
     def TopomapSize(self, value):
          self.ui.spinBoxTopoSize.setValue(value)
     
     def Contours(self,value):
          self.ui.spinBoxContours.setValue(value)
     
     def closeFigures(self):
          plt.close('all')
     
     def print2pdf(self):          
          AlfredoEEG.figFolder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
          if AlfredoEEG.figFolder:
               filename = '/' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.pdf'           
               pdf = matplotlib.backends.backend_pdf.PdfPages(AlfredoEEG.figFolder + filename)
               figs = [plt.figure(n) for n in plt.get_fignums()]
               for fig in figs:
                    fig.savefig(pdf, format='pdf')
               pdf.close()
          else:
               self.error_msg.showMessage("It is necessary to select a folder")
     
     def print2png(self):
          AlfredoEEG.figFolder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
          if AlfredoEEG.figFolder:
               prefix = '/' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
               for i in plt.get_fignums():
                    plt.figure(i)
                    plt.savefig(AlfredoEEG.figFolder + prefix +'figure%d.png' % i)
          else:
               self.error_msg.showMessage("It is necessary to select a folder")
          


class eeg32 ():
     custom_raw = []
     specificTimes = []
     stimatedTimes = []
     epochs = []
     evoked = []
     showChNames = False
     outlines = 'head'

     def __init__(self, custom_raw=[], specificTimes=[], stimatedTimes=[], epochs=[], evoked=[]):
          self.custom_raw=custom_raw
          self.specificTimes=specificTimes
          self.stimatedTimes=stimatedTimes
          self.filename = ""
          self.rawDataFolder = ""
          self.figFolder = ""
          self.alfredo_layout = mne.channels.read_layout('Alfredo32h', scale=False)
          #mne.viz.plot_layout(self.alfredo_layout, show= True)
          #self.alfredoMontage = mne.channels.read_montage('standard_32Tcm_Alfredo')
          #self.evoked.set_montage(self.alfredoMontage)

     def load_raw_data(self):
          self.custom_raw=load_32_EEG(self.rawDataFolder)

     def plotRawData(self):
          self.custom_raw.plot(None, 5, 20, 8,color = colors, scalings = "auto", order=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,
                                           14,15,16,32,17,18,19,20,21,22,
                                           23,24,25,26,27,28,29,30,31,32], show_options = "true" )

     # (3) If you have specific times to analyse, load excel spreadsheet of them below.
     def getSpecificTimes(self):
          self.specificTimes=import_spreadsheet(self.filename) #Imports spreadsheet

     def getRawData(self):
          return self.custom_raw

     def calculateEvokedTimes(self, initialEvoked, finalEvoked, tMin, tMax):
          self.stimatedTimes=create_epochs(self.specificTimes[initialEvoked:finalEvoked], prm.get_sampling_rate()) #Creates stim time array that MNE can read.
          self.epochs=mne.Epochs(self.custom_raw, self.stimatedTimes, baseline= None, detrend=None, tmin=tMin, tmax=tMax)
          self.evoked = self.epochs.average().pick_types(eeg=True, emg=True) #to average epochs.

     def plotEpochsAverage(self, Initial, Final, fromAverageButton=False, tMin=-2, tMax=4):
          # picks =[14, 15]
          if fromAverageButton is True:
               self.calculateEvokedTimes(Initial, Final, tMin, tMax)
          self.evoked.plot(time_unit='s') #to plot these epochs, first array is channel number.

     def plotEpochs(self, Final, tMin, tMax):
          self.calculateEvokedTimes(0, Final, tMin, tMax)
          self.epochs.plot(n_epochs=1, picks=[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 32], block=True, scalings= 'auto') #block episodes.
     
     def showOutlines(self, showHead=True):
          if showHead:                
               self.outlines = 'head'
          else:
               self.outlines = None

     def plotSingleTopomap(self, evockedNumber, vMax=80, vMin=-80, initTime=-0.1, endTime=0.21, interval=0.05, topoSize=2, contours=6):
          self.calculateEvokedTimes(evockedNumber, evockedNumber+1, initTime, endTime)
          self.plotEpochsAverage(False, evockedNumber, evockedNumber+1, initTime, endTime)
          times = np.arange(initTime, endTime, interval)
          plotTitle = 'Epoch # ' + str(evockedNumber)
          self.evoked.plot_topomap(times, layout=self.alfredo_layout, vmax=vMax*10e6, vmin=vMin*10e6, size=topoSize, time_unit='s', 
                                        show_names = self.showChNames, title = plotTitle, outlines=self.outlines, contours=contours)          
               

     def plotMultipleEpochsTopomap(self, InitialEvoked, FinalEvoked, vMax=80, vMin=-80, initTime=-0.1, endTime=0.21, interval=0.05, topoSize=2, contours=6):
          self.calculateEvokedTimes(InitialEvoked, FinalEvoked, initTime, endTime)
          self.plotEpochsAverage(False, InitialEvoked, FinalEvoked, initTime, endTime)
          times = np.arange(initTime, endTime, interval)
          plotTitle = 'Epochs from '+ str(InitialEvoked) +' to '+ str(FinalEvoked)
          self.evoked.plot_topomap(times, layout=self.alfredo_layout, vmax=vMax*10e6, vmin=vMin*10e6, size=topoSize, time_unit='s', 
                                        show_names = self.showChNames, title = plotTitle, outlines=self.outlines, contours=contours)

     def filterRawData(self):
          self.filt=self.custom_raw.filter(1, 200, fir_design='firwin')
          self.filt.plot(None, 5, 20, 8,color = colors, scalings = "auto", order=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,
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


#self.evoked.plot_topomap(times, sensors=True, time_unit='s', title = 'without sensors', head_pos=dict(center=(0,0), scale=(70,70)))
          #self.evoked.plot_topomap(times, time_unit='s', title = 'just center', head_pos=dict(center=(0,0)))
          #self.evoked.plot_topomap(times, time_unit='s')
          #self.evoked.plot_topomap(layout='Alfredo32', time_unit='s', title = 'with Layout')
          #self.evoked.plot_topomap(times, time_unit='s', title = 'without head', head_pos=dict(center=(0,0), scale=(7,7)))
          #self.evoked.plot_topomap(times, time_unit='s', title = 'without head 70', head_pos=dict(center=(0,0), scale=(70,70)))
          #self.evoked.plot_topomap(times, time_unit='s', title = 'Without outlines. '+plotTitle, outlines=None, head_pos=dict(center=(0,0), scale=(70,70)))
          
          
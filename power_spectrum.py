# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:09:44 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""

import matplotlib.pyplot as plt
from numpy import *
import scipy.fftpack
from scipy import signal
import parameters
from initial_processes import *
prm = parameters.Parameters()


def psd(sub_data, windowtype, samplingrate) :  # Calculates PSD, plots it.
    


    window=scipy.signal.get_window(windowtype, samplingrate)
    f, Pxx_den = signal.periodogram(sub_data, samplingrate, window, samplingrate)
    psd=plt.semilogy(f, sqrt(Pxx_den), 'k')
    plt.xlim([0, 100])
    x=[0, 100]
    plt.xticks(arange(min(x), max(x), 10.0), size=10)
    ##plt.ticklabel_format(x, fontsize=1000)
    ##plt.font_manager.FontProerties()
    plt.ylim([1e-1, 1e2])
    plt.yticks(size=10)
    #plt.legend(handles=[psd1, psd2], loc=0)
    #for label in ax.get_xticklabels():
    #   label.set_color('r')
    plt.xlabel('Frequency [Hz]', fontsize=40)
    plt.ylabel('PSD [V**2/Hz]', fontsize=40)
    plt.show()
    
    return

def psd_2chan (sub_data1, sub_data2, windowtype, samplingrate, stimfreq) :  # Calculates PSD, plots it, saves it
    
    

    window=scipy.signal.get_window(windowtype, samplingrate)
    f, Pxx_den = signal.periodogram(sub_data1, samplingrate, window, samplingrate)
    psd=plt.semilogy(f, sqrt(Pxx_den), 'b')
    
    window=scipy.signal.get_window(windowtype, samplingrate)
    f, Pxx_den = signal.periodogram(sub_data2, samplingrate, window, samplingrate)
    psd=plt.semilogy(f, sqrt(Pxx_den), 'k')
    plt.axvline(x=stimfreq)
    
    
    
    
    plt.xlim([0, 25])
    x=[0, 25]
    plt.xticks(arange(min(x), max(x), 1.0), size=10)
    ##plt.ticklabel_format(x, fontsize=1000)
    ##plt.font_manager.FontProerties()
    plt.ylim([1, 1e2])
    plt.yticks(size=10)
    #plt.legend(handles=[psd1, psd2], loc=0)
    #for label in ax.get_xticklabels():
    #   label.set_color('r')
    plt.xlabel('Frequency [Hz]', fontsize=5)
    plt.ylabel('PSD [V**2/Hz]', fontsize=5)
    plt.show()
    plt.savefig(str(prm.get_excelpath()) + str(prm.get_excelname()) + str(prm.get_starttime())+ 'and'+ str(prm.get_starttime2())+'.png')
    plt.close()
    return

def multiple_psds(analysis_times, data): #Plots PSDs at multiple times when fed in an excel spreadsheet.
       
    
    num_rows, num_cols=analysis_times.shape
    for n in range(0, num_rows):
        start_time=(analysis_times.item(n,0))
        prm.set_starttime(start_time) #using as experiment
        end_time=(analysis_times.item(n,1))
        prm.set_endtime(end_time)   
        start_time2=(analysis_times.item(n,2))
        prm.set_starttime2(start_time2) #using as control.
        end_time2=(analysis_times.item(n,3))
        prm.set_endtime2(end_time2)
        stimfreq=(analysis_times.item(n,4))
        prm.set_stimfreq(stimfreq)
 
        time_axis, sub_data1=sub_time_data(data, prm.get_starttime(), prm.get_endtime(), prm.get_sampling_rate())
#########get sub-data with time


        time_axis, sub_data2=sub_time_data(data, prm.get_starttime2(), prm.get_endtime2(), prm.get_sampling_rate())

       
        psd_2chan(sub_data1, sub_data2, prm.get_windowtype(), prm.get_sampling_rate(), prm.get_stimfreq())
        
        
        
#        print(start_time, end_time, start_time2, end_time2)
    return
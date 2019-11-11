
"""
Created on Wed Nov 22 16:09:44 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
import mne
import matplotlib.pyplot as plt
from numpy import *
import scipy.fftpack
from scipy import signal
import parameters
from scipy.signal import coherence
import xlsxwriter
import pandas as pd
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
#Unable to merge"
def psd_entrainment_data (sub_data, windowtype, samplingrate, stimfreq) :  # Calculates PSD, plots it, saves it
    
    window=scipy.signal.get_window(windowtype, samplingrate)
    f, Pxx_den = signal.periodogram(sub_data, samplingrate, window, samplingrate)
    stimpower= Pxx_den[int(stimfreq)]+Pxx_den[int(stimfreq-1)]+Pxx_den[int(stimfreq+1)]
    
#    print(stimfreq)
#    print(Pxx_den[int(stimfreq)])
#    print(stimfreq-1)
#    print(Pxx_den[int(stimfreq-1)])
#    print(stimfreq+1)
#    print(Pxx_den[int(stimfreq+1)])

    cumulativepower=Pxx_den[2]+Pxx_den[3]+Pxx_den[4]+Pxx_den[5]+Pxx_den[6]+Pxx_den[7]+Pxx_den[8]+Pxx_den[9]+Pxx_den[10]+Pxx_den[11]+Pxx_den[12]
    entrainmentratio=stimpower/cumulativepower
    

    return entrainmentratio
    
def psd_theta_delta(sub_data1, sub_data2, windowtype, samplingrate, stimfreq) :  # Calculates PSD, plots it, saves it
    
    

    window=scipy.signal.get_window(windowtype, samplingrate)
    f, Pxx_den = signal.periodogram(sub_data1, samplingrate, window, samplingrate)
    thetapower= Pxx_den[4]+Pxx_den[5]+Pxx_den[6]+Pxx_den[7]+Pxx_den[8]+Pxx_den[9]+Pxx_den[10]+Pxx_den[11]+Pxx_den[12]
    deltapower=Pxx_den[0]+Pxx_den[1]+Pxx_den[2]+Pxx_den[3]
    thetaoverdelta=thetapower/deltapower
    

    
#    window=scipy.signal.get_window(windowtype, samplingrate)
#    f, Pxx_den = signal.periodogram(sub_data2, samplingrate, window, samplingrate)

    return thetaoverdelta

'Function below calculates and plots coherence between 2 channels at 2 data points'
def ind_coherence(sub_data1, sub_data2, sub_data3, sub_data4, samplingrate, stimfreq):

    wind=scipy.signal.get_window("hann", prm.get_sampling_rate()*2) ###2 second window.

    f, coh = coherence(sub_data1, sub_data2, fs=prm.get_sampling_rate(), window=wind) ##window overlap is half. 
    #Here we are using coherence function from numpy and setting paramters previously used.
    
    #betlow we setup the plot along with stimulation line, which is optogenetics stim.
    plt.xlim([0, 15])
    plt.axvline(x=stimfreq)
    plt.plot(f, coh[0,:], lw=1.)
    
    #Coherence calculation for second data set below.
    f, coh = coherence(sub_data3, sub_data4, fs=prm.get_sampling_rate(), window=wind) 
    plt.plot(f, coh[0,:], lw=1.)
    plt.show()
    plt.savefig(str(prm.get_excelpath()) + str(prm.get_excelname()) + str(prm.get_starttime())+ 'and'+ str(prm.get_starttime2())+'.png')
    plt.close()
    return


'Function below is to get coherence data for a particular set of data.'
def coherence_values(sub_data1, sub_data2, samplingrate):  ##Get data points of coherence values.

    wind=scipy.signal.get_window("hann", prm.get_sampling_rate()*2) ###2 second window.
    
    #Using numpy coherence function to get this.
    f, coh = coherence(sub_data1, sub_data2, fs=prm.get_sampling_rate(), window=wind) ##window overlap is half. 
    
    return f, coh  ###return coherence and corresponding frequencies.


'Large function to calculate individual coherence for individual time windows and channel combinations in multi-channel recording'
def global_coherence(analysis_times, channel_combo, custom_raw):  ##Do individual coherence for series of channels.
    #Analysis times is times to compare, see brain state function and channel combo function.
    
    cc_num_rows, cc_num_cols=channel_combo.shape  #Here getting size of channel combination array.
    at_num_rows, at_num_cols=analysis_times.shape  #Get size of analysis times array.
    coh_array = zeros(shape=((at_num_rows)*(cc_num_rows), 1001)) #Make array of zeros to put data in.
  

#    print(at_num_rows)
#    print(cc_num_rows)
 
    
    for m in range(0, at_num_rows): #For loop to run through all analyis stimes.

        start_time=(analysis_times.item(m,1))
        prm.set_starttime(start_time)
        end_time=(analysis_times.item(m,2))
        prm.set_endtime(end_time)
      
       
        
        for n in range(0, cc_num_rows):  #For loop to run through all channel combinations.
            
            chan_1=(channel_combo.item(n,0))
            prm.set_channel_1(int(chan_1)) 
            chan_2=(channel_combo.item(n,1))
            prm.set_channel_2(int(chan_2))
            
            #Below is an MNE function to get index from data object.
            t_idx=custom_raw.time_as_index([prm.get_starttime(), prm.get_endtime()])
            sub_data1, times =custom_raw[prm.get_channel_1(), t_idx[0]:t_idx[1]] #Here retrieve specified indexed and channel data/
            sub_data2, times =custom_raw[prm.get_channel_2(), t_idx[0]:t_idx[1]]
               
            f, coh=coherence_values(sub_data1, sub_data2, prm.get_sampling_rate) #use coherence_values function to get coherence.
            coh_array_index=int(n+cc_num_rows*m)  #Figure out index of where to place data,
            coh_array[coh_array_index,:]=coh

        print('Calculating global coherence')
    coh_average=average(coh_array, 0) #Calculate averages and STDs which will be returned,
    coh_std=std(coh_array, 0)

    #Below writes and saves the calculated array into a spreadsheet.
#    row=0
#    workbook = xlsxwriter.Workbook(str(prm.get_excelpath()) + str(prm.get_excelname()) + str(prm.get_channel_combo_name())+ '_coherence.xls')
#    worksheet = workbook.add_worksheet()
#    
#    for col, data in enumerate(coh_array):
#        worksheet.write_column(row, col, data)
#        
#    workbook.close()
    
    #Below writes and saves the calculated arrray AVERAGE into a spreadsheet.
#    row=0
#    workbook = xlsxwriter.Workbook(str(prm.get_excelpath()) + str(prm.get_excelname()) + str(prm.get_channel_combo_name())+ '_coherence_avg.xls')
#    worksheet = workbook.add_worksheet()
#    
#    for col, data in enumerate(coh_average):
#        worksheet.write_column(row, col, data)
#        
#    workbook.close()
    
    
    

   
    return coh_average, coh_std, f

    
            
def multiple_coherence(analysis_times, custom_raw):
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
 
    
        t_idx=custom_raw.time_as_index([prm.get_starttime(), prm.get_endtime()])
        sub_data1, times =custom_raw[32, t_idx[0]:t_idx[1]]
        sub_data2, times =custom_raw[40,t_idx[0]:t_idx[1]]
        
        t_idx=custom_raw.time_as_index([prm.get_starttime2(), prm.get_endtime2()])
        sub_data3, times =custom_raw[32, t_idx[0]:t_idx[1]]
        sub_data4, times =custom_raw[34,t_idx[0]:t_idx[1]]
     
        
        ind_coherence(sub_data1, sub_data2, sub_data3, sub_data4, prm.get_sampling_rate(), prm.get_stimfreq())
     
    return  

"Function below calculates coherence from two channels at one data point"
def coherence_data(analysis_times, data1, data2):
    num_rows, num_cols=analysis_times.shape
    
    coherenceresults= zeros([num_rows])
    
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
        
        time_axis, sub_data1=sub_time_data(data1, prm.get_starttime(), prm.get_endtime(), prm.get_sampling_rate())

        time_axis, sub_data2=sub_time_data(data2, prm.get_starttime(), prm.get_endtime(), prm.get_sampling_rate())

        f, coh=coherence_values(sub_data1, sub_data2, prm.get_sampling_rate())
        
        coh_index=int(stimfreq)
        
        coh_index_low=int(stimfreq-1)

        
        coh_index_high=int(stimfreq+1)

        
        coh_mid=coh[coh_index]
        coh_low=coh[coh_index_low]
        coh_high=coh[coh_index_high]
        
        coh_total=coh_mid+coh_low+coh_high
        
        coherenceresults[n]=coh_total


    return coherenceresults

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
        
    
     
    return

'This calculates the entrainment ratio'
'Select whether it is pre-stim time or stim time by writing in string'
 
def multiple_entrainmentratio(analysis_times, data, stim): #Plots PSDs at multiple times when fed in an excel spreadsheet.
       
    #Get number of analysis epochs
    num_rows, num_cols=analysis_times.shape
    
    entrainmentresults= zeros([num_rows])
    
#    if stim == 'pre-stim':
        
  
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
        
            
        time_axis, sub_data1=sub_time_data(data, prm.get_starttime2(), prm.get_endtime2(), prm.get_sampling_rate())

        entrainmentratio = psd_entrainment_data(sub_data1, prm.get_windowtype(), prm.get_sampling_rate(), prm.get_stimfreq())
        entrainmentresults[n]=entrainmentratio
       
#    if stim == 'stim':
        
  
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
        
            
        time_axis, sub_data=sub_time_data(data, prm.get_starttime(), prm.get_endtime(), prm.get_sampling_rate())


        entrainmentratio = psd_entrainment_data(sub_data, prm.get_windowtype(), prm.get_sampling_rate(), prm.get_stimfreq())
        entrainmentresults[n]=entrainmentratio
       
    
     
    return entrainmentresults


'Below calculates entrainment ratio before and after stimulation for that duration and makes a plot'

def multiple_entrainmentratio_with_plots(stimulations, data, stim_duration): #Plots PSDs at multiple times when fed in an excel spreadsheet.
       
    #Get number of analysis epochs
    numberstim=len(stimulations)
    
    entrainmentresults= zeros([numberstim, 2])

    channels=prm.get_headstages()*16
    
    entrainment_prestim_array=zeros([numberstim, channels])
    entrainment_stim=zeros([numberstim, channels])
    
    channel_names=['0', 'hpc_mi', 'hpc_ros_deep', 'hpc_ros_sup', 'pfc_deep', 
               'pfc_sup', 'cx1', 'cx2', 'hpc_contra_deep', 'hpc_contra_sup', 
               'EMG1', 'EMG2', 'cb_deep', 'cb_sup', 'hp_caudal_deep', 'hpc_caudal_sup',
               'hpc_mid_d_2', 'hpc_mid_s_2', 'hpc_ros_d_2', 'hpc_ros_s_2', 'pfc_d_2', 
               'pfc_sup_2', 'cx1_2', 'cx2_2', 'hpc_ct_d_2', 'hpc_ct_s_2', 
               'EMG1_2', 'EMG2_2', 'cb_deep_2', 'cb_sup_2', 'hp_caud_d_2', 'hpc_caud_s_2',
               'hpc_mid_d_3', 'hpc_mid_s_3', 'hpc_ros_d_3', 'hpc_ros_s_3', 'pfc_d_3', 
               'pfc_s_3', 'cx1_3', 'cx2_3', 'hpc_ct_d_3', 'hpc_ct_s_3', 
               'EMG1_3', 'EMG2_3', 'cb_deep_3', 'cb_sup_3', 'hp_c_d_3', 'hpc_c_s_3',
               'hpc_mid_d_4', 'hpc_mid_s_4', 'hpc_ros_d_4', 'hpc_ros_s_4', 'pfc_d_4', 
               'pfc_s_4', 'cx1_4', 'cx2_4', 'hpc_ct_d_4', 'hpc_ct_s_4', 
               'EMG1_4', 'EMG2_4', 'cb_deep_4', 'cb_sup_4', 'hp_c_d_4', 'hpc_c_s_4','opto']
    
  
    
    
    
    
    
    for t in range(0, channels):
        
        for n in range(0, numberstim):
            
            'Entrainment during stimulation'
            start_time=stimulations[n]
            prm.set_starttime(start_time) #using as experiment
            end_time=stimulations[n]+stim_duration
            prm.set_endtime(end_time)
                
            time_axis, sub_data=sub_time_data(data[:,t], prm.get_starttime(), prm.get_endtime(), prm.get_sampling_rate())
            entrainmentratio = psd_entrainment_data(sub_data, prm.get_windowtype(), prm.get_sampling_rate(), prm.get_stimfreq())
            entrainmentresults[n,1]=entrainmentratio
            
            entrainment_stim[n,t]=entrainmentratio
            
            'Entrainment before stimulation'
            end_time=stimulations[n]
            prm.set_endtime(end_time)
            start_time=stimulations[n]-stim_duration
            prm.set_starttime(start_time) #using as experiment
            
            time_axis, sub_data=sub_time_data(data[:,t], prm.get_starttime(), prm.get_endtime(), prm.get_sampling_rate())
            entrainmentratio = psd_entrainment_data(sub_data, prm.get_windowtype(), prm.get_sampling_rate(), prm.get_stimfreq())
            entrainmentresults[n,0]=entrainmentratio
        
            entrainment_prestim_array[n,t]=entrainmentratio
            
        fig, ax = plt.subplots()
        x0=full(len(entrainmentresults), 0.5)
        x1=full(len(entrainmentresults), 1)
        
        scatter=ax.scatter(x0, entrainmentresults[:,0], c='k')
        scatter=ax.scatter(x1, entrainmentresults[:,1], c='b')
        plt.ylim(0,1)
        plt.title(str(channel_names[t]))
        plt.savefig(str(prm.get_filepath()) +'_Channel_'+ str(t)+'.png')
        plt.close()
            
    pandas_stim_array = pd.DataFrame(entrainment_stim)
    pandas_prestim_array=pd.DataFrame(entrainment_prestim_array)
    
    
    filepath= str(prm.get_filepath()) + "Entrainment_Numbers_per_Channel_Stim_noSTim.xlsx"
    
    with pd.ExcelWriter(filepath) as writer:
        
        pandas_stim_array.to_excel(writer, sheet_name="Stim_entrain") 
        pandas_prestim_array.to_excel(writer, sheet_name='Prestim_entrain')
    
     
        
        

        
    
        
    
     
    return 
    
def multiple_theta_delta(analysis_times, data): #Plots PSDs at multiple times when fed in an excel spreadsheet.
       
    
    num_rows, num_cols=analysis_times.shape
    
    thetadeltaresults= zeros([num_rows])
  
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
        time_axis, sub_data1=sub_time_data(data, prm.get_starttime2(), prm.get_endtime2(), prm.get_sampling_rate())

        
        time_axis, sub_data2=sub_time_data(data, prm.get_starttime2(), prm.get_endtime2(), prm.get_sampling_rate())

        thetadeltaratio = psd_theta_delta(sub_data1, sub_data2, prm.get_windowtype(), prm.get_sampling_rate(), prm.get_stimfreq())
        thetadeltaresults[n]=thetadeltaratio
        
       
    
     
    return thetadeltaresults
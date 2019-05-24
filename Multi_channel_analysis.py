# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:33:17 2018

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
from numpy import *
import parameters
import matplotlib.pyplot as plt
prm = parameters.Parameters()
from OpenEphys import *
from power_spectrum import*
import mne
import xlrd
import pandas as pd



'This function calculates theta_delta ratio and entrainment for all channels in a 16 channel headstage'
'It outputs as excel spreadsheet in file, have to specify animal name as string'

def sixteenchan_thetadelta_entrainment(data, analysis_times, animal):
    
    #Below I define channel names that will be the list that use to run through data and as excel column headers
    
    channel_names=['hpc_mid_deep', 'hpc_mid_sup', 'hpc_ros_deep', 'hpc_ros_sup', 'pfc_deep', 
                       'pfc_sup', 'cx1', 'cx2', 'hpc_contra_deep', 'hpc_contra_sup', 
                       'EMG1', 'EMG2', 'cb_deep', 'cb_sup', 'hp_caudal_deep', 'hpc_caudal_sup']
   
    #Get number of analyis_times
    num_rows, num_cols=analysis_times.shape
    #Use number of times to make zero arrays for thetadelta, entrinment,coherence,pre-entrainment
    thetadeltaarray= zeros(shape=(16, num_rows))
    entrainmentarray=zeros(shape=(16, num_rows))
    coherencearray=zeros(shape=(16, num_rows))
    preentrainment=zeros(shape=(16, num_rows))
    #Run through all the channels, calculate theta_delta ratio and append to results
    for n in range(len(channel_names)):
        thetadeltaresults=multiple_theta_delta(analysis_times, data[:,n])
        thetadeltaarray[n]=thetadeltaresults
    
    #Transpose to run with pandas
    thetadeltaarray_tp=thetadeltaarray.transpose()
    
    #Make a pandas dataframe with the transponsed results array
    df1=pd.DataFrame(thetadeltaarray_tp)
    
    
    #Open an instance of of excel writer and use to define path and filename where it is to be saved.
    writer=pd.ExcelWriter(str(prm.get_excelpath()) + str(prm.get_excelname())+'_'+animal+'.xlsx')
    
    #Write array to sheet.
    df1.to_excel(writer,sheet_name="theta_delta", header=channel_names)   

    #Run through all the channels, calculate theta_delta ratio and append to results
    for n in range(len(channel_names)):
        entrainmentresults=multiple_entrainmentratio(analysis_times, data[:,n], 'stim')
        entrainmentarray[n]=entrainmentresults 
     #Transpose to run with pandas
    entrainmentarray_tp=entrainmentarray.transpose()
    #Make a pandas dataframe with the transponsed results array
    df2=pd.DataFrame(entrainmentarray_tp)
    #Write array to sheet.
    df2.to_excel(writer, sheet_name="entrainment", header=channel_names)
    
    
    
    
    #Run through all the channels, calculate coherence with optogenetics channel and append results
    for n in range(len(channel_names)):
        coherenceresults=coherence_data(analysis_times, data[:,n], data[:,16]) #data[:,16] is optogenetics
        coherencearray[n]=coherenceresults
    
    coherencearray_tp=coherencearray.transpose()
    #Make a pandas dataframe with the transponsed results array
    df3=pd.DataFrame(coherencearray_tp)
    #Write array to sheet.
    df3.to_excel(writer, sheet_name="coherence", header=channel_names)  
    
    
    for n in range(len(channel_names)):
        entrainmentresults=multiple_entrainmentratio(analysis_times, data[:,n], 'pre-stim')
        entrainmentarray[n]=entrainmentresults 
     #Transpose to run with pandas
    entrainmentarray_tp=entrainmentarray.transpose()
    #Make a pandas dataframe with the transponsed results array
    df4=pd.DataFrame(entrainmentarray_tp)
    #Write array to sheet.
    df4.to_excel(writer, sheet_name="pre-entrainment", header=channel_names)
    
    
    
    
    return

    
    
    
    

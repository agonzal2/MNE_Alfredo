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
import mne
import xlrd



def 16_channel_entrainment_delta_theta(data, analysis_times, channel_names, animal_list):
    if len(animal_list) == 4:
        
    
        
    return

       
    
    
    
    
    
    
#    
#    if headstage_number == 3:
#        
#        'Add Opto Stim Channel to Data'
#    
#        data= np.append(data, (np.zeros((data.shape[0],1), dtype=int64)), axis=1)
#        data[:,48]=(data_adc[:,0]*300) #Multiply by 300 to have about the same scale for optogenetics.
#        
# 
#    if headstage_number ==2:
#        
#        'Add Opto Stim Channel to Data'
#    
#        data= np.append(data, (np.zeros((data.shape[0],1), dtype=int64)), axis=1)
#        data[:,32]=(data_adc[:,0]*300) #Multiply by 300 to have about the same scale for optogenetics.
#
#        n_channels=33
#
#        
#    if headstage_number ==1:
#        
#        'Add Opto Stim Channel to Data'
#    
#        data= np.append(data, (np.zeros((data.shape[0],1), dtype=int64)), axis=1)
#        data[:,16]=(data_adc[:,0]*300) 
#    
    
    multiple_theta_delta(analysis_times, data[:, n])
    
    
    
    
    

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:04:37 2015

@author: agonzal2
"""


from scipy.signal import butter, filtfilt

def highpass(data, sampling_rate):

    lowcut = 50#this is the low end of the theta band pass filter
    highcut = 250 #this is the high end of the theta band pass filter
    order = 2
    
    def butter_bandpass(lowcut, highcut, sampling_rate, order): #here we define the butter bandpass in order to get coefficient readouts for our output
        nyq = 256 #we define the nquist frequency here for the filter
        low = lowcut / nyq
        high = highcut / nyq
        butter_b, butter_a = butter(order, [low, high], btype='band', analog=False) #this runs the filter function with our parameters
        return butter_b, butter_a
    
    def butter_bandpass_filter(data, lowcut, highcut, fs, order): #now we run the filtfilt function in order to get the data
        butter_b, butter_a = butter_bandpass(lowcut, highcut, sampling_rate, order)
        butter_y = filtfilt(butter_b, butter_a, data)
        return butter_y
    
  
    filtered_data = butter_bandpass_filter(data, lowcut, highcut, sampling_rate, order) #This takes the data for an individual channel and puts into correct dictiona

    return filtered_data

def lowpass(data, sampling_rate, lowcut, highcut):

#    lowcut = 0.1#this is the low end of the theta band pass filter
#    highcut = 255 #this is the high end of the theta band pass filter
    order = 2
    
    def butter_bandpass(lowcut, highcut, sampling_rate, order): #here we define the butter bandpass in order to get coefficient readouts for our output
        nyq = 256 #we define the nquist frequency here for the filter
        low = lowcut / nyq
        high = highcut / nyq
        butter_b, butter_a = butter(order, [low, high], btype='band', analog=False) #this runs the filter function with our parameters
        return butter_b, butter_a
    
    def butter_bandpass_filter(data, lowcut, highcut, fs, order): #now we run the filtfilt function in order to get the data
        butter_b, butter_a = butter_bandpass(lowcut, highcut, sampling_rate, order)
        butter_y = filtfilt(butter_b, butter_a, data)
        return butter_y
    
  
    filtered_data = butter_bandpass_filter(data, lowcut, highcut, sampling_rate, order) #This takes the data for an individual channel and puts into correct dictiona

    return filtered_data


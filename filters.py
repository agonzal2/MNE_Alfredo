
"""
Created on Tue Mar 17 15:04:37 2015

@author: agonzal2
"""


from scipy.signal import *

# Required input defintions are as follows;
# time:   Time between samples
# band:   The bandwidth around the centerline freqency that you wish to filter
# freq:   The centerline frequency to be filtered
# ripple: The maximum passband ripple that is allowed in db
# order:  The filter order.  For FIR notch filters this is best set to 2 or 3,
#         IIR filters are best suited for high values of order.  This algorithm
#         is hard coded to FIR filters
# filter_type: 'butter', 'bessel', 'cheby1', 'cheby2', 'ellip'
# data:         the data to be filtered

def Implement_Notch_Filter(fs, band, freq, ripple, order, filter_type, data):
    from scipy.signal import iirfilter
    nyq  = fs/2.0
    low  = freq - band/2.0
    high = freq + band/2.0
    low  = low/nyq
    high = high/nyq
    b, a = iirfilter(order, [low, high], rp=ripple, btype='bandstop',
                     analog=False, ftype=filter_type)
    filtered_data = lfilter(b, a, data)
    return filtered_data
    


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


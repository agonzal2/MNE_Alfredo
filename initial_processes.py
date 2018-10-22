
"""
Created on Wed Nov 22 16:17:18 2017

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

def load_file(file):  #Opens text files.
    print(" Opening file " + file)
    
    data=loadtxt(file)
    print(len(data))
    return data


'The function below loads 16 channel headstage recordings, specify how many there are'

def load_16_channel_opto(headstage_number):
    
     
    'Below are 2 functions from OpenEphys to load data channels and auxilary (accelerometer) channels'
    data=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'CH', dtype = float, session = '0', source = '100')#######load file
    data_adc=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'ADC', dtype = float, session = '0', source = '100')#######load file8

    if headstage_number == 4:
    
        'Add Opto Stim Channel to Data'
    
        data= np.append(data, (np.zeros((data.shape[0],1), dtype=int64)), axis=1)
        data[:,64]=(data_adc[:,0]*300) #Multiply by 300 to have about the same scale for optogenetics.
        
        datatp=data.transpose()#Array from openephys has to be transposed to match RawArray MNE function to create.
        del data
        del data_adc
        
        'Below I make the channel names and channel types, this should go in the parameteres file later.'
        
        n_channels=65
        
        channel_names=['hpc_mid_deep', 'hpc_mid_sup', 'hpc_ros_deep', 'hpc_ros_sup', 'pfc_deep', 
                       'pfc_sup', 'cx1', 'cx2', 'hpc_contra_deep', 'hpc_contra_sup', 
                       'EMG1', 'EMG2', 'cb_deep', 'cb_sup', 'hp_caudal_deep', 'hpc_caudal_sup',
                       'hpc_mid_d_2', 'hpc_mid_s_2', 'hpc_ros_d_2', 'hpc_ros_s_2', 'pfc_d_2', 
                       'pfc_sup_2', 'cx1_2', 'cx2_2', 'hpc_ct_d_2', 'hpc_ct_s_2', 
                       'EMG1_2', 'EMG2_2', 'cb_deep_2', 'cb_sup_2', 'hp_caud_d_2', 'hpc_caud_s_2',
                       'hpc_mid_d_3', 'hpc_mid_s_3', 'hpc_ros_d_3', 'hpc_ros_s_3', 'pfc_d_3', 
                       'pfc_s_3', 'cx1_3', 'cx2_3', 'hpc_c_d_3', 'hpc_c_s_3', 
                       'EMG1_3', 'EMG2_3', 'cb_deep_3', 'cb_sup_3', 'hp_c_d_3', 'hpc_c_s_3',
                       'hpc_mid_d_4', 'hpc_mid_s_4', 'hpc_ros_d_4', 'hpc_ros_s_4', 'pfc_d_4', 
                       'pfc_s_4', 'cx1_4', 'cx2_4', 'hpc_c_d_4', 'hpc_c_s_4', 
                       'EMG1_4', 'EMG2_4', 'cb_deep_4', 'cb_sup_4', 'hp_c_d_4', 'hpc_c_s_4',
                       
                       'Opto']
        channel_types=['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
                       'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
                       'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
                       'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
                       'stim']
    
    
    
    if headstage_number == 3:
        
        'Add Opto Stim Channel to Data'
    
        data= np.append(data, (np.zeros((data.shape[0],1), dtype=int64)), axis=1)
        data[:,48]=(data_adc[:,0]*300) #Multiply by 300 to have about the same scale for optogenetics.
        
        datatp=data.transpose()#Array from openephys has to be transposed to match RawArray MNE function to create.
        del data
        del data_adc
        
        'Below I make the channel names and channel types, this should go in the parameteres file later.'
        
        n_channels=49
        
        channel_names=['hpc_mid_deep', 'hpc_mid_sup', 'hpc_ros_deep', 'hpc_ros_sup', 'pfc_deep', 
                       'pfc_sup', 'cx1', 'cx2', 'hpc_contra_deep', 'hpc_contra_sup', 
                       'EMG1', 'EMG2', 'cb_deep', 'cb_sup', 'hp_caudal_deep', 'hpc_caudal_sup',
                       'hpc_mid_d_2', 'hpc_mid_s_2', 'hpc_ros_d_2', 'hpc_ros_s_2', 'pfc_d_2', 
                       'pfc_sup_2', 'cx1_2', 'cx2_2', 'hpc_ct_d_2', 'hpc_ct_s_2', 
                       'EMG1_2', 'EMG2_2', 'cb_deep_2', 'cb_sup_2', 'hp_caud_d_2', 'hpc_caud_s_2',
                       'hpc_mid_d_3', 'hpc_mid_s_3', 'hpc_ros_d_3', 'hpc_ros_s_3', 'pfc_d_3', 
                       'pfc_s_3', 'cx1_3', 'cx2_3', 'hpc_c_d_3', 'hpc_c_s_3', 
                       'EMG1_3', 'EMG2_3', 'cb_deep_3', 'cb_sup_3', 'hp_c_d_3', 'hpc_c_s_3',
                       'Opto']
        channel_types=['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
                       'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
                       'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
                       'stim']
        
    if headstage_number ==2:
        
        'Add Opto Stim Channel to Data'
    
        data= np.append(data, (np.zeros((data.shape[0],1), dtype=int64)), axis=1)
        data[:,32]=(data_adc[:,0]*300) #Multiply by 300 to have about the same scale for optogenetics.
        
        datatp=data.transpose()#Array from openephys has to be transposed to match RawArray MNE function to create.
        del data
        del data_adc
        
        n_channels=33

        channel_names=['hpc_mid_deep', 'hpc_mid_sup', 'hpc_ros_deep', 'hpc_ros_sup', 'pfc_deep', 
                       'pfc_sup', 'cx1', 'cx2', 'hpc_contra_deep', 'hpc_contra_sup', 
                       'EMG1', 'EMG2', 'cb_deep', 'cb_sup', 'hp_caudal_deep', 'hpc_caudal_sup',
                       'hpc_mid_d_2', 'hpc_mid_s_2', 'hpc_ros_d_2', 'hpc_ros_s_2', 'pfc_d_2', 
                       'pfc_sup_2', 'cx1_2', 'cx2_2', 'hpc_ct_d_2', 'hpc_ct_s_2', 
                       'EMG1_2', 'EMG2_2', 'cb_deep_2', 'cb_sup_2', 'hp_caud_d_2', 'hpc_caud_s_2',
                       'Opto']
        channel_types=['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
                       'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
                       'stim']
        
    if headstage_number ==1:
        
        'Add Opto Stim Channel to Data'
    
        data= np.append(data, (np.zeros((data.shape[0],1), dtype=int64)), axis=1)
        data[:,16]=(data_adc[:,0]*300) #Multiply by 300 to have about the same scale for optogenetics.
        
        datatp=data.transpose()#Array from openephys has to be transposed to match RawArray MNE function to create.
        del data
        del data_adc
        
        n_channels=17

        channel_names=['hpc_mid_deep', 'hpc_mid_sup', 'hpc_ros_deep', 'hpc_ros_sup', 'pfc_deep', 
                       'pfc_sup', 'cx1', 'cx2', 'hpc_contra_deep', 'hpc_contra_sup', 
                       'EMG1', 'EMG2', 'cb_deep', 'cb_sup', 'hp_caudal_deep', 'hpc_caudal_sup',
                       'Opto']
        channel_types=['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','emg','emg','eeg','eeg','eeg','eeg',
                       'stim']
        
    
    'This creates the info that goes with the channels, which is names, sampling rate, and channel types.'
    info = mne.create_info(channel_names, prm.get_sampling_rate(), channel_types)
    
    
    'This makes the object that contains all the data and info about the channels.'
    'Computations like plotting, averaging, power spectrums can be performed on this object'
    
    custom_raw = mne.io.RawArray( datatp, info)
    del datatp
    return custom_raw
    

'The function below loads individual 32 channel probe recordings'
def load_32_EEG():
   
    'Below are 2 functions from OpenEphys to load data channels and auxilary (accelerometer) channels'
    data=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'CH', dtype = float, session = '0', source = '100')
    data_aux=loadFolderToArray(prm.get_filepath(), channels = 'all', chprefix = 'AUX', dtype = float, session = '0', source = '100')
    
    'Below we append a line to the data array and add the accelrometer data. We transpose to fit the MNE data format.'
    data = np.append(data, (np.zeros((data.shape[0],1), dtype=int64)), axis=1)
    data[:,32]=data_aux[:,0]
    
    datatp=data.transpose()#Array from openephys has to be transposed to match RawArray MNE function to create.
    del data
    
    'Below is the info needed for making the MNE object'
    n_channels =33

    channel_names=['S1Tra', 'S1DZ_S1BFa', 'V2MM_RSAa', 'V2MLa', 'V2La', 'V2MMa', 
                   'V1Ma', 'V2L_V1Ba', 'M2_posta', 'S1HL_S1FLa',
                   'M1_Posta', 'S1FL_S1DZa', 'M1_anta', 'M2_anta', 'M1_FrAa', 
                   'M2_FrAa', 'M2_FRAb', 'M1_FRAb', 'M2_antb', 
                   'M1_antb', 'S1FL_S1DZb', 'M1_Postb', 'S1HL_S1FLb',
                   'M2_postb', 'V2L_V1Bb', 'V1Mb', 'V2MMb', 'V2Lb',
                   'V2MLb', 'V2MM_RSAb', 'S1DZ_S1BFb', 'S1Trb', 'AUX']
    channel_types=['eeg','eeg','eeg','eeg','eeg','eeg', 'eeg', 'eeg', 
                   'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg'
                   ,'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg'
                   ,'eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg', 'emg']
    
    'Below is an attempt to make the electrode map of electrodes to perform CSD analysis, -----still not working'
    
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


    
    
    'This creates the info that goes with the channels, which is names, sampling rate, and channel types.'
    info = mne.create_info(channel_names, prm.get_sampling_rate(), channel_types)
    
    
    'This makes the object that contains all the data and info about the channels.'
    'Computations like plotting, averaging, power spectrums can be performed on this object'
    
    custom_raw = mne.io.RawArray( datatp, info)
    del datatp
    return custom_raw
    
    
    
    
    

def create_epochs(analysis_times, sampling_rate): #Makes epoch file for MNE of stimulation times.
    
    num_rows, num_cols=analysis_times.shape
    epochs= tile(0, (num_rows, 3))
    for n in range(0, num_rows):
        start_time=(analysis_times.item(n,0))
        epochs[n][0]=start_time*sampling_rate
        epochs[n][2]=n
        
        
    return epochs

def create_brain_state_epochs(analysis_times, sampling_rate): #Makes epoch file for MNE of stimulation times.
    
    num_rows, num_cols=analysis_times.shape
    epochs= tile(0, (num_rows, 3))
    for n in range(0, num_rows):
        start_time=(analysis_times.item(n,1))
        epochs[n][0]=start_time
        epochs[n][2]=n
        
        
    return epochs


def actual_stim_times(data, sampling_rate):##for use with normal opto
    
    times=[]
    times=data[:,64]>300
    start_times=[]
    
    for n in range(len(times)): 
        if times[n] == True:
            start_times.append(n)
    
    stim_times=[]    
    
    for n in range(len(start_times)):
        x=n-1
        if n ==0:
            stim_times.append(start_times[n]/sampling_rate)
        elif start_times[n]-start_times[n-1]>(sampling_rate*20):
            stim_times.append(start_times[n]/sampling_rate)
    
    
    stimulations= asarray(stim_times)
    
    return stimulations

def import_brain_state(excelfile): #Import analysis times for optogenetic on and control times from excel.
    #Make sure values are not empty.
    #Save file as .xls"
    print(" Openning Brain State Data " + excelfile)
    book= xlrd.open_workbook(excelfile)
    sheet_names = book.sheet_names()
    sheet= book.sheet_by_name(sheet_names[0])
    analysis_times= zeros(shape=(sheet.nrows, 3))
    print(analysis_times.shape)
    for n in range(0, sheet.nrows):
        cell1=sheet.cell(n, 0)
        cell1_value=cell1.value
        analysis_times[n, 0]=cell1_value
        
        cell2=sheet.cell(n, 1)
        cell2_value=cell2.value
        analysis_times[n, 1]=cell2_value
    
        cell3=sheet.cell(n, 2)
        cell3_value=cell3.value
        analysis_times[n, 2]=cell3_value
        
    return analysis_times


def import_channel_combo(excelfile):
    print(" Openning Channel Data " + excelfile)
    book= xlrd.open_workbook(excelfile)
    sheet_names = book.sheet_names()
    sheet= book.sheet_by_name(sheet_names[0])
    channel_combo= zeros(shape=(sheet.nrows, 2))
    
    for n in range(0, sheet.nrows):
        cell1=sheet.cell(n, 0)
        cell1_value=cell1.value
        channel_combo[n, 0]=cell1_value
        cell2=sheet.cell(n, 1)
        cell2_value=cell2.value
        channel_combo[n, 1]=cell2_value
        
    return channel_combo

 
def import_spreadsheet(excelfile): #Import analysis times for optogenetic on and control times from excel.
    #Make sure values are not empty.
    #Save file as .xls"
    print(" Openning Excelfile " + excelfile)
    book= xlrd.open_workbook(excelfile)
    sheet_names = book.sheet_names()
    sheet= book.sheet_by_name(sheet_names[0])
    analysis_times= zeros(shape=(sheet.nrows - 1, 5))
    
    for n in range(0, sheet.nrows-1):
        cell1=sheet.cell(n+1, 3)
        cell1_value=cell1.value
        analysis_times[n, 0]=cell1_value
        cell2=sheet.cell(n+1, 4)
        cell2_value=cell2.value
        analysis_times[n, 1]=cell2_value
        cell5=sheet.cell(n+1, 5)
        cell5_value=cell5.value
        analysis_times[n, 2]=cell5_value
        cell6=sheet.cell(n+1, 6)
        cell6_value=cell6.value
        analysis_times[n, 3]=cell6_value
        cell7=sheet.cell(n+1, 7)
        cell7_value=cell7.value
        analysis_times[n, 4]=cell7_value
        
    return analysis_times


def sub_time_data(data, start_time, end_time, sampling_rate): #Gets time axis and data of specific times.
    
    prm.set_filelength(len(data))
    filelength=prm.get_filelength()
    timelength=filelength/sampling_rate
    time_axis = linspace(start_time, end_time, ((end_time-start_time)*sampling_rate))
    
    index_start = start_time*sampling_rate
    index_end = end_time*sampling_rate
    sub_data = data[int(index_start):int(index_end)]
    
    return time_axis, sub_data


def plot_all(data, sampling_rate, color):  #This allows for an initial plot of all the ddata.
    
    timemax=len(data)
    timelength = timemax/sampling_rate
    
    timeforplot = linspace(0, timelength, timemax)
    plt.plot(timeforplot, data, color)
    
    return


    


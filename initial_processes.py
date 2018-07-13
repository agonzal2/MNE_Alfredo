# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:17:18 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
from numpy import *
import parameters
import matplotlib.pyplot as plt
prm = parameters.Parameters()
import xlrd

def load_file(file):  #Opens text files.
    print(" Opening file " + file)
    
    data=loadtxt(file)
    print(len(data))
    return data

def create_epochs(analysis_times, sampling_rate): #Makes epoch file for MNE of stimulation times.
    
    num_rows, num_cols=analysis_times.shape
    epochs= tile(0, (num_rows, 3))
    for n in range(0, num_rows):
        start_time=(analysis_times.item(n,0))
        epochs[n][0]=start_time*sampling_rate
        epochs[n][2]=n
        
        
    return epochs

    
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


    


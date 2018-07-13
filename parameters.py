# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:29:46 2017

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk

This class has the setters and getters for the parameters. The parameters need to be set in main
and they can be called by calling the getter functions.
For example to set and get filepath:
prm.set_filepath('D:\\ERUK\\Wireless_Opto\\171120_VGATCRE_150_Day_3')
prm.get_filepath()
"""

class Parameters:
    
    
    filepath = ''
    filename = ''
    excelpath = ''
    excelname = ''
    sampling_rate = 512
    windowtype =''
    filelength = 500
    starttime=0
    endtime=90
    starttime2=0
    endtime2=90
    stimfreq=10
 
    def get_excelpath(self):
        return Parameters.excelpath

    def set_excelpath(self, exp):
        Parameters.excelpath = exp
    
    def get_excelname(self):
        return self.excelname

    def set_excelname(self, exn):
        Parameters.excelname = exn
        
    def get_starttime(self):
        
        return Parameters.starttime
    
    def set_starttime(self, start):
        
        Parameters.starttime=start
        
    def get_starttime2(self):
        
        return Parameters.starttime2
    
    def set_starttime2(self, start2):
        
        Parameters.starttime2=start2
    
    def get_endtime(self):
        
        return Parameters.endtime
    
    def set_endtime(self, end):
        
        Parameters.endtime=end
        
        
    def get_endtime2(self):
        
        return Parameters.endtime2
    
    def set_endtime2(self, end2):
        
        Parameters.endtime2=end2
    
    
    def get_filelength(self):
        
        return Parameters.filelength
    
    def set_filelength(self, leng):
        Parameters.filelength=leng
    
    def get_windowtype(self):
        return Parameters.windowtype
    
    def set_windowtype(self, wt):
        
        Parameters.windowtype = wt
        
    def get_filepath(self):
        return Parameters.filepath

    def set_filepath(self, fp):
        Parameters.filepath = fp
    
    def get_filename(self):
        return self.filename

    def set_filename(self, fn):
        Parameters.filename = fn
        
    def get_sampling_rate(self):
        return Parameters.sampling_rate
                
    def set_sampling_rate(self, sr):
        
        Parameters.sampling_rate = sr
        
    def get_stimfreq(self):
        return Parameters.stimfreq
                
    def set_stimfreq(self, sf):
        
        Parameters.stimfreq = sf
    

        
    

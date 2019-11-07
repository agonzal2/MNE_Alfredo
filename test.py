# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:56:05 2019

@author: agonzal2
"""

from PyQt5.QtCore import pyqtSignal,QObject
 
class nut(QObject):
 
    cracked = pyqtSignal()
    
    def __init__(self):
    
        QObject.__init__(self)
    
    def crack(self):
    
        self.cracked.emit()
	
def crackit():
 
    print("hazelnut cracked!")
 
hazelnut = nut()
 
hazelnut.cracked.connect(crackit) # connecting the cracked signal with crackit slot
 
hazelnut.crack()

	
def keyPressEvent(self, e):
 
    if e.key() == Qt.Key_F12:
 
        self.close()
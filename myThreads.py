# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:06:30 2019

@author: agonzal2
"""

import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal

TIME_LIMIT = 100

class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count +=1
            time.sleep(1)
            self.countChanged.emit(count)
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 18:57:01 2018

@author: ZEN-1
"""

import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,

    QInputDialog, QApplication)

 

app = QApplication([])

dialog = QInputDialog()

dialog.show()

app.exec_()
#! /usr/bin/env python

# PictureViewer.py
#
# Copyright 2014 Virtua Enterprise Limited
#
# A simple Python image viewer application
# Supports a number of image formats


import sys
from PySide import QtGui, QtCore

try:
    from PySide.phonon import Phonon
except ImportError:
    print "Cannot find Phonon, exiting!"
    sys.exit(1)


# Main Picture Viewer Class
class QPicViewer(QtGui.QWidget):
    def __init__(self):
        super(QPicViewer, self).__init__()

        # ====================
        # Set the window title
        # ====================
        self.setWindowTitle("Image Viewer")

        # =============================
        # Define Application components
        # =============================
        self.open_button = QtGui.QPushButton("Open Image")


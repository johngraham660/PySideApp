#! /usr/bin/env python

# QVideoPlayer.py
#
# Copyright 2014 Virtua Enterprise Limited

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

        self.setWindowTitle("Image Viewer")


        # ==========================
        # Define image viewer widget
        # ==========================
        self.imagewidget =


#! /usr/bin/env python

# QVideoPlayer.py
#
# Copyright 2014 Virtua Enterprise Limited


import sys

from PySide import QtCore, QtGui

try:
    from PySide.phonon import Phonon
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "Video Player",
                               "Your Qt Installation does not have Phonon support.",
                               QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                               QtGui.QMessageBox.NoButton)
    sys.exit(1)

# =================
# Main QVideo Class
# =================


class QVideo(QtGui.QWidget):

    def __init__(self):

        super(QVideo, self).__init__()
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.player = Phonon.MediaObject(self)
        Phonon.createPath(self.player, self.audioOutput)

        self.videoWidget = Phonon.VideoWidget(self)
        Phonon.createPath(self.player, self.videoWidget)

        #self.player.setTickInterval(1000)
        #self.connect(self.player, QtCore.SIGNAL("tick(qint64)"), self.tick)

        self.seekSlider = Phonon.SeekSlider(self.player, self)
        self.volumeSlider = Phonon.VolumeSlider(self.audioOutput, self)

        # =================
        # Define GUI Assets
        # =================

        # =======
        # BUTTONS
        # =======
        self.browsebutton = QtGui.QPushButton("Open Media")
        self.browsebutton.setIcon(QtGui.QIcon("digital_assets/browse_button.png"))

        self.playbutton = QtGui.QPushButton("Play")
        self.playbutton.setIcon(QtGui.QIcon("digital_assets/play_button.png"))

        self.pausebutton = QtGui.QPushButton("Pause")
        self.pausebutton.setIcon(QtGui.QIcon("digital_assets/pause_button.png"))

        self.stopbutton = QtGui.QPushButton("Stop")
        self.stopbutton.setIcon(QtGui.QIcon("digital_assets/stop_button.png"))

        self.build_interface()
        self.setup_connections()

    def build_interface(self):

        # ===
        # TOP
        # ===
        toplayout = QtGui.QHBoxLayout()
        toplayout.addWidget(self.browsebutton)

        # ======
        # MIDDLE
        # ======
        middlelayout = QtGui.QHBoxLayout()
        middlelayout.addWidget(self.seekSlider)

        # ======
        # BOTTOM
        # ======
        bottomlayout = QtGui.QHBoxLayout()
        bottomlayout.addWidget(self.playbutton)
        bottomlayout.addWidget(self.pausebutton)
        bottomlayout.addWidget(self.stopbutton)
        bottomlayout.addWidget(self.volumeSlider)

        # =======================================================
        # Bring widgets and layouts together in a Vertical Layout
        # =======================================================
        layout = QtGui.QVBoxLayout()
        layout.addLayout(toplayout)
        layout.addWidget(self.videoWidget)
        layout.addLayout(middlelayout)
        layout.addLayout(bottomlayout)

        self.setLayout(layout)
        self.seekSlider.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        self.volumeSlider.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)

    def setup_connections(self):

        # =======================================
        # Setup all of the connections in the GUI
        # =======================================

        self.connect(self.browsebutton, QtCore.SIGNAL("clicked()"), self.browse_clicked)
        self.connect(self.playbutton, QtCore.SIGNAL("clicked()"), self.play_clicked)
        self.connect(self.stopbutton, QtCore.SIGNAL("clicked()"), self.stop_clicked)
        self.connect(self.pausebutton, QtCore.SIGNAL("clicked()"), self.pause_clicked)

    # ====================================================
    # Define the "clicked" Methods for each of our buttons
    # ====================================================

    def play_clicked(self):
        self.player.play()

    def pause_clicked(self):
        self.player.pause()

    def stop_clicked(self):
        self.player.stop()

    def browse_clicked(self):
        fd = QtGui.QFileDialog.getOpenFileName(self)

        # =======================================================================================
        # fd is now a tuple, The file name selected is stored in the first element of that tuple.
        # =======================================================================================

        media_file = fd[0]

        # TODO: get media resolution and resize the VPlayer window accordingly

        self.player.setCurrentSource(Phonon.MediaSource(media_file))

        # Set the video widget size
        self.videoWidget.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)



if __name__ == "__main__":
    QtApp = QtGui.QApplication(sys.argv)
    QtApp.setApplicationName("VPlayer")
    VPlayer = QVideo()
    VPlayer.setWindowTitle("Best Media Player Since Sliced Bread")
    VPlayer.show()
    sys.exit(QtApp.exec_())

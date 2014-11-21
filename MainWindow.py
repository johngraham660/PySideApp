#! /usr/bin/env python

# =======
# IMPORTS
# =======
import sys

# ==============
# PySide Imports
# ==============
from PySide.QtGui import QMainWindow
from PySide.QtGui import QApplication
from PySide.QtGui import QIcon
from PySide.QtGui import QToolTip
from PySide.QtGui import QFont
from PySide.QtGui import QMessageBox
from PySide.QtGui import QDesktopWidget
from PySide.QtGui import QStatusBar
from PySide.QtGui import QAction
from PySide.QtGui import QKeySequence
from PySide.QtGui import QTextEdit



# ==================================
# MAIN APPLICATION CLASS DECLARATION
# ==================================
class AppWindow(QMainWindow):

    # =====================
    # The Main Window Class
    # =====================

    def __init__(self):
        # ====================
        # Constructor Function
        # ====================

        QMainWindow.__init__(self)
        self.setWindowTitle("Virtua Text Editor")
        self.setGeometry(300, 300, 1024, 768)

        QToolTip.setFont(QFont("Decorative", 9, QFont.Bold))
        self.setToolTip('Application Window')

        # ================================
        # Function to setup menus, etc etc
        # ================================
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.create_menus()
        self.create_actions()
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.saveasAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.selectallAction)
        self.editMenu.addAction(self.deselectallAction)
        self.helpMenu.addAction(self.aboutAction)

        self.app_status_bar = QStatusBar()
        self.app_status_bar.showMessage('Ready', 10000)
        self.setStatusBar(self.app_status_bar)

        self.create_toolbar()
        self.toolbar.addAction(self.newAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)


    def create_toolbar(self):
        # ===============================
        # Function to create the toolbar.
        # ===============================
        self.toolbar = self.addToolBar('Main')


    def newfile(self):
        self.textEdit.setText('')

    # TODO: Create the file/open method
    def openfile(self):
        print "Open File Menu Selected"

    # TODO: Create the file/save method
    def savefile(self):
        print "Save File Menu Selected"

    # TODO: Create the file/saveas method
    def saveasfile(self):
        print "Save As File Menu Selected"

    def create_actions(self):
        # =========================================
        # Function to create actions for menu items
        # =========================================

        self.newAction = QAction(QIcon('digital_assets/document-new.svg'), 'New', self)
        self.newAction.setShortcut(QKeySequence.New)
        self.newAction.setStatusTip("Create a New File")
        self.newAction.setIconText("New")
        self.newAction.triggered.connect(self.newfile)

        self.openAction = QAction(QIcon('digital_assets/document-open.svg'), 'Open', self)
        self.openAction.setShortcut(QKeySequence.Open)
        self.openAction.setStatusTip("Open a file")
        self.openAction.triggered.connect(self.openfile)

        self.saveAction = QAction(QIcon('digital_assets/document-save.svg'), 'Save', self)
        self.saveAction.setShortcut(QKeySequence.Save)
        self.saveAction.setStatusTip("Save a file")
        self.saveAction.triggered.connect(self.savefile)

        self.saveasAction = QAction(QIcon('digital_assets/document-save-as.svg'), 'Save As', self)
        self.saveasAction.setShortcut(QKeySequence.SaveAs)
        self.saveasAction.setStatusTip("Save a File As....")
        self.saveasAction.triggered.connect(self.saveasfile)

        self.exitAction = QAction(QIcon('digital_assets/application-exit.svg'), 'Exit', self)
        self.exitAction.setShortcut(QKeySequence.Quit)
        self.exitAction.setStatusTip("Exit the Application")
        self.exitAction.triggered.connect(self.quit_application)

        self.undoAction = QAction(QIcon('digital_assets/edit-undo.svg'), 'Undo', self)
        self.undoAction.setShortcut(QKeySequence.Undo)
        self.undoAction.setStatusTip("Undo")
        self.undoAction.triggered.connect(self.textEdit.undo)

        self.redoAction = QAction(QIcon('digital_assets/edit-redo.svg'), 'Redo', self)
        self.redoAction.setShortcut(QKeySequence.Redo)
        self.redoAction.setStatusTip("Redo")
        self.redoAction.triggered.connect(self.textEdit.redo)

        self.cutAction = QAction(QIcon('digital_assets/edit-cut.svg'), 'Cut', self)
        self.cutAction.setShortcut(QKeySequence.Cut)
        self.cutAction.setStatusTip("Cut")
        self.cutAction.triggered.connect(self.textEdit.cut)

        self.copyAction = QAction(QIcon('digital_assets/edit-copy.svg'), 'Copy', self)
        self.copyAction.setShortcut(QKeySequence.Copy)
        self.copyAction.setStatusTip("Copy")
        self.copyAction.triggered.connect(self.textEdit.copy)

        self.pasteAction = QAction(QIcon('digital_assets/edit-paste.svg'), 'Paste', self)
        self.pasteAction.setShortcut(QKeySequence.Paste)
        self.pasteAction.setStatusTip("Paste")
        self.pasteAction.triggered.connect(self.textEdit.paste)

        self.selectallAction = QAction(QIcon('digital_assets/edit-select-all.svg'), 'Select All', self)
        self.selectallAction.setShortcut(QKeySequence.SelectAll)
        self.selectallAction.setStatusTip("Select All")
        self.selectallAction.triggered.connect(self.textEdit.selectAll)

        self.deselectallAction = QAction(QIcon('digital_assets/edit-select-all.svg'), 'Deselect All', self)
        self.deselectallAction.setShortcut("Shift+Ctrl+A")
        self.deselectallAction.setStatusTip("Deselect All")
        self.deselectallAction.triggered.connect(self.deselect_all_text)

        self.aboutAction = QAction(QIcon('digital_assets/AppIcon.png'), 'About', self)
        self.aboutAction.setStatusTip("Displays info about the application")
        self.aboutAction.triggered.connect(self.show_about)


    def deselect_all_text(self):
        text_cursor = self.textEdit.textCursor()
        text_cursor.clearSelection()
        self.textEdit.setTextCursor(text_cursor)

    def create_menus(self):
        # ================================
        # Function to create the menu bar.
        # ================================
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.helpMenu = self.menuBar().addMenu("&Help")

    def set_icon(self):
        # ===============================
        # Function to set the Window Icon
        # ===============================
        appicon = QIcon('digital_assets/AppIcon.png')
        self.setWindowIcon(appicon)

    def quit_application(self):
        # ================================
        # Function to quit the application
        # ================================
        userinfo = QMessageBox.question(self, "Confirmation", "This will quit, Do you want to continue?",
                                        QMessageBox.Yes | QMessageBox.No)
        if userinfo == QMessageBox.Yes:
            templateApp.quit()
        if userinfo == QMessageBox.No:
            pass

    def show_about(self):
        QMessageBox.about(self, "About VirtuaEditor",
                          "<p><b><h3>Virtua Editor Application</h3></b></p>"
                          "<p>VirtuaEditor has been written as a template application"
                          " that can be used as a basis for creating a working application.</p>"
                          " <p>All of the components that make up the core functions of an"
                          " application, the main window, a status bar, menus and dialogs"
                          " are provided here as a basis for writing something new and interesting</p>")

    def center_application(self):
        # ============================================
        # Function to center the Application on screen
        # ============================================
        qrect = self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        qrect.moveCenter(centerpoint)
        self.move(qrect.topLeft())

# ====================
# APPLICATION INSTANCE
# ====================

if __name__ == '__main__':
    # ===========================================
    # Let's wrap the application in a try block
    # so that we can catch and handle exceptions
    # ===========================================
    try:
        # =============================================
        # Here we create an instance of our application
        # =============================================
        templateApp = QApplication(sys.argv)
        templateApp.setApplicationName('TextEdit')

        templateWindow = AppWindow()
        templateWindow.set_icon()
        templateWindow.center_application()
        #templateWindow.create_status_bar()
        #templateWindow.setup_components()
        templateWindow.show()
        templateWindow.raise_()

        templateApp.exec_()
        sys.exit(0)

    except NameError:
        print "Name Error: %s" % sys.exc_info()[1]
    except SystemExit:
        print "Closing Application......"
    except Exception:
        print "%s" % sys.exc_info()[1]

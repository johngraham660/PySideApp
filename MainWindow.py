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
from PySide.QtGui import QLabel
from PySide.QtGui import QToolTip
from PySide.QtGui import QFont
from PySide.QtGui import QPushButton
from PySide.QtGui import QMessageBox
from PySide.QtGui import QDesktopWidget
from PySide.QtGui import QStatusBar
from PySide.QtGui import QMenuBar
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
        self.setWindowTitle("Generic Text Editor")
        self.setGeometry(300, 300, 1024, 768)

        QToolTip.setFont(QFont("Decorative", 8, QFont.Bold))
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
        self.newAction = QAction(QIcon('digital_assets/AppIcon.png'), 'New',
                                 self, shortcut=QKeySequence.New,
                                 statusTip="Create a New File",
                                 triggered=self.newfile)

        self.openAction = QAction(QIcon('digital_assets/AppIcon.png'), 'Open',
                                 self, shortcut=QKeySequence.Open,
                                 statusTip="Open a file",
                                 triggered=self.openfile)

        self.saveAction = QAction(QIcon('digital_assets/AppIcon.png'), 'Save',
                                  self, shortcut=QKeySequence.Save,
                                  statusTip="Save a File",
                                  triggered=self.savefile)

        self.saveasAction = QAction(QIcon('digital_assets/AppIcon.png'), 'Save As',
                                  self, shortcut=QKeySequence.SaveAs,
                                  statusTip="Save a File As....",
                                  triggered=self.saveasfile)

        self.exitAction = QAction(QIcon('digital_assets/AppIcon.png'), 'Exit',
                                  self, shortcut=QKeySequence.Quit,
                                  statusTip="Exit the Application",
                                  triggered=self.quit_application)

        self.undoAction = QAction(QIcon('digital_assets/AppIcon.png)'), 'Undo',
                                  self, shortcut=QKeySequence.Undo,
                                  statusTip="Undo",
                                  triggered=self.textEdit.undo)

        self.redoAction = QAction(QIcon('digital_assets/AppIcon.png'), 'Redo',
                                  self, shortcut=QKeySequence.Redo,
                                  statusTip="Redo",
                                  triggered=self.textEdit.redo)

        self.cutAction = QAction(QIcon('digital_assets/AppIcon.png'), 'Cut',
                                 self, shortcut=QKeySequence.Cut,
                                 statusTip="Cut",
                                 enabled=self.textEdit.textCursor().hasSelection(),
                                 triggered=self.textEdit.cut)

        self.copyAction = QAction(QIcon('digital_assets/AppIcon.png'), 'Copy',
                                  self, shortcut=QKeySequence.Copy,
                                  statusTip="Copy",
                                  triggered=self.textEdit.copy)

        self.pasteAction = QAction(QIcon(':digital_assets/AppIcon.png'), 'Paste',
                                   self, shortcut=QKeySequence.Paste,
                                   statusTip="Paste",
                                   triggered=self.textEdit.paste)

        self.selectallAction = QAction(QIcon('digital_assets/AppIcon.png'), 'Select All',
                                       self, shortcut=QKeySequence.SelectAll,
                                       statusTip="Select All",
                                       triggered=self.textEdit.selectAll)

        self.deselectallAction = QAction(QIcon('digital_assets/AppIcon.png'), 'Deselect All',
                                         self, shortcut="Shift+Ctrl+A",
                                         statusTip="Deselect All",
                                         triggered=self.deselect_all_text)

        self.aboutAction = QAction(QIcon('digital_assets/AppIcon.png'), 'About',
                                   self, statusTip="Displays info about the application",
                                   triggered=self.show_about)

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
                          "VirtuaEditor has been written as a template application"
                          " that can be used as a basis for creating a working application."
                          " All of the components that make up the core functions of an"
                          " application, the main window, a status bar, menus and dialogs"
                          " are provided here as a basis for writing something new and interesting")

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

        templateApp.exec_()
        sys.exit(0)

    except NameError:
        print "Name Error: %s" % sys.exc_info()[1]
    except SystemExit:
        print "Closing Application......"
    except Exception:
        print "%s" % sys.exc_info()[1]

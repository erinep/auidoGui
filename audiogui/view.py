# -*- coding: utf-8 -*-
# audiogui/views.py

"""This module provides the audiogui main window."""

from .customWidgets import BooksTable, FileSelector
from time import sleep
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QWidget,
    QStatusBar,
    QFileDialog,
    QPushButton,
    QListWidget,
    QProgressBar,
)

HEIGHT = 400
WIDTH = 350

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self._createRoot()
        self._createSrcSelector()
        self._createDestSelector()
        self._createBooksTable()
        self._createUploadControl()

        self.setMinimumHeight(HEIGHT)
        self.setMinimumWidth(WIDTH)

    def _createRoot(self): 
        """ create parent widget and layout"""
        self._rootLayout = QVBoxLayout()
        self._root = QWidget()
        self._root.setLayout(self._rootLayout)
        self.setCentralWidget(self._root)

    def _createSrcSelector(self):
        """ Add Source File Selection the center widget"""
        self._srcWidget = FileSelector("Source Folder")
        self._rootLayout.addWidget(self._srcWidget)
        self.setSrcButton, self.srcLineEdit = self._srcWidget.getItems()

    def _createDestSelector(self):
        """Add Destination File Selection to the center widget"""
        self._destWidget = FileSelector("Destination Folder")
        self._rootLayout.addWidget(self._destWidget)
        self.setDestButton, self.destLineEdit = self._destWidget.getItems()

    def _createBooksTable(self):
        """ Create table to hold books info"""
        self.table = BooksTable()
        self._rootLayout.addWidget(self.table)

    def _createUploadControl(self):
        """Add Doc to control upload items"""
        uploadPanel = QWidget()
        layout = QGridLayout()
        uploadPanel.setLayout(layout)

        self.toUpload = QListWidget()
        self.uploadButton = QPushButton("Upload")
        self.clearButton = QPushButton("Deselect")

        layout.addWidget(QLabel("Books to upload"))
        layout.addWidget(self.toUpload)
        layout.addWidget(self.uploadButton)
        layout.addWidget(self.clearButton)

        self._rootLayout.addWidget(uploadPanel)

    def createProgressBar(self, max=100):

        min = 0
        if (not hasattr(self, 'progressbarContainer')):
            # Create Base Element/Layout
            self.progressbarContainer = QWidget()
            layout = QHBoxLayout(self.progressbarContainer)
            self.progressbar = QProgressBar()
            layout.addWidget(self.progressbar)
            self.pLabel = QLabel(f'{min}/{max}')
            layout.addWidget(self.pLabel)
            self._rootLayout.addWidget(self.progressbarContainer)

        self.progressbar.setRange(min, max)
        self.progressbar.setValue(0)

    def updateProgressBar(self, value, text):
        self.progressbar.setValue(value)
        self.pLabel.setText(text)

    def setSrcLine(self, text):
        """ Sets text in in the Source Line Edit"""
        self.srcLineEdit.setText(text)

    def setDestLine(self, text):
        """ Sets text in in the Destination Line Edit"""
        self.destLineEdit.setText(text)

    def setStatusMessage(self, text, ms):
        """ Sets temporary text of the status bar for ms milliseconds"""
        self.statusBar().showMessage(text, ms)

    def setPermanentMessage(self, text):
        """ Sets A permanent text on the status bar. 
            Normal = covered by temporary status
            Permanent = not covered by temporary status"""
        if hasattr(self, '_pStatus'):
            self.statusBar().removeWidget(self._pStatus)
            del self._pStatus
        self._pStatus = QLabel(text)
        self.statusBar().addPermanentWidget(self._pStatus)

    def showBooks(self, data):
        """ adds all the values in the dictionary to a BookTable widget """
        self.table.setData(data)

    def selectDir(self, prompt, path):
        """ Open file selection dialog and return selected folder"""
        dirName = QFileDialog().getExistingDirectory(
            self,
            caption=prompt,
            directory=str(path))
        return dirName

    def killProgressBar(self, s):
        """delete progressBar container after s seconds"""
        print(f'progress bar will be closed in {s} seconds')
        sleep(s)
        if(self.progressbarContainer.close()):
            print('success')
        else:
            print('fail')
        

# -*- coding: utf-8 -*-
# audiogui/app.py

"""This module provides the audiogui application."""

import sys
from distutils.dir_util import copy_tree
from functools import partial
from multiprocessing import Process
from PyQt6.QtWidgets import QApplication
from .view import Window
from .model import Model, Status

def main():
    app = QApplication(sys.argv)
    win = Window()
    mod = Model()
    con = Controller(model=mod, view=win)
    win.show()
    sys.exit(app.exec())


class Controller():

    def __init__(self, model, view):
        self._m = model
        self._v = view
        self._setSlots()
        self._load() 

    def _load(self):
        """ Load book list and show it in the view"""

        #load source books
        if (self._m.getBooks(self._m.srcPath, self._m.srcBooks)):
            self._v.setStatusMessage("Permission Error: could not access all files at Source", 3000)
        
        #load dest book
        if (self._m.getBooks(self._m.dstPath, self._m.dstBooks)):
            self._v.setStatusMessage("Permission Error: could not access all files at Destination", 3000)

        self._m.compareBooks()
        self._v.showBooks(self._m.srcBooks)
        self._v.setSrcLine(self._m.getPathStr())
        self._v.setDestLine(self._m.getPathStr(1))

    def copy(self):
        """ Copy selected items to destination Path"""
        srcBase = str(self._m.srcPath)
        dstBase = str(self._m.dstPath)
        
        length =  len(self._m.selected)
        if (length != 0):
            self._v.createProgressBar(length)
            for n, book in enumerate(self._m.selected):
                sUrl = str(self._m.srcPath.joinpath(book['author']).joinpath(book['title']))
                dUrl = str(self._m.dstPath.joinpath(book['author']).joinpath(book['title']))
                print(sUrl, " to ", dUrl)
                copy_tree(sUrl, dUrl)
                self._v.updateProgressBar(n, f"{n}/{length}")
            # After Loop, update progress bar values
            self._v.updateProgressBar(length, f"{length}/{length}")
            #set timeout to remove proces
            Process()
        else:
            self._v.setStatusMessage('nothing selected...', 2000)
       
        

    def _updateDir(self, isDest=False):
        """ select active directory, and reload the window"""
        dirName = self._v.selectDir(
            "select destination folder" if isDest else "select source folder",
             self._m.dstPath if isDest else self._m.srcPath
        )
        self._m.setPathStr(dirName, isDest)
        self._load()

    def clearSelected(self):
        self._v.toUpload.clear()
        self._m.selected.clear()

    def _updateUploadList(self):
        """ change upload list to match values in _v.selected"""
        self.clearSelected()
        s = self._v.table.getSelected().selectedRows()
        for i in s:
            if self._m.srcBooks[i.row()]['status'] == Status.sourceonly:
                self._m.addSelected(i.row())
        for i in self._m.selected:
            self._v.toUpload.addItem(i['title'])

    def _upload(self):
        """ on upload button push"""
        self.copy()
        self._updateUploadList()
        print('upload action called')
        self._load()

    def _setSlots(self):
        """ Setup slots and signals"""
        self._v.setSrcButton.clicked.connect(
            self._updateDir
        )
        self._v.setDestButton.clicked.connect(
            partial(self._updateDir, True)
        )

        self._v.uploadButton.clicked.connect(
            self._upload
        )
        
        self._v.clearButton.clicked.connect(
            self.clearSelected
        )

        self._v.table.getSelected().selectionChanged.connect(
            self._updateUploadList
        )


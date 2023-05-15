# -*- coding: utf-8 -*-
# audiogui/model.py

"""This module provides the audiogui model."""

from pathlib import Path
from enum import Enum

Status = Enum( 'Status', ['both', 'sourceonly'])

class Model():

    defaultSrc = '/Users/Erin/Documents/2023/Python/TestSrc'
    defaultDest = '/Users/Erin/Documents/2023/Python/TestDest'

    def __init__(self, src=defaultSrc, dest=defaultDest):
        self.srcBooks = []
        self.dstBooks = []
        self.selected = []
        self.srcPath = Path(src)
        self.dstPath = Path(dest)
        self.getBooks(self.srcPath, self.srcBooks)
        self.getBooks(self.dstPath, self.dstBooks)
        self.ignoreList = self.getIgnoreList()

    def addSelected(self, index):
        """ Append object at index of srcBook to select"""
        self.selected.append(self.srcBooks[index])

    def getIgnoreList(self):
        """ Read contents of ignore file and return"""
        return

    def compareBooks(self):
        """ compare books in input and output 
        and add an element to srcBook collection to track comparison"""
        length = len(self.srcBooks) if len(self.srcBooks) > len(self.dstBooks) else len(self.dstBooks)

        for n, dbook in enumerate(self.dstBooks):
            if (n == length):
                break
            for sbook in self.srcBooks:
                if dbook == sbook:
                    sbook.update({'status': Status.both})


    def getBooks(self, path, booksCollection):
        """Scan url and create a list of dictionaries with the contents"""
        booksCollection.clear()
        try:
            for a in path.iterdir():
                if a.is_dir():
                    for b in a.iterdir():
                        newBook = {
                            "title": b.name,
                            "author": a.name,
                            "status": Status.sourceonly}
                        booksCollection.append(newBook)
        except PermissionError:
            return 1
            print("Permission Error: Please select a different folder")

    def getPathStr(self, dest=0):
        """ return string value of current path"""
        path = self.dstPath if dest else self.srcPath
        return str(path)

    def setPathStr(self, str, dest=0):
        """ create Path object using string input parameter"""
        if dest: 
            self.dstPath = Path(str)
        else:
            self.srcPath = Path(str)

    sampleData = [
        {"title": "book1", "author" : "abc"},
        {"title": "book2", "author" : "abc"},
        {"title": "book3", "author" : "def"},
    ]
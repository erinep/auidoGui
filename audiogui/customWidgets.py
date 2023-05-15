# -*- coding: utf-8 -*-
# audiogui/customWidgets.py

"""This module provides the audiogui custom widgets."""

from PyQt6.QtCore import Qt
from .model import Status as StatusEnum

from PyQt6.QtGui import (
    QIcon,
    QImage,
    QPainter,
    QPixmap,
)

from PyQt6.QtWidgets import (
    QWidget,
    QCheckBox,
    QToolButton,
    QLineEdit,
    QLabel,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
)

class BooksTable(QTableWidget):


    def __init__(self):
        super().__init__(0, 3)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        #self.verticalHeader().hideSection()


    def getSelected(self):
        return self.selectionModel()

    def createCheckItem(self):
        chkUrl = "./images/checkmark.png"
        chkIcon = QIcon(chkUrl)
        return QTableWidgetItem(chkIcon, "")

    def refreshStatus(self, data):
        """ Update the icons in the status column"""
        for n, book in enumerate(len(data)):
            if book['status'] == StatusEnum.both:
                self.setItem(n, 2, self.createCheckItem())
            else:
                self.setItem(n, 2, QTableWidgetItem())

    def setData(self, data):
        """ clear table and add book information"""
        self.clear()

        hHeaders = ['Title', 'Author', 'Status']

        self.setRowCount(len(data))

        for n, book in enumerate (data):
            title = QTableWidgetItem(book['title'])
            author = QTableWidgetItem(book['author'])

            if book['status'] == StatusEnum.both:
               
                self.setItem(n, 2, self.createCheckItem())

            self.setItem(n, 0, title)
            self.setItem(n, 1, author)

        self.setHorizontalHeaderLabels(hHeaders)

class FileSelector(QWidget):
    """ A HBbox widget containing read only line edit, and file selection button"""
    def __init__(self, text):

        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.button = QToolButton()
        icon = QIcon("./images/open.png")
        self.button.setIcon(icon)

        self.lineEdit = QLineEdit()
        self.lineEdit.setReadOnly(True)

        layout.addWidget(QLabel(text))
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button)

    def getItems(self):
        """ return tuple with button, lineEdit"""
        return self.button, self.lineEdit

# class ImageWidget( QWidget):
#     """" Widget that holds an image """
#     def __init__(self, imagePath, parent):
#         super(ImageWidget, self).__init__(parent)
#         self.icon = QPixmap(imagePath)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.drawPixmap(0, 0, self.icon)

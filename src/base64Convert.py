
# -*- coding: UTF8 -*-
import io, shutil, sys, os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import base64

class MainWidgetUI(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize (250, 200) # PyQT prohibited resizing the window
        self.setWindowTitle ( 'base64 encoded file system conversion')
        self.setWindowIcon(QtGui.QIcon("favicon.ico"))

        Layout = QVBoxLayout()
        self.pushButton1 = QPushButton("To base64")
        self.pushButton2 = QPushButton("To file")
        Layout.addWidget (self.pushButton1) # addWidget add a pendant
        Layout.addSpacing (100) # 100px add a spatial distance without the elastic band
        Layout.addWidget(self.pushButton2)
        self.setLayout (Layout) # setLayout provided QVBoxLayout, () a QHBoxLayout groups the perpendicular () horizontal layout, the layout of the venue view CURL-api.py
                 # PushButton1 click the button
        self.pushButton1.clicked.connect(self.Tobase64)
                 # PushButton2 click the button
        self.pushButton2.clicked.connect(self.Tofile)

    def Tobase64(self):
        fileDict = self.selectFile()
        if fileDict:
            GlobalToBase64(fileDict['file'], fileDict['filepath'] + "/" + fileDict['shotname'] + ".txt")
            QMessageBox.information (self, 'suggesting!' "Conversion successful", QMessageBox.Yes)

    def Tofile(self):
        fileDict = self.selectFile()
        if fileDict:
                         # Judge whether a simple file that comes with the file extension Mime data: audio / mp3; base64,
            fobj = open(fileDict['file'])
            contents = fobj.read()
            extensions = contents.split(',')[0].rsplit('/')[1].split(';')
            if len (extensions) == 2: # [ 'mp3', 'base64'] in the format of two
                # Generate temporary files are saved base64
                tmpFile = fileDict['filepath'] + "/" + fileDict['shotname'] + ".tmp"
                tmpFileObj = open(tmpFile, 'w')
                tmpFileObj.write(contents.split(',')[1])
                tmpFileObj.close()
                GlobalToFile(tmpFile, fileDict['filepath'] + "/" + fileDict['shotname'] + "." + extensions[0])
                QMessageBox.information (self, 'suggesting!' "Conversion successful", QMessageBox.Yes)
                os.remove (tmpFile) # delete temporary files

            else: # No mime
                mine, okPressed = QInputDialog.getText (self, "type of file format", "Please enter the type of file format:", QLineEdit.Normal,
                                                                                                               "Mp3") # get input dialog content
                if okPressed and mine: # Enter the text and select OK
                    GlobalToFile(fileDict['file'], fileDict['filepath'] + "/" + fileDict['shotname'] + "." + mine)
                    QMessageBox.information (self, 'suggesting!' "Conversion successful", QMessageBox.Yes)
                else:
                    return False

    def selectFile(self):
        '''
                 Select a document 
        '''
        # GetOpenFileName getOpenFileNames can only choose a multiple choice
        file = QFileDialog.getOpenFileName (self, "select file", '' "*. *")
        if file[0] == '':
            QMessageBox.warning (self, 'error!', 'Please select a file ', QMessageBox.Yes)
        else:
            (Filepath, filename) = os.path.split (file [0]) # get file path, file name
            (Shotname, extension) = os.path.splitext (filename) # get the file name, file extension
        return {"file": file[0], "filepath": filepath, "shotname": shotname}

def GlobalToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()

def GlobalToBase64_2(file):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
    
    return base64_data

def GlobalToFile_2(txt, file):
    ori_image_data = base64.b64decode(txt)
    fout = open(file, 'xb')
    fout.write(ori_image_data)
    fout.close()    
        

def GlobalToFile(txt, file):
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_widget = MainWidgetUI()
    main_widget.show()
    sys.exit(app.exec_())

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainwindow import Ui_YTDownloader
from pytube import YouTube
import os.path
import shutil
import time

save_path = '/Downloads/'

class MainWindow(QMainWindow, Ui_YTDownloader):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.enterbutton.clicked.connect(lambda: self.begin_search())

    def begin_search(self):
        link = self.inputlink.text()
        print('good')
        yt = YouTube(link)

        print(yt.title, yt.views)
        try:
             
            yd = yt.streams.get_highest_resolution()
            yd.download()
            src = f'{yt.title}.mp4'
            dst = 'Downloads'
            shutil.move(src, dst)
            self.label_8.setText("Your video has been downloaded, Congrats!")
            self.label_9.setText("Please check the Downloads directory.")
        except:
            self.label_8.setText('An error occurred. Please try again.')
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
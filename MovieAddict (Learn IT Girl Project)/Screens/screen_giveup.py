import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import webbrowser
import os
path = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\EASY"
import sys

#function for reading the files
def read(filename):
    fh = open(filename)
    return fh.read()

dir = os.listdir(path)
from random import shuffle     #choose movie names randomly
f = [movie for movie in dir]   #list with all the movies in the chosen level of difficulty folder
shuffle(f)
h = []
#iterating through all movie folders in the folder
for i in f:
    #create the paths for the movie folders
    m = os.path.join(path, i)

    imdb = os.path.join(m, 'imdblink.txt')
    rt = os.path.join(m, 'rtlink.txt')

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    next = QPushButton("Next question")
    next.setStyleSheet("height:50px;"
                     "background-color:#FFFDFD;"
                     "border-width:2px; "
                     "margin-left:100px;"
                     "margin-right:100px")
    quit = QPushButton("Quit")
    quit.setStyleSheet("height:50px;"
                     "background-color:#FFFDFD;"
                     "border-width:2px;"
                     "margin-left:100px;"
                     "margin-right:100px")

    d = QLabel()
    d.setText("<details>")
    d.setAlignment(Qt.AlignCenter)

    dbl = QPushButton("imdb")
    dbl.setStyleSheet("background-color:#3A9076;"
                    "margin-right:450px;"
                    "margin-left:20px;"
                    "height:20px;"
                    "margin-top:30px;"
                    "border-radius:10px")
    QObject.connect(dbl,SIGNAL("clicked()"),open_imdb)

    rtl = QPushButton("rotten tomatoes")
    rtl.setStyleSheet("background-color:#3A9076;"
                    "margin-right:450px;"
                    "margin-left:20px;"
                    "height:20px;"
                    "border-radius:10px")
    QObject.connect(rtl,SIGNAL("clicked()"),open_rt)

    vbox = QVBoxLayout()
    vbox.addWidget(next)
    vbox.addWidget(quit)
    vbox.addStretch()
    vbox.addWidget(d)
    vbox.addStretch()
    vbox.addWidget(dbl)
    vbox.addWidget(rtl)
    win.setLayout(vbox)

    win.setGeometry(200,80,600,400)
    win.setWindowTitle("Movie Addict")
    win.show()
    sys.exit(app.exec_())

def open_imdb():
    k = read(imdb)
    webbrowser.open(k)
def open_rt():
    l = read(rt)
    webbrowser.open(l)

window()
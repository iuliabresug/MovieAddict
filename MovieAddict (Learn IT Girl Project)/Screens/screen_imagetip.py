import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
path = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\EASY"

dir = os.listdir(path)
from random import shuffle     #choose movie names randomly
f = [movie for movie in dir]   #list with all the movies in the chosen level of difficulty folder
shuffle(f)
h = []
#iterating through all movie folders in the folder
for i in f:
    m = os.path.join(path, i)
    img1 = os.path.join(m, 'image_1.jpg')

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    i = QLabel()
    i.setPixmap(QPixmap(img1))
    i.setMaximumSize(250,200)
    i.setScaledContents(True)
    i.setAlignment(Qt.AlignCenter)  #it doesn't work

    t1 = QPushButton("image(easy)")
    t1.setStyleSheet("height:40px;"
                     "background-color:#FFF96C;"
                     "border-width:2px;"
                     "margin-top:90px")
    t2 = QPushButton("image(hard)")
    t2.setStyleSheet("height:40px;"
                     "background-color:#FFD16B;"
                     "border-width:2px;"
                     "margin-top:90px")
    t3 = QPushButton("quote")
    t3.setStyleSheet("height:40px;"
                     "background-color:#F5A657;"
                     "border-width:2px;"
                     "margin-top:90px")
    t4 = QPushButton("fun fact")
    t4.setStyleSheet("height:40px;"
                     "background-color:#F58157;"
                     "border-width:2px;"
                     "margin-top:90px")
    g = QLabel()
    g.setText("What is the movie?")
    g.setAlignment(Qt.AlignCenter)
    d = QLabel()
    d.setText("<help>")
    d.setAlignment(Qt.AlignCenter)
    d.setStyleSheet("margin-top:50px")
    m = QLineEdit()
    m.setStyleSheet("border: 0px;"
                    "background: #FBFCE6;"
                    "selection-background-color: #F1ABAB;"
                    "margin-right:50px;"
                    "margin-left:50px;"
                    "height:30px;"
                    "font-size:15px;"
                    "margin-top:50px")
    x = QPushButton("I give up")
    x.setStyleSheet("background-color:#3A9076;"
                    "margin-right:180px;"
                    "margin-left:180px;"
                    "height:20px;"
                    "margin-top:30px")

    fbox = QFormLayout()

    vbox = QVBoxLayout()
    vbox.addWidget(g)
    vbox.addStretch()
    vbox.addWidget(m)
    vbox.addStretch()
    vbox.addWidget(i)
    vbox.addWidget(d)
    vbox.addStretch()

    hbox = QHBoxLayout()
    hbox.addWidget(t1)
    hbox.addWidget(t2)
    hbox.addWidget(t3)
    hbox.addWidget(t4)

    fbox.addItem(vbox)
    fbox.addItem(hbox)
    fbox.addRow(x)


    win.setLayout(fbox)

    win.setGeometry(200,80,600,400)
    win.setWindowTitle("Movie Addict")
    win.show()
    sys.exit(app.exec_())

window()
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
import webbrowser
path = "C:\Users\Iulia\PycharmProjects\MovieAddict\MovieAddict\EASY"

#function for reading the files
def read(filename):
    if filename.endswith("txt"):
        fh = open(filename)
        return fh.read()
    else:
        webbrowser.open(filename)

dir = os.listdir(path)
from random import shuffle     #choose movie names randomly
f = [movie for movie in dir]   #list with all the movies in the chosen level of difficulty folder
shuffle(f)
h = []
#iterating through all movie folders in the folder
for i in f:

    m = os.path.join(path, i)

    help = os.path.join(m, 'help.txt')
    q1 = os.path.join(m, 'quote_1.txt')
    #for tips:
    q2 = os.path.join(m, 'quote_2.txt')
    img1 = os.path.join(m, 'image_1.jpg')
    img2 = os.path.join(m, 'image_2.jpg')
    ff = os.path.join(m, 'funfact.txt')

    #list with all files
    g = [m, q1, q2, img1, img2, ff]

    #dictionary and function for the tips
    tips = {'q': q2, 'i': img1, 'j': img2,'f': ff}

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    #textbox for writing the movie:
    write = QLineEdit()
    write.setAlignment(Qt.AlignCenter)

    #function for the guess button:
    def button_clicked():
       if write.text() == i:
          print ("Correct!")
       else:
          print ("Wrong!")

    #functions for the tips buttons:
    def t1_clicked():
        p2.setPixmap(QPixmap(img1))

    def t2_clicked():
        p2.setPixmap(QPixmap(img2))

    def t3_clicked():
        p1.setText(read(q2))
        p1.setWordWrap(True)

    def t4_clicked():
        p1.setText(read(ff))
        p1.setWordWrap(True)


    #Guess button:
    button = QPushButton("Guess")
    QObject.connect(button,SIGNAL("clicked()"),button_clicked)

    #Tips buttons:
    t1 = QPushButton("image(easy)")
    t1.setStyleSheet("height:40px;"
                     "background-color:#FFF96C;"
                     "border-width:2px")
    QObject.connect(t1,SIGNAL("clicked()"),t1_clicked)
    t2 = QPushButton("image(hard)")
    t2.setStyleSheet("height:40px;"
                     "background-color:#FFD16B;"
                     "border-width:2px")
    QObject.connect(t2,SIGNAL("clicked()"),t2_clicked)
    t3 = QPushButton("quote")
    t3.setStyleSheet("height:40px;"
                     "background-color:#F5A657;"
                     "border-width:2px")
    QObject.connect(t3,SIGNAL("clicked()"),t3_clicked)
    t4 = QPushButton("fun fact")
    t4.setStyleSheet("height:40px;"
                     "background-color:#F58157;"
                     "border-width:2px")
    QObject.connect(t4,SIGNAL("clicked()"),t4_clicked)

    #give up button:
    x = QPushButton("I give up")
    x.setStyleSheet("background-color:#3A9076;"
                    "margin-right:180px;"
                    "margin-left:180px;"
                    "height:20px;"
                    "margin-top:30px")

    #display the quote and the help to guess the movie:
    h = QPushButton(read(help))
    h.setStyleSheet("border-style: outset; "
                     "background-color:white;"
                     "border-width: 2px; "
                     "border-color:beige ")
    q = QPushButton(read(q1))
    q.setStyleSheet("background-color:white;"
                     "border-style: outset; "
                     "border-width: 2px; "
                     "border-color:beige ")

    #widget for showing the tips:
    p1 = QLabel()
    p1.setStyleSheet("background-color:#D8F3D4")
    p1.setAlignment(Qt.AlignCenter)
    p2 = QLabel()
    p2.setStyleSheet("background-color:#D8F3D4")
    p2.setAlignment(Qt.AlignCenter)

    fbox = QFormLayout()

    vbox = QVBoxLayout()
    vbox.addWidget(q)
    vbox.addWidget(h)
    vbox.addStretch()
    vbox.addWidget(write)
    vbox.addStretch()
    vbox.addWidget(button)
    vbox.addWidget(p1)
    vbox.addWidget(p2)

    hbox = QHBoxLayout()
    hbox.addWidget(t1)
    hbox.addWidget(t2)
    hbox.addWidget(t3)
    hbox.addWidget(t4)

    fbox.addItem(vbox)
    fbox.addItem(hbox)
    fbox.addRow(x)

    win.setLayout(fbox)
    win.setWindowTitle("Movie Addict")
    win.show()
    sys.exit(app.exec_())

window()

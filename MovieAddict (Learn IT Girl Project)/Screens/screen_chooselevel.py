import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    a1 = QPushButton("EASY")
    a1.setStyleSheet("margin-right:100px; "
                     "margin-left:100px;"
                     "height:30px;"
                     "background-color:white;"
                     "border-style: outset; "
                     "border-width: 2px; "
                     "border-color:beige ")
    a2 = QPushButton("MEDIUM")
    a2.setStyleSheet("margin-right:100px; "
                     "margin-left:100px;"
                     "height:30px;"
                     "background-color:white;"
                     "border-style: outset; "
                     "border-width: 2px; "
                     "border-color:beige ")
    a3 = QPushButton("HARD")
    a3.setStyleSheet("margin-right:100px; "
                     "margin-left:100px;"
                     "height:30px;"
                     "background-color:white;"
                     "border-style: outset; "
                     "border-width: 2px; "
                     "border-color:beige ")
    b1 = QLabel()
    b1.setStyleSheet("color:#380000 ;"
                     "font:bold,large,Arial;"
                     "font-size:20px ")

    b1.setText("Choose level of difficulty")
    b1.setAlignment(Qt.AlignCenter)

    vbox = QVBoxLayout()
    vbox.addStretch()
    vbox.addWidget(b1)
    vbox.addStretch()
    vbox.addWidget(a1)
    vbox.addWidget(a2)
    vbox.addWidget(a3)
    vbox.addStretch()

    win.setLayout(vbox)

    win.setGeometry(200,200,600,400)
    win.setWindowTitle("Movie Addict")
    win.show()
    sys.exit(app.exec_())

window()
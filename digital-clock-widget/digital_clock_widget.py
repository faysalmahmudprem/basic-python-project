# digital clock widget

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
            self.setWindowTitle("Digital clock")
            self.setGeometry(600,400,300,100)    # can change it according screen size

            vbox = QVBoxLayout()
            vbox.addWidget(self.time_label)
            self.setLayout(vbox)

            self.time_label.setAlignment(Qt.AlignCenter)

            self.time_label.setStyleSheet("font-size: 150px;"
                                          "font-family: Arial;"
                                          "color: hsl(111, 100%, 50%);")
            
            self.setStyleSheet("background-color: black;")

            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)

            self.update_time()

    def update_time(self):
         current_time = QTime.currentTime().toString("hh:mm:ss AP")
         self.time_label.setText(current_time)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()        
    sys.exit(app.exec_())

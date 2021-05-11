import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Example(QWidget):
   def __init__(self):
      super(Example, self).__init__()
      self.initUI()

   def initUI(self):
      self.text = "hello world"
      self.setGeometry(400,400, 600,600)
      self.setWindowTitle('Draw Demo')
      self.show()

   def paintEvent(self, event):
      qp = QPainter()
      qp.begin(self)
      qp.setPen(QColor(Qt.red))
      qp.setFont(QFont('Arial', 50))
      qp.drawText(10,50, "hello Annie")
      qp.setPen(QColor(Qt.red))
      qp.drawLine(10,100,100,500)
      qp.drawRect(10,150,500,500)
      qp.setPen(QColor(Qt.blue))
      qp.drawEllipse(100,50,100,50)
      qp.drawPixmap(220,10,QPixmap("pythonlogo.png"))
      qp.fillRect(20,175,130,250,QBrush(Qt.SolidPattern))
      qp.end()

def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
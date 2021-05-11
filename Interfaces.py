import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

def dialog():

    mbox = QMessageBox()



    mbox.setText("Hey Annie. Watch this!!!!!!")

    mbox.setDetailedText("Noooooooooooooooooooooooooooooooooooooooo")

    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            

    mbox.exec_()

def Training():
    Text=input("What will we print")
    print(Text)




if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = QWidget()

    w.resize(1000,500)

    w.setWindowTitle('Our Widget!')

    

    label = QLabel(w)

    label.setText("Ya goot see this")

    label.move(0,0)

    label.show()



    btn = QPushButton(w)

    btn.setText('Press here')

    btn.move(10,20)

    btn.show()

    btn.clicked.connect(dialog)

        
    btn2 = QPushButton(w)

    btn2.setText('Press here2')

    btn2.move(100,200)

    btn2.show()

    btn2.clicked.connect(Training)



    

    w.show()

    sys.exit(app.exec_())
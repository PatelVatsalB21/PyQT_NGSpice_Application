import sys
from PyQt5.QtWidgets import *
from worker import Worker
import os

class PyUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.outSignal.connect(self.logging)
        self.setWindowTitle('Netlist Simulator')
        self.setGeometry(200, 200, 600, 600)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self.btn = QPushButton("Add Netlist File")
        self.btn.clicked.connect(self.getfile)

        self.generalLayout.addWidget(self.btn)
        self.le = QLabel("Process Instruction will be displayed here.")
                    
        self.generalLayout.addWidget(self.le)
		
    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Netlist (*.cir *.cir.out)")[0]
        self.le.setText("File Selected")
        d = os.path.dirname(fname)
        d = d.replace('/','\\')
        f = os.path.basename(fname)
        self.le.setText("Source Directory is " + d + " and the selected file is " + f)
        command = "ngspice " + f
        self.worker.run_command(command, cwd=d, shell=True)

    def logging(self, string):
        self.le.setText(string.strip())
        

def main():
    pyapp = QApplication(sys.argv)
    view = PyUi()
    view.show()
    sys.exit(pyapp.exec_())

if __name__ == '__main__':
    main()

import sys

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import *
from worker import Worker
import os

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyUi(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.outSignal.connect(self.logging)
        # Set some main window's properties
        self.setWindowTitle('PyCalc')
        self.setFixedSize(600, 600)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self.btn = QPushButton("Add File")
        self.btn.clicked.connect(self.getfile)

        self.generalLayout.addWidget(self.btn)
        self.le = QLabel("Hello")
                    
        self.generalLayout.addWidget(self.le)
		
    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Netlist (*.cir *.cir.out)")[0]
        self.le.setText("File Selected")
        d = os.path.dirname(fname)
        d = d.replace('/','\\')
        f = os.path.basename(fname)
        self.le.setText(d)
        command = "ngspice " + f
        self.worker.run_command(command, cwd=d, shell=True)

    def logging(self, string):
        self.le.setText(string.strip())

        

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyUi()
    view.show()
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()

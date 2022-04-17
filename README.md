# PyQT_NGSpice_Application
This project is developed to interface ngspice and build a desktop application using PyQt5 framework.

## Table of Contents
- [Abstract](#abstract)
- [App Functioning](#app-functioning)
- [Steps to run this project](#steps-to-run-this-project)
- [Next Steps](#next-steps)
- [Software Used](#software-used)
  * [NgSpice](#ngspice)
  * [PyQT](#pyqt)
- [Author](#author)


## Abstract
ngspice is the open source spice simulator for electric and electronic circuits. ngspice offers a wealth of device models for active, passive, analog, and digital elements. Model parameters are provided by our collections, by the semiconductor device manufacturers, or from semiconductor foundries. The user adds her circuits as a netlist, and the output is one or more graphs of currents, voltages and other electrical quantities or is saved in a data file. Its input is command line or file based.

PyQt is one of the most popular Python bindings for the Qt cross-platform C++ framework. PyQt was developed by Riverbank Computing Limited. Qt itself is developed as part of the Qt Project. PyQt4 runs on Windows, Linux, Mac OS X and various UNIX platforms. PyQt5 also runs on Android and iOS.

## App Functioning

The app has been made with the help of PyQT framework. There is a main screen where a button and a display are available. Button can be used to locate and upload the netlist file (With .cir extension) that are compatible with ngspice. Display is available for informing user according to the actions of the user.

There are two python programs made in the app
- App.py
- Worker.py

### App.py
It defines the UI of the app and consist of code related to PyQT.

### Worker.py
It is made to interact with the command prompt or terminal. It send the commands to the command prompt and also logs the outputs and errors from it. It is then call by App.py for use.

## Steps to run this project
1. Open a new terminal
2. Clone this project using the following command:</br>
```git clone https://github.com/PatelVatsalB21/PyQT_NGSpice_Application.git```</br>
3. Run the python file app.py directly or via terminal:</br>
```python app.py```</br>
4. Click on the Add Netlist File button</br>
5. Locate the netlist file with ".cir" extension
6. Wait for process to complete and then save the simulation results generated.

## Next Steps
 As the project is working fine now it needs to enhance the UI. The ngspice windows should not be visile along with the outputs. All the simulation logs and the outputs should be visible within PyQT app itself. This can be done in three ways that needs to be tested.
 - Controlling the ngspice processes and shoe it in PyQT app
 - Use NGspice to generate ".raw" file and parse it withe the help of [LTspice library](https://pypi.org/project/ltspice/) and simulate and generate outputs
 - Use [Pyspice library](https://pyspice.fabrice-salvaire.fr/releases/v1.4/overview.html#:~:text=PySpice%20is%20an%20open%20source,by%20the%20Sandia%20National%20Laboratories.) that provides integration of NGspice andpython combined for ease of use and it is free and opensource.











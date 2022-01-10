# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Electricity.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(293, 296)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.PreviousRead = QtWidgets.QLineEdit(self.groupBox)
        self.PreviousRead.setObjectName("PreviousRead")
        self.gridLayout.addWidget(self.PreviousRead, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.CurrentRead = QtWidgets.QLineEdit(self.groupBox)
        self.CurrentRead.setText("")
        self.CurrentRead.setObjectName("CurrentRead")
        self.gridLayout.addWidget(self.CurrentRead, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 2)
        self.TotalRead = QtWidgets.QLineEdit(self.groupBox)
        self.TotalRead.setText("")
        self.TotalRead.setObjectName("TotalRead")
        self.gridLayout.addWidget(self.TotalRead, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.Bill = QtWidgets.QLineEdit(self.groupBox)
        self.Bill.setText("")
        self.Bill.setObjectName("Bill")
        self.gridLayout.addWidget(self.Bill, 3, 2, 1, 1)
        self.Tax = QtWidgets.QCheckBox(self.groupBox)
        self.Tax.setObjectName("Tax")
        self.gridLayout.addWidget(self.Tax, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.Ouput = QtWidgets.QLineEdit(self.groupBox)
        self.Ouput.setEnabled(True)
        self.Ouput.setClearButtonEnabled(False)
        self.Ouput.setObjectName("Ouput")
        self.gridLayout.addWidget(self.Ouput, 6, 1, 1, 1)
        self.Calculate = QtWidgets.QPushButton(self.groupBox)
        self.Calculate.setObjectName("Calculate")
        self.Calculate.clicked.connect(self.Run)
        self.gridLayout.addWidget(self.Calculate, 6, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bill Calculator"))
        self.groupBox.setTitle(_translate("Dialog", "Calculator"))
        self.label.setText(_translate("Dialog", "Previous Reading (KW.h)"))
        self.label_2.setText(_translate("Dialog", "Current Reading (KW.h)"))
        self.label_5.setText(_translate("Dialog", "Total Reading (KW.h)"))
        self.label_3.setText(_translate("Dialog", "Bill amount (Fils)"))
        self.Tax.setText(_translate("Dialog", "Add Taxes"))
        self.label_4.setText(_translate("Dialog", "Amount (JD)"))
        self.Calculate.setText(_translate("Dialog", "Calculate"))

    def Run(self):

        CurrentRead = float(self.CurrentRead.text())
        PreviousRead = float(self.PreviousRead.text())
        TotalCost = float(self.Bill.text())
        TotalRead = float(self.TotalRead.text())
        cost = 0
        MonthRead = CurrentRead - PreviousRead
        Read = TotalRead - MonthRead

        print(MonthRead)
        print(Read)

        for i in range(4):
            if i == 0:
                
                if (Read<160):
                    cost += Read*33
                    
                    break
                else:
                    Read -=160
                    cost += 160*33
                                      

            elif i==1:
                
                if (Read<140):
                    cost += Read*72
                    break
                else:
                    Read -=140
                    cost += 140*72
                                      
                
            elif i==3:
                if (Read<299):
                    cost += Read*86
                    
                    break
                else:
                    Read -=299
                    cost += 299*86

        output = (TotalCost - cost)
        print(cost)

        if (self.Tax.isChecked()):
            output += MonthRead*18  #Fuel price compensation
            output += MonthRead*5 + 1.6   #Garbage
            output += MonthRead     #Reef fils

        self.Ouput.setText(str(round((output)/1000,3))) 

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


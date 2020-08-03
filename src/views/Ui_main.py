# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\FHL\MyProject\PyProject\rt_uiauto\src\views\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 837)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 900))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_button.setObjectName("select_button")
        self.horizontalLayout.addWidget(self.select_button)
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setObjectName("run_button")
        self.horizontalLayout.addWidget(self.run_button)
        self.analyze_button = QtWidgets.QPushButton(self.centralwidget)
        self.analyze_button.setObjectName("analyze_button")
        self.horizontalLayout.addWidget(self.analyze_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tableWidget.setFont(font)
        self.tableWidget.setGridStyle(QtCore.Qt.DashDotLine)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setObjectName("add_button")
        self.verticalLayout2.addWidget(self.add_button)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setObjectName("clear_button")
        self.verticalLayout2.addWidget(self.clear_button)
        self.validate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.validate_btn.setObjectName("validate_btn")
        self.verticalLayout2.addWidget(self.validate_btn)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout2.addWidget(self.save_btn)
        self.load_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_btn.setObjectName("load_btn")
        self.verticalLayout2.addWidget(self.load_btn)
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setObjectName("play_btn")
        self.verticalLayout2.addWidget(self.play_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout2)
        self.scriptVerticalLayout = QtWidgets.QVBoxLayout()
        self.scriptVerticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.scriptVerticalLayout.setObjectName("scriptVerticalLayout")
        self.horizontalLayout_2.addLayout(self.scriptVerticalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UIAuto"))
        self.select_button.setText(_translate("MainWindow", "Select..."))
        self.run_button.setText(_translate("MainWindow", "Run..."))
        self.analyze_button.setText(_translate("MainWindow", "Analyze..."))
        self.textBrowser.setPlaceholderText(_translate("MainWindow", "Keep the application that your wanna to analyze getting focus"))
        self.tableWidget.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "ControlType"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "ClassName"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Rect"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "Handle"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "Depth"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.add_button.setText(_translate("MainWindow", "Add..."))
        self.clear_button.setText(_translate("MainWindow", "Clear..."))
        self.validate_btn.setText(_translate("MainWindow", "Validate..."))
        self.save_btn.setText(_translate("MainWindow", "Save..."))
        self.load_btn.setText(_translate("MainWindow", "Load..."))
        self.play_btn.setText(_translate("MainWindow", "Play..."))
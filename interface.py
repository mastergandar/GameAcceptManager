# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(493, 187)
        MainWindow.setMinimumSize(QtCore.QSize(493, 187))
        MainWindow.setMaximumSize(QtCore.QSize(493, 187))
        MainWindow.setAccessibleName("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 491, 161))
        self.tabWidget.setMinimumSize(QtCore.QSize(491, 161))
        self.tabWidget.setMaximumSize(QtCore.QSize(491, 161))
        self.tabWidget.setWhatsThis("")
        self.tabWidget.setObjectName("tabWidget")
        self.work_space = QtWidgets.QWidget()
        self.work_space.setObjectName("work_space")
        self.Start_button = QtWidgets.QPushButton(self.work_space)
        self.Start_button.setGeometry(QtCore.QRect(290, 10, 191, 51))
        self.Start_button.setObjectName("Start_button")
        self.textEdit = QtWidgets.QTextEdit(self.work_space)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 271, 121))
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName("textEdit")
        self.Pause_button = QtWidgets.QPushButton(self.work_space)
        self.Pause_button.setGeometry(QtCore.QRect(290, 70, 191, 61))
        self.Pause_button.setObjectName("Pause_button")
        self.tabWidget.addTab(self.work_space, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.settings.setObjectName("settings")
        self.sensetivity_edit = QtWidgets.QLineEdit(self.settings)
        self.sensetivity_edit.setEnabled(True)
        self.sensetivity_edit.setGeometry(QtCore.QRect(350, 10, 131, 20))
        self.sensetivity_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.sensetivity_edit.setObjectName("sensetivity_edit")
        self.label = QtWidgets.QLabel(self.settings)
        self.label.setGeometry(QtCore.QRect(10, 10, 341, 20))
        self.label.setObjectName("label")
        self.Save_button = QtWidgets.QPushButton(self.settings)
        self.Save_button.setGeometry(QtCore.QRect(350, 90, 131, 41))
        self.Save_button.setObjectName("Save_button")
        self.tabWidget.addTab(self.settings, "")
        self.contacts = QtWidgets.QWidget()
        self.contacts.setObjectName("contacts")
        self.label_2 = QtWidgets.QLabel(self.contacts)
        self.label_2.setGeometry(QtCore.QRect(350, 0, 131, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/avatar.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.contacts)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 331, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.contacts)
        self.label_4.setGeometry(QtCore.QRect(350, 110, 131, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.contacts)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 191, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.contacts)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 261, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.contacts)
        self.label_7.setGeometry(QtCore.QRect(90, 0, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.contacts, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Game Accept Manager"))
        self.Start_button.setText(_translate("MainWindow", "Запуск"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to the GAME (Game Manager Accept)!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Before starting, go to settings and calibrate the program(in development[by default, the program works with a resolution of 1920x1080])</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After calibration, select the algorithm sensitivity(for 1920x1080 resolution, the recommended sensitivity is 4000000)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For the program to work it is necessary that The DotA 2 window does not overlap with anything!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Also, mouse movements are emulated for taking the game(do not touch the mouse while taking the game!)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Добро пожаловать в GAM (Game Accept Manager)!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Перед запуском зайдите в настройки и отколибруйте программу(в разработке[по умолчанию программа работает с разрешением 1920x1080])</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">После калибровки выберите чувствительность алгоритма(для разрешения 1920х1080 рекомендуемая чувствительность 4000000)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Для работы программы нужно чтобы окно </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dota 2 ни чем не перекрывалось!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Также для принятия игры эмулируются движения мыши(не трогайте мышь во время принятия игры!)</p></body></html>"))
        self.Pause_button.setText(_translate("MainWindow", "Остановка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.work_space), _translate("MainWindow", "Главная"))
        self.sensetivity_edit.setText(_translate("MainWindow", "4000000"))
        self.label.setText(_translate("MainWindow", "Чувствительность алгоритма (рекомендуемое значение 4000000)"))
        self.Save_button.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "Настройки"))
        self.label_3.setText(_translate("MainWindow", "GitHub: https://github.com/mastergandar/"))
        self.label_4.setText(_translate("MainWindow", "Колганов Владимир"))
        self.label_5.setText(_translate("MainWindow", "Discord: mastergandar#5066"))
        self.label_6.setText(_translate("MainWindow", "Steam: https://steamcommunity.com/id/mastergand/"))
        self.label_7.setText(_translate("MainWindow", "Контакты"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contacts), _translate("MainWindow", "Об авторе"))

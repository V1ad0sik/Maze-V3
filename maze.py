# PyQT V 5.15.2
# Python V 3.9.1

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog

from threading import Thread

import pymem, requests, time, ctypes, re, numpy, keyboard, configparser
from PIL import ImageColor
from math import *
from win32api import GetKeyState
from win32gui import GetWindowText, GetForegroundWindow

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 275)
        ch_box_style = "QCheckBox {color: white; font: 12pt \"Arial\"; font-weight: bold; padding-top: -1px;} QCheckBox::indicator {width: 15px; height: 15px; border: 1px solid white; } QCheckBox::indicator:unchecked {background-color: rgb(30,30,30);} QCheckBox::indicator:unchecked:hover {background-color: rgb(45,45,45); } QCheckBox::indicator:checked {background-color: red;}"
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 630, 275))
        self.label.setStyleSheet("background-color: rgb(40,40,40);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 630, 27))
        self.label_2.setStyleSheet("background-color: rgb(60,60,60);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 27, 630, 2))
        self.label_3.setStyleSheet("background-color: #00a8ff;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(3, 2, 49, 23))
        self.label_4.setStyleSheet("font: 14pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(5, 35, 200, 235))
        self.label_5.setStyleSheet("background-color: rgb(50,50,50); border: 1px solid white;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(5, 35, 200, 30))
        self.label_6.setStyleSheet("background-color: rgb(50,50,50); font: 14pt \"Arial\"; border: 1px solid white;")
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(10, 70, 56, 18))
        self.checkBox.setStyleSheet(ch_box_style)
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 69, 30, 20))
        self.pushButton_3.setStyleSheet("QPushButton{background-color: rgb(255,255,255); border: none; border-radius: 2px;}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 95, 127, 18))
        self.checkBox_2.setStyleSheet(ch_box_style)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 120, 77, 18))
        self.checkBox_3.setStyleSheet(ch_box_style)
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(169, 120, 30, 20))
        self.pushButton_4.setStyleSheet("QPushButton{background-color: rgb(255,255,255); border: none; border-radius: 2px;}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 145, 101, 18))
        self.checkBox_4.setStyleSheet(ch_box_style)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 165, 130, 22))
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #00a8ff; height: 9px; background: #273c75;} QSlider::handle:horizontal {background:#0097e6; width: 15px;}")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setProperty("value", 1000)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 166, 40, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(30,30,30); border: 1px solid white; border-radius: 2px; color: white; font: 10pt \"Arial\"; font-weight: bold;")
        self.lineEdit.setMaxLength(5)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 190, 56, 18))
        self.checkBox_5.setStyleSheet(ch_box_style)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 210, 130, 22))
        self.horizontalSlider_2.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #00a8ff; height: 9px; background: #273c75;} QSlider::handle:horizontal {background:#0097e6; width: 15px;}")
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(160)
        self.horizontalSlider_2.setProperty("value", 90)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 212, 40, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(30,30,30); border: 1px solid white; border-radius: 2px; color: white; font: 10pt \"Arial\"; font-weight: bold;")
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_2.setCursorPosition(2)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 235, 103, 18))
        self.checkBox_6.setStyleSheet(ch_box_style)
        self.checkBox_6.setObjectName("checkBox_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(215, 35, 200, 235))
        self.label_7.setStyleSheet("background-color: rgb(50,50,50); border: 1px solid white;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(215, 35, 200, 30))
        self.label_8.setStyleSheet("background-color: rgb(50,50,50); font: 14pt \"Arial\"; border: 1px solid white;")
        self.label_8.setObjectName("label_8")
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setGeometry(QtCore.QRect(220, 70, 82, 18))
        self.checkBox_7.setStyleSheet(ch_box_style)
        self.checkBox_7.setObjectName("checkBox_7")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(320, 92, 90, 23))
        self.comboBox.setStyleSheet("QComboBox{ font-size: 14px; border: none; background-color: rgb(40,40,40); color: white; font-weight: bold; border: 1px solid gray;} QComboBox::drop-down{border: none; background-color: rgb(100,100,100); font-weight: bold;}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(220, 95, 73, 20))
        self.label_9.setStyleSheet("font: 12pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(220, 120, 33, 20))
        self.label_10.setStyleSheet("font: 12pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 120, 60, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(30,30,30); border: 1px solid white; border-radius: 2px; color: white; font: 10pt \"Arial\"; font-weight: bold;")
        self.lineEdit_3.setMaxLength(2)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(220, 145, 60, 20))
        self.label_11.setStyleSheet("font: 12pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 145, 60, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(30,30,30); border: 1px solid white; border-radius: 2px; color: white; font: 10pt \"Arial\"; font-weight: bold;")
        self.lineEdit_4.setMaxLength(4)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox_8 = QtWidgets.QCheckBox(Form)
        self.checkBox_8.setGeometry(QtCore.QRect(220, 170, 137, 18))
        self.checkBox_8.setStyleSheet(ch_box_style)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Form)
        self.checkBox_9.setGeometry(QtCore.QRect(220, 195, 108, 18))
        self.checkBox_9.setStyleSheet(ch_box_style)
        self.checkBox_9.setObjectName("checkBox_9")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(220, 215, 43, 20))
        self.label_12.setStyleSheet("font: 12pt \"Arial\";")
        self.label_12.setObjectName("label_12")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 218, 60, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(30,30,30); border: 1px solid white; border-radius: 2px; color: white; font: 10pt \"Arial\"; font-weight: bold;")
        self.lineEdit_5.setMaxLength(3)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(220, 244, 52, 20))
        self.label_13.setStyleSheet("font: 12pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 242, 90, 23))
        self.comboBox_2.setStyleSheet("QComboBox{ font-size: 14px; border: none; background-color: rgb(40,40,40); color: white; font-weight: bold; border: 1px solid gray;} QComboBox::drop-down{border: none; background-color: rgb(100,100,100); font-weight: bold;}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(425, 35, 200, 235))
        self.label_14.setStyleSheet("background-color: rgb(50,50,50); border: 1px solid white;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(425, 35, 200, 30))
        self.label_15.setStyleSheet("background-color: rgb(50,50,50); font: 14pt \"Arial\"; border: 1px solid white;")
        self.label_15.setObjectName("label_15")
        self.checkBox_10 = QtWidgets.QCheckBox(Form)
        self.checkBox_10.setGeometry(QtCore.QRect(430, 70, 120, 18))
        self.checkBox_10.setStyleSheet(ch_box_style)
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(Form)
        self.checkBox_11.setGeometry(QtCore.QRect(430, 95, 106, 18))
        self.checkBox_11.setStyleSheet(ch_box_style)
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(Form)
        self.checkBox_12.setGeometry(QtCore.QRect(430, 120, 110, 20))
        self.checkBox_12.setStyleSheet(ch_box_style)
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(Form)
        self.checkBox_13.setGeometry(QtCore.QRect(430, 145, 112, 18))   
        self.checkBox_13.setStyleSheet(ch_box_style)
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(Form)
        self.checkBox_14.setGeometry(QtCore.QRect(430, 170, 91, 18))
        self.checkBox_14.setStyleSheet(ch_box_style)
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(Form)
        self.checkBox_15.setGeometry(QtCore.QRect(430, 195, 122, 18))
        self.checkBox_15.setStyleSheet(ch_box_style)
        self.checkBox_15.setObjectName("checkBox_15")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(605, 0, 25, 27))
        self.pushButton.setStyleSheet("QPushButton{color: white; background-color: rgb(60,60,60); font-size: 18px; font-weight: bold; border: none;padding-left: 2px;} QPushButton:hover {color: red; background-color: rgb(70,70,70);} QPushButton:pressed {background-color: rgb(75,75,75);}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 0, 25, 27))
        self.pushButton_2.setStyleSheet("QPushButton{color: white; background-color: rgb(60,60,60); font-size: 18px; font-weight: bold; border: none;padding-left: 2px;} QPushButton:hover {background-color: rgb(70,70,70);} QPushButton:pressed {background-color: rgb(75,75,75);}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Maze V3"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Maze</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Visual</span></p></body></html>"))
        self.checkBox.setText(_translate("Form", "ESP"))
        self.checkBox_2.setText(_translate("Form", "Dynamic ESP"))
        self.checkBox_3.setText(_translate("Form", "Chams"))
        self.checkBox_4.setText(_translate("Form", "Night Mod"))
        self.lineEdit.setText(_translate("Form", "1.000"))
        self.checkBox_5.setText(_translate("Form", "FOV"))
        self.lineEdit_2.setText(_translate("Form", "90"))
        self.checkBox_6.setText(_translate("Form", "Global WH"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Target</span></p></body></html>"))
        self.checkBox_7.setText(_translate("Form", "AIM Bot"))
        self.comboBox.setItemText(0, _translate("Form", "Голова"))
        self.comboBox.setItemText(1, _translate("Form", "Шея"))
        self.comboBox.setItemText(2, _translate("Form", "Грудь"))
        self.comboBox.setItemText(3, _translate("Form", "Живот"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">AIM Bone</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">FOV</span></p></body></html>"))
        self.lineEdit_3.setText(_translate("Form", "26"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Smooth</span></p></body></html>"))
        self.lineEdit_4.setText(_translate("Form", "2000"))
        self.checkBox_8.setText(_translate("Form", "Semi-Rage AIM"))
        self.checkBox_9.setText(_translate("Form", "Trigger Bot"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Delay</span></p></body></html>"))
        self.lineEdit_5.setText(_translate("Form", "0.1"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Button</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Form", "mouse 3"))
        self.comboBox_2.setItemText(1, _translate("Form", "mouse 4"))
        self.comboBox_2.setItemText(2, _translate("Form", "mouse 5"))
        self.comboBox_2.setItemText(3, _translate("Form", "mouse 6"))
        self.comboBox_2.setItemText(4, _translate("Form", "No Key"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Misc</span></p></body></html>"))
        self.checkBox_10.setText(_translate("Form", "Skinchanger"))
        self.checkBox_11.setText(_translate("Form", "Auto Pistol"))
        self.checkBox_12.setText(_translate("Form", "Bunny Hop"))
        self.checkBox_13.setText(_translate("Form", "Radar Hack"))
        self.checkBox_14.setText(_translate("Form", "No Falsh"))
        self.checkBox_15.setText(_translate("Form", "Show Money"))
        self.pushButton.setText(_translate("Form", "☓"))
        self.pushButton_2.setText(_translate("Form", "-"))

class Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            x_main, y_main = self.geometry().x(), self.geometry().y()
            cursor_x, cursor_y = QtGui.QCursor.pos().x(), QtGui.QCursor.pos().y()

            if x_main <= cursor_x <= x_main + self.geometry().width():
                if y_main <= cursor_y <= y_main + self.geometry().height():
                    self.old_pos = event.pos()
                else:
                    self.old_pos = None
        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
    	try:
    		if not self.old_pos:
    			return

    		delta = event.pos() - self.old_pos
    		self.move(self.pos() + delta)
    	except:
    		pass

def WallHack_ESP():

    ESPR_, ESPG_, ESPB_ = float(ESPR / 255), float(ESPG / 255), float(ESPB / 255)

    while wallHack_esp_status:

        player = pm.read_int(client + dwLocalPlayer)
        glow_manager = pm.read_int(client + dwGlowObjectManager)
        team  = pm.read_int(player + m_iTeamNum)

        for i in range(1, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

                if entity_team_id != team :

                    if dynamic_status == True:

                        entity_hp = pm.read_int(entity + m_iHealth)
                        if entity_hp > 60:
                            ESPR_, ESPG_, ESPB_ = ESPR, ESPG, ESPB
                        if entity_hp < 40:
                            ESPR_, ESPG_, ESPB_ = 1,1,0
                        if entity_hp < 20:
                            ESPR_, ESPG_, ESPB_ = 1,0,0

                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(ESPR_))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(ESPG_))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(ESPB_))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, length)

                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)

def Chams():
	while wallHack_chams_status:

		player = pm.read_int(client + dwLocalPlayer)
		team = pm.read_int(player + m_iTeamNum)

		for ent_id in range(1, 32):
			ent = pm.read_int(client + dwEntityList + ent_id * 0x10)

			if ent:
				entity_team_id = pm.read_int(ent + m_iTeamNum)

				if entity_team_id != team:
					pm.write_int(ent + m_clrRender, CHAMSR)
					pm.write_int(ent + m_clrRender + 1, CHAMSG)
					pm.write_int(ent + m_clrRender + 2, CHAMSB)
					pm.write_int(ent + m_clrRender + 3, 1)

		time.sleep(0.2)

def night_mod__():
    while night_mod_status:
        for i in range(0, 2048):
            entity = pm.read_uint(client + dwEntityList + i * 0x10)
            if entity:
                EntityClassID = pm.read_int(entity + 0x8)
                huita1 = pm.read_int(EntityClassID + 2 * 0x4)
                huita2 = pm.read_int(huita1 + 0x1)
                huita3 = pm.read_int(huita2 + 20)

                if (huita3 != 69):
                    continue
                
                if (True):
                    pm.write_int(entity + m_bUseCustomAutoExposureMin, 1)
                    pm.write_int(entity + m_bUseCustomAutoExposureMax, 1)
                    pm.write_float(entity + m_flCustomAutoExposureMin, night_mod)
                    pm.write_float(entity + m_flCustomAutoExposureMax, night_mod)
                else:
                    pm.write_bool(entity + m_bUseCustomAutoExposureMin, 0)
                    pm.write_bool(entity + m_bUseCustomAutoExposureMax, 0)
        time.sleep(1)

def FOVP():
	try:
		player = pm.read_int(client + dwLocalPlayer)
		pm.write_int(player + m_iDefaultFOV, fovp)
	except:
		pass

def WallHack_mod():
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,'client.dll')
        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F',clientModule).start() + 2
        pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
        pm.close_process()

def calc_distance(current_x, current_y, new_x, new_y):
    distancex = new_x - current_x
    if distancex < -89:
        distancex += 360
    elif distancex > 89:
        distancex -= 360
    if distancex < 0.0:
        distancex = -distancex

    distancey = new_y - current_y

    if distancey < -180:
        distancey += 360
    elif distancey > 180:
        distancey -= 360
    if distancey < 0.0:
        distancey = -distancey
    return distancex, distancey

def checkangles(x, y):
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else:
        return True

def normalizeAngles(viewAngleX, viewAngleY):
    if viewAngleX > 89:
        viewAngleX -= 360
    if viewAngleX < -89:
        viewAngleX += 360
    if viewAngleY > 180:
        viewAngleY -= 360
    if viewAngleY < -180:
        viewAngleY += 360
    return viewAngleX, viewAngleY

def calcangle(localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3):
    delta_x, delta_y, delta_z = localpos1 - enemypos1, localpos2 - enemypos2, localpos3 - enemypos3
    hyp = sqrt( delta_x * delta_x + delta_y * delta_y + delta_z * delta_z )

    try:
    	x = asin( delta_z / hyp ) * 57.295779513082
    	y = atan( delta_y / delta_x ) * 57.295779513082
    except:
    	x,y = 0

    if delta_x >= 0.0:
        y += 180.0
    return x, y

def GetBestBoneTarget(mypos_x, mypos_y, mypos_z, viewanglex, viewangley, entity):
    diffs = []
    for x in range(4):
        if x == 0:
            x = 5
        elif x == 1:
            x = 6
        elif x == 2:
            x = 7
        elif x == 3:
            x = 8

        entity_bones = pm.read_int(entity + m_dwBoneMatrix)
        entitypos_x = pm.read_float(entity_bones + 0x30 * x + 0xC)
        entitypos_y = pm.read_float(entity_bones + 0x30 * x + 0x1C)
        entitypos_z = pm.read_float(entity_bones + 0x30 * x + 0x2C)
        X, Y = calcangle(mypos_x, mypos_y, mypos_z, entitypos_x, entitypos_y, entitypos_z)
        distancex, distancey = calc_distance(viewanglex, viewangley, X, Y)
        diffs.append(distancex + distancey)
    if diffs:
        return int(numpy.argmin(diffs)) + 5

def GetBestTarget():
    global enginepointer
    while True:
        olddistx = 111111111111
        olddisty = 111111111111
        newdist_x, newdist_y = 0, 0
        target = None
        aimlocalplayer = pm.read_int(client + dwLocalPlayer)
        enginepointer = pm.read_int(engine + dwClientState)
        if aimlocalplayer:
            localplayer_team = pm.read_int(aimlocalplayer + m_iTeamNum)
            localplayer_index = pm.read_int(aimlocalplayer + 0x64) - 1
            for x in range(32):
                if pm.read_int(client + dwEntityList + x * 0x10):
                    entity = pm.read_int(client + dwEntityList + x * 0x10)
                    entity_hp = pm.read_int(entity + m_iHealth)
                    entity_team = pm.read_int(entity + m_iTeamNum)
                    spotted = pm.read_int(entity + m_bSpottedByMask)
                    if spotted == 1 << localplayer_index and localplayer_team != entity_team and entity_hp > 0:
                        entity_bones = pm.read_int(int(entity) + int(m_dwBoneMatrix))
                        localpos_x_angles = pm.read_float(int(enginepointer) + int(dwClientState_ViewAngles))
                        localpos_y_angles = pm.read_float(enginepointer + dwClientState_ViewAngles + 0x4)
                        localpos1 = pm.read_float(aimlocalplayer + m_vecOrigin)
                        localpos2 = pm.read_float(aimlocalplayer + m_vecOrigin + 4)
                        localpos_z_angles = pm.read_float(aimlocalplayer + m_vecViewOffset + 0x8)
                        localpos3 = pm.read_float(aimlocalplayer + m_vecOrigin + 8) + localpos_z_angles
                        aimbone = GetBestBoneTarget(localpos1, localpos2, localpos3, localpos_x_angles, localpos_y_angles, entity)
                        entitypos_x = pm.read_float(entity_bones + 0x30 * bone + 0xC)
                        entitypos_y = pm.read_float(entity_bones + 0x30 * bone + 0x1C)
                        entitypos_z = pm.read_float(entity_bones + 0x30 * bone + 0x2C)
                        X, Y = calcangle(localpos1, localpos2, localpos3, entitypos_x, entitypos_y, entitypos_z)
                        newdist_x, newdist_y = calc_distance(localpos_x_angles, localpos_y_angles, X, Y)
                        if newdist_x < olddistx and newdist_y < olddisty:
                            olddistx = newdist_x
                            olddisty = newdist_y
                            target = entity
                            target_hp = pm.read_int(target + m_iHealth)
            if target and target_hp > 0:
                return target, aimbone, aimlocalplayer

def aimthread():
    while aim_status:
        aimplayer, aimbone, aimlocalplayer = GetBestTarget()
        aimplayer_hp = pm.read_int(aimplayer + m_iHealth)
        aimplayerbone = pm.read_int(aimplayer + m_dwBoneMatrix)
        localpos1 = pm.read_float(aimlocalplayer + m_vecOrigin)
        localpos2 = pm.read_float(aimlocalplayer + m_vecOrigin + 4)
        localpos_z_angles = pm.read_float(aimlocalplayer + m_vecViewOffset + 0x8)
        localpos3 = pm.read_float(aimlocalplayer + m_vecOrigin + 8) + localpos_z_angles
        enemypos1 = pm.read_float(aimplayerbone + 0x30 * bone + 0xC)
        enemypos2 = pm.read_float(aimplayerbone + 0x30 * bone + 0x1C)
        enemypos3 = pm.read_float(aimplayerbone + 0x30 * bone + 0x2C)
        viewanglex = pm.read_float(enginepointer + dwClientState_ViewAngles)
        viewangley = pm.read_float(enginepointer + dwClientState_ViewAngles + 0x4)
        x, y = calcangle(localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3)
        diff_x = x - viewanglex
        diff_y = y - viewangley
        diff_x, diff_y = normalizeAngles(diff_x, diff_y)
        distancex, distancey = calc_distance(viewanglex, viewangley, x, y)
        if distancex < fov and distancey < fov and aimplayer_hp > 0:
            pm.write_float(enginepointer + dwClientState_ViewAngles, viewanglex + (diff_x / smooth))
            pm.write_float(enginepointer + dwClientState_ViewAngles + 0x4, viewangley + (diff_y / smooth))

def aim_lock():
        while aim_lock_status:

            target = None
            olddistx = 111111111111
            olddisty = 111111111111
 
            try:
                player = pm.read_int( client + dwLocalPlayer)
                engine_pointer = pm.read_int(engine + dwClientState)
                localTeam = pm.read_int(player + m_iTeamNum)
            except:
                time.sleep(1)
                continue

            for i in range(1, 64):
                entity = pm.read_int(client + dwEntityList + i * 0x10)

                if entity:
                    try:
                        entity_team_id, entity_hp, entity_dormant = pm.read_int(entity + m_iTeamNum), pm.read_int(entity + m_iHealth), pm.read_int(entity + m_bDormant) 
                    except:
                        time.sleep(1)
                        continue

                    if localTeam != entity_team_id and entity_hp > 0:
                        entity_bones = pm.read_int( entity + m_dwBoneMatrix )
                        localpos_x_angles, localpos_y_angles = pm.read_float( engine_pointer + dwClientState_ViewAngles ), pm.read_float( engine_pointer + dwClientState_ViewAngles + 0x4 )
                        localpos1, localpos2  = pm.read_float( player + m_vecOrigin ), pm.read_float( player + m_vecOrigin + 4 )

                        localpos_z_angles = pm.read_float( player + m_vecViewOffset + 0x8 )
                        localpos3 = pm.read_float( player + m_vecOrigin + 8 ) + localpos_z_angles

                       	try:
                       		entitypos_x = pm.read_float( entity_bones + 0x30 * aim_lock_bone + 0xC )
                       		entitypos_y = pm.read_float( entity_bones + 0x30 * aim_lock_bone + 0x1C )
                       		entitypos_z = pm.read_float( entity_bones + 0x30 * aim_lock_bone + 0x2C )
                       	except:
                       		continue

                        X, Y = calcangle( localpos1, localpos2, localpos3, entitypos_x, entitypos_y, entitypos_z )
                        newdist_x, newdist_y = calc_distance( localpos_x_angles, localpos_y_angles, X, Y )

                        if newdist_x < olddistx and newdist_y < olddisty and newdist_x <= 26 and newdist_y <= 26:

                            olddistx, olddisty = newdist_x, newdist_y
                            target, target_hp, target_dormant = entity, entity_hp, entity_dormant
                            target_x, target_y, target_z = entitypos_x, entitypos_y, entitypos_z

                    if target and target_hp > 0 and not target_dormant:

                        pitch, yaw = calcangle( localpos1, localpos2, localpos3, target_x, target_y, target_z )
                        normalize_x, normalize_y = normalizeAngles( pitch, yaw )
                        punchx, punchy = pm.read_float( player + m_aimPunchAngle ), pm.read_float( player + m_aimPunchAngle + 0x4 )

                        if aimrcs and pm.read_int( player + m_iShotsFired ) > 1:
                            pm.write_float( engine_pointer + dwClientState_ViewAngles, normalize_x - (punchx * 2) )
                            pm.write_float( engine_pointer + dwClientState_ViewAngles + 0x4, normalize_y - (punchy * 2) )
                        else:
                        	pm.write_float(engine_pointer + dwClientState_ViewAngles, normalize_x)
                        	pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, normalize_y)

def trigger_bot_no_key():
    while trigger_bot_status_no_key:

        player = pm.read_int(client + dwLocalPlayer)
        entity_id = pm.read_int(player + m_iCrosshairId)
        entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

        entity_team = pm.read_int(entity + m_iTeamNum)
        player_team = pm.read_int(player + m_iTeamNum)
        if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
            time.sleep (delay)
            pm.write_int(client + dwForceAttack, 6)

        time.sleep(0.01)

def trigger_bot():
    while trigger_bot_status:
    	if GetKeyState(mouse) == -127 or GetKeyState(mouse) == -128:
	        player = pm.read_int(client + dwLocalPlayer)
	        entity_id = pm.read_int(player + m_iCrosshairId)
	        entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

	        entity_team = pm.read_int(entity + m_iTeamNum)
	        player_team = pm.read_int(player + m_iTeamNum)

	        if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
	            time.sleep (delay)
	            pm.write_int(client + dwForceAttack, 6)

    	time.sleep(0.05)

def skinchanger():
	while skinchanger_status:

		engine_state = pm.read_int(int(engine) + int(dwClientState))
		local_player = pm.read_int(client + dwLocalPlayer)

		if local_player == 0:
			continue

		for i in range(0, 8):
			my_weapons = pm.read_int(local_player + m_hMyWeapons + (i - 1) * 0x4) & 0xFFF
			weapon_address = pm.read_int(client + dwEntityList + (my_weapons - 1) * 0x10)

			if weapon_address:
				weapon_id = pm.read_int(weapon_address + m_iItemDefinitionIndex)
				weapon_owner = pm.read_int(weapon_address + m_OriginalOwnerXuidLow)

				if weapon_id in gun_id_list:
					fallbackpaint = gun_id_list[weapon_id]
				else:
					continue

				pm.write_int(weapon_address + m_iItemIDHigh, -1)
				pm.write_int(weapon_address + m_nFallbackPaintKit, fallbackpaint)
				pm.write_int(weapon_address + m_iAccountID, weapon_owner)
				pm.write_int(weapon_address + m_nFallbackStatTrak, 1337)
				pm.write_int(weapon_address + m_nFallbackSeed, seed)
				pm.write_float(weapon_address + m_flFallbackWear, float(0.000001))

		if keyboard.is_pressed( "f6" ):
			pm.write_int(engine_state + 0x174, -1)

def Auto_Pistol():
    while auto_pistol_status:
        if GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
        	if GetKeyState(0x01) == -127 or GetKeyState(0x01) == -128:
        		pm.write_int(client + dwForceAttack, 6)
        time.sleep(0.02)
        	

def Bunny_Hop():
    while bunny_hop_status:

    	player = pm.read_int(client + dwLocalPlayer)
    	force_jump = (client + dwForceJump)

    	if pm.read_int(client + dwLocalPlayer):
    		on_ground = pm.read_int(player + m_fFlags)
    		if keyboard.is_pressed("space") :
    			if on_ground == 257 or on_ground == 263:
    				pm.write_int(force_jump, 5)
    				time.sleep(0.17)
    				pm.write_int(force_jump, 4)

def Radar_Hack():
	pm = pymem.Pymem('csgo.exe')
	client = pymem.process.module_from_name(pm.process_handle, 'client.dll')
	clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
	address = client.lpBaseOfDll + re.search(rb'\x80\xB9.{5}\x74\x12\x8B\x41\x08', clientModule).start() + 6
	pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)
	pm.close_process()

def NoFlash():
    while no_flash_status:
    	player = pm.read_int(client + dwLocalPlayer)
    	flash_value = (player + m_flFlashMaxAlpha)

    	if player:
    		if flash_value:
    			pm.write_float(flash_value, float(0)) 
    	time.sleep(0.1)

def Show_Money_mod():
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,'client.dll')
        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',clientModule).start()
        pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)

if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   ui = Widget()
   ui.show()

   def start_variable():
   	global ESPR, ESPG, ESPB, CHAMSR, CHAMSG, CHAMSB
   	global wallHack_esp_status, dynamic_status, length, wallHack_chams_status, night_mod_status, night_mod, fovp, fov, smooth, aim_status, bone, aim_lock_status, aimrcs, aim_lock_bone, trigger_bot_status, delay, mouse, trigger_bot_status_no_key, skinchanger_status, gun_id_list, seed, auto_pistol_status, bunny_hop_status, no_flash_status

   	gun_id_list = {32:0, 262205:0, 4:0, 2:0, 36:0, 30:0, 262207:0, 1:0, 3:0, 262208:0, 35:0, 25:0, 27:0, 14:0, 28:0, 29:0, 17:0, 262167:0, 24:0, 19:0, 26:0, 34:0, 33:0, 10:0, 16:0, 262204:0, 40:0, 8:0, 9:0, 38:0, 13:0, 7:0, 39:0, 11:0}

   	ESPR, ESPG, ESPB = 255,255,255
   	CHAMSR, CHAMSG, CHAMSB = 255,255,255

   	length = 0.9
   	night_mod = 1.000
   	fovp = 90
   	fov = 26
   	smooth = 2000
   	bone = 8
   	aim_lock_bone = 8
   	delay = 0.1
   	mouse = 4
   	seed = 500

   	wallHack_esp_status = False
   	dynamic_status = False
   	wallHack_chams_status = False
   	night_mod_status = False
   	aim_status = False
   	aim_lock_status = False
   	aimrcs = True
   	trigger_bot_status = False
   	trigger_bot_status_no_key = False
   	skinchanger_status = False
   	auto_pistol_status = False
   	bunny_hop_status = False
   	no_flash_status = False

   def No_Flash_():
   	global no_flash_status

   	if bool(ui.checkBox_14.isChecked()) == True:
   		no_flash_status = True
   		Thread(target = NoFlash).start()
   		return

   	if bool(ui.checkBox_14.isChecked()) == False:
   		no_flash_status = False
   		return

   def Bunny_Hop_():
   	global bunny_hop_status

   	if bool(ui.checkBox_12.isChecked()) == True:
   		bunny_hop_status = True
   		Thread(target = Bunny_Hop).start()
   		return

   	if bool(ui.checkBox_12.isChecked()) == False:
   		bunny_hop_status = False
   		return

   def Auto_Pistol_():
   	global auto_pistol_status

   	if bool(ui.checkBox_11.isChecked()) == True:
   		auto_pistol_status = True
   		Thread(target = Auto_Pistol).start()
   		return

   	if bool(ui.checkBox_11.isChecked()) == False:
   		auto_pistol_status = False
   		return

   def Skinchanger_():
   	global skinchanger_status, gun_id_list

   	config = configparser.ConfigParser()
   	config.read("skins.ini")
   	gun_id_list = {32:int(config.get("P2000", "sid")), 
		262205:   int(config.get("USP-S", "sid")), 
		4:        int(config.get("Glock", "sid")), 
		2:        int(config.get("Dual Berettas", "sid")), 
		36:       int(config.get("P250", "sid")), 
		30:       int(config.get("Tec-9", "sid")), 
		262207:   int(config.get("CZ75-Auto", "sid")), 
		1:        int(config.get("Desert Eagle", "sid")), 
		3:        int(config.get("Five-SeveN", "sid")), 
		262208:   int(config.get("R8", "sid")), 
		35:       int(config.get("Nova", "sid")), 
		25:       int(config.get("XM1014", "sid")), 
		27:       int(config.get("MAG-7", "sid")), 
		14:       int(config.get("M249", "sid")), 
		28:       int(config.get("Negev", "sid")), 
		29:       int(config.get("Sawed-Off", "sid")), 
		17:       int(config.get("MAC-10", "sid")), 
		262167:   int(config.get("MP5-SD", "sid")), 
		24:       int(config.get("UMP-45", "sid")), 
		19:       int(config.get("P90", "sid")), 
		26:       int(config.get("PP-19", "sid")), 
		34:       int(config.get("MP9", "sid")), 
		33:       int(config.get("MP7", "sid")), 
		10:       int(config.get("FAMAS", "sid")), 
		16:       int(config.get("M4A4", "sid")), 
		262204:   int(config.get("M4A1-S", "sid")), 
		40:       int(config.get("SSG 08", "sid")), 
		8:        int(config.get("AUG", "sid")), 
		9:        int(config.get("AWP", "sid")), 
		38:       int(config.get("SCAR-20", "sid")), 
		13:       int(config.get("Galil", "sid")), 
		7:        int(config.get("AK-47", "sid")), 
		39:       int(config.get("SG 553", "sid")), 
		11:       int(config.get("C3SG1", "sid"))}

   	if bool(ui.checkBox_10.isChecked()) == True:
   		skinchanger_status = True
   		Thread(target = skinchanger).start()
   		return

   	if bool(ui.checkBox_10.isChecked()) == False:
   		skinchanger_status = False

   def AIM_Lock_():
   	global aim_lock_status

   	if bool(ui.checkBox_8.isChecked()) == True:
   		ui.checkBox_7.setChecked(False)
   		AIM_()
   		aim_lock_status = True
   		Thread(target = aim_lock).start()
   		return
   	if bool(ui.checkBox_8.isChecked()) == False:
   		aim_lock_status = False
   		return

   def AIM_():
   	global aim_status, bone, fov, smooth 

   	if ui.comboBox.currentText() == 'Голова':
   		bone = 8
   	if ui.comboBox.currentText() == 'Шея':
   		bone = 7
   	if ui.comboBox.currentText() == 'Грудь':
   		bone = 5
   	if ui.comboBox.currentText() == 'Живот':
   		bone = 3

   	fov = int(ui.lineEdit_3.text())
   	smooth = int(ui.lineEdit_4.text())

   	if bool(ui.checkBox_7.isChecked()) == True:
   		aim_status = True
   		Thread(target = aimthread).start()
   		return

   	if bool(ui.checkBox_7.isChecked()) == False:
   		aim_status = False
   		return

   def FOVP_():
   	global fovp

   	fovp = int(ui.lineEdit_2.text())

   	if bool(ui.checkBox_5.isChecked()) == True:
   		FOVP()
   		return

   	if bool(ui.checkBox_5.isChecked()) == False:
   		fovp = 90
   		FOVP()
   		return

   def Night_mod_():
   	global night_mod_status

   	if bool(ui.checkBox_4.isChecked()) == True:
   		night_mod_status = True
   		Thread(target = night_mod__).start()
   		return

   	if bool(ui.checkBox_4.isChecked()) == False:
   		night_mod_status = False
   		return

   def Chams_():
   	global wallHack_chams_status

   	if bool(ui.checkBox_3.isChecked()) == True:
   		wallHack_chams_status = True
   		Thread(target = Chams).start()
   		return

   	if bool(ui.checkBox_3.isChecked()) == False: 
   		wallHack_chams_status = False
   		return

   def ESP_():
   	global wallHack_esp_status, dynamic_status

   	if bool(ui.checkBox.isChecked()) == True:
   		wallHack_esp_status = True
   		dynamic_status = bool(ui.checkBox_2.isChecked())
   		Thread(target = WallHack_ESP).start()
   		return

   	if bool(ui.checkBox.isChecked()) == False:
   		wallHack_esp_status = False
   		dynamic_status = bool(ui.checkBox_2.isChecked())
   		return

   def Trigger_Bot_():
   	global mouse, trigger_bot_status, trigger_bot_status_no_key

   	if ui.comboBox_2.currentText() == "mouse 3":
   		mouse = 3
   	if ui.comboBox_2.currentText() == "mouse 4":
   		mouse = 4
   	if ui.comboBox_2.currentText() == "mouse 5":
   		mouse = 5
   	if ui.comboBox_2.currentText() == "mouse 6":
   		mouse = 6
   	if ui.comboBox_2.currentText() == "No Key":
   		mouse = 0
   		trigger_bot_status_no_key = True

   	if bool(ui.checkBox_9.isChecked()) == True:
   		trigger_bot_status = True

   		if trigger_bot_status_no_key == True:
   			Thread(target = trigger_bot_no_key).start()
   			return
   		Thread(target = trigger_bot).start()
   		return

   	if bool(ui.checkBox_9.isChecked()) == False:
   		trigger_bot_status = False
   		trigger_bot_status_no_key = False
   		return

   def Set_Trigger_Bot_Delay():
   	global delay

   	try:
   		delay = float(ui.lineEdit_5.text())
   	except:
   		delay = 0.1
   		ui.lineEdit_5.setText(str(delay))

   	if float(ui.lineEdit_5.text()) < 0:
   		delay = 0.1
   		ui.lineEdit_5.setText(str(delay))

   	if float(ui.lineEdit_5.text()) > 5.0:
   		delay = 5.0
   		ui.lineEdit_5.setText(str(delay))

   def Set_AIM_Smooth():
   	global smooth

   	try:
   		smooth = int(ui.lineEdit_4.text())
   	except:
   		smooth = 2000
   		ui.lineEdit_4.setText(str(smooth))

   	if smooth > 2000:
   		smooth = 2000
   		ui.lineEdit_4.setText(str(smooth))

   	if smooth < 1:
   		smooth = 1
   		ui.lineEdit_4.setText(str(smooth))

   def Set_AIM_FOV():
   	global fov

   	try:
   		fov = int(ui.lineEdit_3.text())
   	except:
   		fov = 26
   		ui.lineEdit_3.setText(str(fov))

   	if fov < 1:
   		fov = 1
   		ui.lineEdit_3.setText(str(fov))

   	if fov > 26:
   		fov = 26
   		ui.lineEdit_3.setText(str(fov))   	

   def Set_FOVP_Value_Slider():
   	global fovp

   	try:
   		fovp = int(ui.lineEdit_2.text())
   	except:
   		fovp = 90
   		ui.lineEdit_2.setText(str(fovp))

   	if fovp > 160:
   		fovp = 90
   		ui.lineEdit_2.setText(str(fovp))

   	ui.horizontalSlider_2.setValue(int(fovp))

   def Set_FOVP_Value():
   	global fovp

   	try:
   		fovp = int(ui.lineEdit_2.text())
   	except:
   		fovp = 90
   		ui.lineEdit_2.setText(str(fovp))

   	if fovp > 160:
   		fovp = 90
   		ui.lineEdit_2.setText(str(fovp))


   	fovp = ui.horizontalSlider_2.value()
   	ui.lineEdit_2.setText(str(fovp))

   def Set_NM_Value_Slider():
   	global night_mod

   	try:
   		night_mod = float(ui.lineEdit.text())
   	except:
   		night_mod = 1.000
   		ui.lineEdit.setText(str(night_mod))

   	if night_mod > 1.000:
   		night_mod = 1.000
   		ui.lineEdit.setText(str(night_mod))

   	if night_mod < 0.1:
   		night_mod = 0.1
   		ui.lineEdit.setText(str(night_mod))

   	data = int(float(ui.lineEdit.text()) * 1000)
   	ui.horizontalSlider.setValue(data)

   def Set_NM_Value():
   	global night_mod

   	try:
   		night_mod = float(ui.lineEdit.text())
   	except:
   		night_mod = 1.000
   		ui.lineEdit.setText(str(night_mod))

   	if night_mod > 1.000:
   		night_mod = 1.000
   		ui.lineEdit.setText(str(night_mod))

   	data = float(ui.horizontalSlider.value() / 1000)
   	ui.lineEdit.setText(str(data))

   def Chams_Set_Color():
   	global CHAMSR, CHAMSG, CHAMSB

   	color = QColorDialog.getColor()

   	CHAMSR = ImageColor.getcolor(color.name(), "RGB")[0]
   	CHAMSG = ImageColor.getcolor(color.name(), "RGB")[1]
   	CHAMSB = ImageColor.getcolor(color.name(), "RGB")[2]

   	ui.pushButton_4.setStyleSheet("QPushButton{background-color: rgb(" + f"{CHAMSR},{CHAMSG},{CHAMSB}" + "); border: none; border-radius: 2px;}")

   def ESP_Set_Color():
   	global ESPR, ESPG, ESPB

   	color = QColorDialog.getColor()

   	ESPR = ImageColor.getcolor(color.name(), "RGB")[0]
   	ESPG = ImageColor.getcolor(color.name(), "RGB")[1]
   	ESPB = ImageColor.getcolor(color.name(), "RGB")[2]

   	ui.pushButton_3.setStyleSheet("QPushButton{background-color: rgb(" + f"{ESPR},{ESPG},{ESPB}" + "); border: none; border-radius: 2px;}")

   def read_game():
   	global pm, client, engine

   	global dwLocalPlayer, dwGlowObjectManager, dwEntityList, dwClientState, dwClientState_ViewAngles, dwForceAttack, dwForceJump
   	global m_iTeamNum, m_iGlowIndex, m_iHealth, m_clrRender, m_bUseCustomAutoExposureMin, m_bUseCustomAutoExposureMax, m_flCustomAutoExposureMin, m_flCustomAutoExposureMax, m_iDefaultFOV, m_bSpottedByMask, m_dwBoneMatrix, m_vecOrigin, m_vecViewOffset, m_bDormant, m_aimPunchAngle, m_iShotsFired, m_iCrosshairId, m_hMyWeapons, m_iItemDefinitionIndex, m_OriginalOwnerXuidLow, m_iItemIDHigh, m_nFallbackPaintKit, m_iAccountID, m_nFallbackStatTrak, m_nFallbackSeed, m_flFallbackWear, m_fFlags, m_flFlashMaxAlpha
   	
   	try:
   		pm = pymem.Pymem("csgo.exe")
   		client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
   		engine = pymem.process.module_from_name( pm.process_handle, "engine.dll" ).lpBaseOfDll
   	except pymem.exception.ProcessNotFound:
   		ctypes.windll.user32.MessageBoxW(0, u"Игра не запущена.", u"Ошибка", 0)
   		out_side()
   		return
   	except:
   		ctypes.windll.user32.MessageBoxW(0, "Не удалось подключиться к игре.", u"Ошибка", 0)
   		out_side()
   		return

   	def get_sig(modname, pattern, extra = 0, offset = 0, relative = True):
	    module = pymem.process.module_from_name(pm.process_handle, modname)
	    bytes = pm.read_bytes(module.lpBaseOfDll, module.SizeOfImage)
	    match = re.search(pattern, bytes).start()
	    non_relative = pm.read_int(module.lpBaseOfDll + match + offset) + extra
	    yes_relative = pm.read_int(module.lpBaseOfDll + match + offset) + extra - module.lpBaseOfDll
	    return "0x{:X}".format(yes_relative) if relative else "0x{:X}".format(non_relative)

   	offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
   	response = requests.get(offsets).json()

   	dwLocalPlayer = int(get_sig('client.dll', rb'\x8D\x34\x85....\x89\x15....\x8B\x41\x08\x8B\x48\x04\x83\xF9\xFF', 4, 3), 0)
   	dwGlowObjectManager = int(get_sig('client.dll', rb'\xA1....\xA8\x01\x75\x4B', 4, 1),0)
   	dwEntityList = int(get_sig('client.dll',rb'\xBB....\x83\xFF\x01\x0F\x8C....\x3B\xF8',0,1),0)
   	dwForceAttack = int(get_sig('client.dll', rb'\x89\x0D....\x8B\x0D....\x8B\xF2\x8B\xC1\x83\xCE\x04', 0, 2), 0)
   	dwForceJump = int(get_sig('client.dll', rb'\x8B\x0D....\x8B\xD6\x8B\xC1\x83\xCA\x02', 0, 2), 0)
   	dwClientState = int(response["signatures"]["dwClientState"])
   	dwClientState_ViewAngles = int(response["signatures"]["dwClientState_ViewAngles"])

   	m_iTeamNum = int(response["netvars"]["m_iTeamNum"])
   	m_iGlowIndex = int(response["netvars"]["m_iGlowIndex"])
   	m_iHealth = int(response["netvars"]["m_iHealth"])
   	m_clrRender = int(response["netvars"]["m_clrRender"])
   	m_bUseCustomAutoExposureMin = int(response["netvars"]["m_bUseCustomAutoExposureMin"])
   	m_bUseCustomAutoExposureMax = int(response["netvars"]["m_bUseCustomAutoExposureMax"])
   	m_flCustomAutoExposureMin = int(response["netvars"]["m_flCustomAutoExposureMin"]) 
   	m_flCustomAutoExposureMax = int(response["netvars"]["m_flCustomAutoExposureMax"])
   	m_bSpottedByMask = int(response["netvars"]["m_bSpottedByMask"])
   	m_dwBoneMatrix = int(response["netvars"]["m_dwBoneMatrix"])
   	m_vecOrigin = int(response["netvars"]["m_vecOrigin"])
   	m_vecViewOffset = int(response["netvars"]["m_vecViewOffset"])
   	m_bDormant = int(response["signatures"]["m_bDormant"])
   	m_aimPunchAngle = int(response["netvars"]["m_aimPunchAngle"])
   	m_iShotsFired = int(response["netvars"]["m_iShotsFired"])
   	m_iCrosshairId = int(response["netvars"]["m_iCrosshairId"])
   	m_hMyWeapons = int(response["netvars"]["m_hMyWeapons"])
   	m_iItemDefinitionIndex = int(response["netvars"]["m_iItemDefinitionIndex"])
   	m_OriginalOwnerXuidLow = int(response["netvars"]["m_OriginalOwnerXuidLow"])
   	m_iItemIDHigh = int(response["netvars"]["m_iItemIDHigh"])
   	m_nFallbackPaintKit = int(response["netvars"]["m_nFallbackPaintKit"])
   	m_iAccountID = int(response["netvars"]["m_iAccountID"])
   	m_nFallbackStatTrak = int(response["netvars"]["m_nFallbackStatTrak"])
   	m_nFallbackSeed = int(response["netvars"]["m_nFallbackSeed"])
   	m_flFallbackWear = int(response["netvars"]["m_flFallbackWear"])
   	m_fFlags = int(response["netvars"]["m_fFlags"])
   	m_flFlashMaxAlpha = int(response["netvars"]["m_flFlashMaxAlpha"])
   	m_iDefaultFOV = 0x332C

   def fall():
   	ui.showMinimized()

   def out_side():
   	global wallHack_esp_status, wallHack_chams_status, night_mod_status, night_mod_status, aim_status, aim_lock_status, trigger_bot_status, trigger_bot_status_no_key, skinchanger_status, auto_pistol_status, bunny_hop_status, no_flash_status

   	save_cfg()

   	wallHack_esp_status = False
   	wallHack_chams_status = False
   	night_mod_status = False
   	night_mod_status = False
   	aim_status = False
   	aim_lock_status = False
   	trigger_bot_status = False
   	trigger_bot_status_no_key = False
   	skinchanger_status = False
   	auto_pistol_status = False
   	bunny_hop_status = False
   	no_flash_status = False
   	exit()

   def save_cfg():

   	open('setting.ini', 'w')
   	config = configparser.ConfigParser()
   	config.read('setting.ini')

   	config.add_section("ESP")
   	config.set("ESP", "Status", str(wallHack_esp_status))
   	config.set("ESP", "R", str(ESPR))
   	config.set("ESP", "G", str(ESPG))
   	config.set("ESP", "B", str(ESPB))
   	config.set("ESP", "length", str(length))

   	config.add_section("Dynamic ESP")
   	config.set("Dynamic ESP", "Status", str(dynamic_status))

   	config.add_section("Chams")
   	config.set("Chams", "Status", str(wallHack_chams_status))
   	config.set("Chams", "R", str(CHAMSR))
   	config.set("Chams", "G", str(CHAMSG))
   	config.set("Chams", "B", str(CHAMSB))

   	config.add_section("Night Mod")
   	config.set("Night Mod", "Status", str(night_mod_status))
   	config.set("Night Mod", "value", str(night_mod))

   	config.add_section("FOV")
   	config.set("FOV", "Status", str(ui.checkBox_5.isChecked()))
   	config.set("FOV", "value", str(fovp))

   	config.add_section("Global WH")
   	config.set("Global WH", "Status", str(ui.checkBox_6.isChecked()))

   	config.add_section("AIM Bot")
   	config.set("AIM Bot", "Status", str(aim_status))
   	config.set("AIM Bot", "bone", str(bone))
   	config.set("AIM Bot", "fov", str(fov))
   	config.set("AIM Bot", "smooth", str(smooth))

   	config.add_section("Semi-Rage AIM")
   	config.set("Semi-Rage AIM", "Status", str(aim_lock_status))
   	config.set("Semi-Rage AIM", "bone", str(aim_lock_bone))

   	config.add_section("Trigger Bot")
   	config.set("Trigger Bot", "Status", str(trigger_bot_status))
   	config.set("Trigger Bot", "No_Key_Status", str(trigger_bot_status_no_key))
   	config.set("Trigger Bot", "mouse", str(mouse))
   	config.set("Trigger Bot", "delay", str(delay))

   	config.add_section("Misc")
   	config.set("Misc", "Skinchanger", str(skinchanger_status))
   	config.set("Misc", "Auto Pistol", str(auto_pistol_status))
   	config.set("Misc", "Bunny Hop", str(bunny_hop_status))
   	config.set("Misc", "Radar Hack", str(ui.checkBox_13.isChecked()))
   	config.set("Misc", "No Falsh", str(no_flash_status))
   	config.set("Misc", "Show Money", str(ui.checkBox_15.isChecked()))

   	with open('setting.ini', "w") as config_file:
   		config.write(config_file)

   def load_cfg():
   	global ESPR, ESPG, ESPB, CHAMSR, CHAMSG, CHAMSB
   	global wallHack_esp_status, dynamic_status, length, wallHack_chams_status, night_mod_status, night_mod, fovp, fov, smooth, aim_status, bone, aim_lock_status, aimrcs, aim_lock_bone, trigger_bot_status, delay, mouse, trigger_bot_status_no_key, skinchanger_status, gun_id_list, seed, auto_pistol_status, bunny_hop_status, no_flash_status

   	try:
   		open('setting.ini', 'r')
   	except FileNotFoundError:
   		return

   	config = configparser.ConfigParser()
   	config.read('setting.ini')

   	wallHack_esp_status = config.get("ESP", "Status")

   	ESPR = float(config.get("ESP", "R"))
   	ESPG = float(config.get("ESP", "G"))
   	ESPB = float(config.get("ESP", "B"))

   	ui.pushButton_3.setStyleSheet("QPushButton{background-color: rgb(" + f"{ESPR},{ESPG},{ESPB}" + "); border: none; border-radius: 2px;}")

   	length = float(config.get("ESP", "length"))

   	if wallHack_esp_status == 'True':
   		ui.checkBox.setChecked(True)
   		ESP_()

   	dynamic_status = config.get("Dynamic ESP", "Status")

   	if dynamic_status == 'True':
   		ui.checkBox_2.setChecked(True)
   		ESP_()

   	wallHack_chams_status = config.get("Chams", "Status")

   	CHAMSR = int(config.get("Chams", "R"))
   	CHAMSG = int(config.get("Chams", "G"))
   	CHAMSB = int(config.get("Chams", "B"))

   	ui.pushButton_4.setStyleSheet("QPushButton{background-color: rgb(" + f"{CHAMSR},{CHAMSG},{CHAMSB}" + "); border: none; border-radius: 2px;}")

   	if wallHack_chams_status == 'True':
   		ui.checkBox_3.setChecked(True)
   		Chams_()

   	night_mod_status = config.get("Night Mod", "Status")
   	night_mod = float(config.get("Night Mod", "value"))

   	ui.lineEdit.setText(str(night_mod))
   	a = float(night_mod) * 1000
   	ui.horizontalSlider.setValue(int(a))

   	if night_mod_status == 'True':
   		ui.checkBox_4.setChecked(True)
   		Night_mod_()

   	fov_status = config.get("FOV", "Status")
   	fov_value = config.get("FOV", "value")

   	ui.lineEdit_2.setText(str(fov_value))
   	ui.horizontalSlider_2.setValue(int(fov_value))

   	if fov_status == 'True':
   		ui.checkBox_5.setChecked(True)
   		FOVP_()

   	global_wh_status = config.get("Global WH", "Status")

   	if global_wh_status == 'True':
   		ui.checkBox_6.setChecked(True)
   		WallHack_mod()

   	aim_status = config.get("AIM Bot", "Status")

   	bone = int(config.get("AIM Bot", "bone"))

   	if bone == 8:
   		ui.comboBox.setCurrentText("Голова");
   	if bone == 7:
   		ui.comboBox.setCurrentText("Шея");
   	if bone == 5:
   		ui.comboBox.setCurrentText("Грудь");
   	if bone == 3:
   		ui.comboBox.setCurrentText("Живот");

   	fov = int(config.get("AIM Bot", "fov"))
   	ui.lineEdit_3.setText(str(fov))

   	smooth = int(config.get("AIM Bot", "smooth"))
   	ui.lineEdit_4.setText(str(smooth))

   	if aim_status == 'True':
   		ui.checkBox_7.setChecked(True)
   		AIM_()

   	aim_lock_status = config.get("Semi-Rage AIM", "Status")
   	aim_lock_bone = int(config.get("Semi-Rage AIM", "bone"))

   	if aim_lock_status == 'True':
   		ui.checkBox_8.setChecked(True)
   		AIM_Lock_()

   	delay = float(config.get("Trigger Bot", "delay"))
   	ui.lineEdit_5.setText(str(delay))

   	mouse = int(config.get("Trigger Bot", "mouse"))

   	if mouse == 3:
   		ui.comboBox_2.setCurrentText("mouse 3");
   	if mouse == 4:
   		ui.comboBox_2.setCurrentText("mouse 4");
   	if mouse == 5:
   		ui.comboBox_2.setCurrentText("mouse 5");
   	if mouse == 6:
   		ui.comboBox_2.setCurrentText("mouse 6");
   	if mouse == 0:
   		ui.comboBox_2.setCurrentText("No Key");
   		trigger_bot_no_key = True

   	trigger_bot_status = config.get("Trigger Bot", "Status")
   	print(trigger_bot_status)

   	if trigger_bot_status == 'True':
   		ui.checkBox_9.setChecked(True)
   		Trigger_Bot_()

   	skinchanger_status = config.get("Misc", "Skinchanger")
   	auto_pistol_status = config.get("Misc", "Auto Pistol")
   	bunny_hop_status = config.get("Misc", "Bunny Hop")
   	no_flash_status = config.get("Misc", "No Falsh")
   	show_money = config.get("Misc", "Show Money")

   	if skinchanger_status == 'True':
   		ui.checkBox_10.setChecked(True)
   		Skinchanger_()

   	if auto_pistol_status == 'True':
   		ui.checkBox_11.setChecked(True)
   		Auto_Pistol_()

   	if bunny_hop_status == 'True':
   		ui.checkBox_12.setChecked(True)
   		Bunny_Hop_()

   	if no_flash_status == 'True':
   		ui.checkBox_13.setChecked(True)
   		No_Flash_()

   	if show_money == 'True':
   		ui.checkBox_14.setChecked(True)
   		Show_Money_mod()

   start_variable()
   read_game()
   load_cfg()

   ui.pushButton.clicked.connect(out_side)
   ui.pushButton_2.clicked.connect(fall)

   ui.pushButton_3.clicked.connect(ESP_Set_Color)
   ui.pushButton_4.clicked.connect(Chams_Set_Color)

   ui.checkBox.stateChanged.connect(ESP_)
   ui.checkBox_2.stateChanged.connect(ESP_)
   ui.checkBox_3.stateChanged.connect(Chams_)
   ui.checkBox_4.stateChanged.connect(Night_mod_)
   ui.checkBox_5.stateChanged.connect(FOVP_)
   ui.checkBox_6.stateChanged.connect(WallHack_mod)
   ui.checkBox_7.stateChanged.connect(AIM_)
   ui.checkBox_8.stateChanged.connect(AIM_Lock_)
   ui.checkBox_9.stateChanged.connect(Trigger_Bot_)
   ui.checkBox_10.stateChanged.connect(Skinchanger_)
   ui.checkBox_11.stateChanged.connect(Auto_Pistol_)
   ui.checkBox_12.stateChanged.connect(Bunny_Hop_)
   ui.checkBox_13.stateChanged.connect(Radar_Hack)
   ui.checkBox_14.stateChanged.connect(No_Flash_)
   ui.checkBox_15.stateChanged.connect(Show_Money_mod)

   ui.horizontalSlider.valueChanged.connect(Set_NM_Value)
   ui.horizontalSlider_2.valueChanged.connect(Set_FOVP_Value)

   ui.lineEdit.textChanged.connect(Set_NM_Value_Slider)
   ui.lineEdit_2.textChanged.connect(Set_FOVP_Value_Slider)
   ui.lineEdit_3.textChanged.connect(Set_AIM_FOV)
   ui.lineEdit_4.textChanged.connect(Set_AIM_Smooth)
   ui.lineEdit_5.textChanged.connect(Set_Trigger_Bot_Delay)

   sys.exit(app.exec_())

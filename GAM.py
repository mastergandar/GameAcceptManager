from multiprocessing import Process, Queue
import os
import sys

location = sys.executable

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = location[:-10] + 'Lib\site-packages\PyQt5\Qt\plugins'
os.environ['PATH'] += ';' + location[:-10] + 'Lib\site-packages\PyQt5\Qt\bin'

from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from interface import Ui_MainWindow

import mss
import mss.tools
import numpy
import pyautogui
import sys

programm = True
game_accepted = 0
sensetivity = 0

class mywindow(QtWidgets.QMainWindow):

	def __init__(self):
		
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.ui.Start_button.clicked.connect(self.start_clicked)
		self.ui.Pause_button.clicked.connect(self.pause_clicked)
		self.ui.Save_button.clicked.connect(self.save_clicked)

	def start_clicked(self):

		global game_accepted
		game_accepted = 0

		def grab():
			
			rect = {"top": 361, "left": 573, "width": 773, "height": 259}
			output = "img/Find.png"
	
			with mss.mss() as sct:

				sct_img = sct.grab(rect)
				mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

			print(output)

	
		def find(state):
	
			print("Loading Image #1")
			img1 = Image.open("img/Accept.png")
			print("Loading Image #2")
			img2 = Image.open("img/Find.png")
			
			similarity = 0

			for band_index, band in enumerate(img1.getbands()):

				m1 = numpy.array([p[band_index] for p in img1.getdata()]).reshape(*img1.size)
				m2 = numpy.array([p[band_index] for p in img2.getdata()]).reshape(*img2.size)
				similarity += numpy.sum(numpy.abs(m1-m2))

			print(similarity)
			print("Чувствительность алгоритма = %s" % sensetivity)
			if similarity < int(sensetivity):
				
				print("ИГРА НАЙДЕНА")
				global game_accepted
				game_accepted = 1
				pyautogui.moveTo (956, 520)
				pyautogui.click(button = 'left')

		while programm == True:
			if game_accepted == 0:
				grab()
				find(game_accepted)
				self.statusBar().showMessage('Программа работает')
				print(game_accepted)
				app.processEvents()

			elif game_accepted == 1:
				print(game_accepted)
				self.statusBar().showMessage('ИГРА НАЙДЕНА! Программа приостановлена')
				break

			elif game_accepted == 2:
				break

	def pause_clicked(self):

		global game_accepted
		game_accepted = 2

		self.statusBar().showMessage('Программа приостановленна')

	def save_clicked(self):

		global sensetivity
		sensetivity = self.ui.sensetivity_edit.text()
		print("Чувствительность алгоритма = %s" % sensetivity)

app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()

sys.exit(app.exec())
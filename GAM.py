import os
import sys

location = sys.executable

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = location[:-10] + 'Lib\site-packages\PyQt5\Qt\plugins'
os.environ['PATH'] += ';' + location[:-10] + 'Lib\site-packages\PyQt5\Qt\bin'
os.environ['PATH'] += ';' + os.path.abspath(__file__)

from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from interface import Ui_MainWindow

import mss
import mss.tools
import numpy
import pyautogui
import PyQt5_stylesheets
import configparser
import vk_api
import random

vk_session = vk_api.VkApi(token = '4256d7432db5a9a66a936f4c4c478928260afc0e1d653ae37e29d6218571b0e3a434793128b75593555ad')

programm = True
game_accepted = 0
path = "settings.ini"

def createConfig(path):
	config = configparser.ConfigParser()
	config.add_section("Settings")
	config.set("Settings", "sensetivity", "0")
	config.set("Settings", "user_id", "0")
		
	with open(path, "w") as config_file:
		config.write(config_file)
		
def crudConfig(path):
	
	if not os.path.exists(path):
		createConfig(path)

class mywindow(QtWidgets.QMainWindow):

	global path,user_id
	
	def __init__(self):
		
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.ui.Start_button.clicked.connect(self.start_clicked)
		self.ui.Pause_button.clicked.connect(self.pause_clicked)
		self.ui.Save_button.clicked.connect(self.save_clicked)
	
	def start_clicked(self):
		
		config = configparser.ConfigParser()
		config.read(path)
		
		sensetivity = int(config.get("Settings", "sensetivity"))
		user_id = int(config.get("Settings", "user_id"))
	
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
	
			crudConfig(path)
			
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
				global vk_session
				if user_id != 0:
					vk = vk_session.get_api()
					rand = random.getrandbits(31) * random.choice([-1, 1])
					notice_text = "ИГРА НАЙДЕНА! Пожалуйста проследуйте к игровому пространству!"
					vk.messages.send(user_id = user_id, random_id = rand, message = notice_text)
				break

			elif game_accepted == 2:
				break

	def pause_clicked(self):

		global game_accepted
		game_accepted = 2

		self.statusBar().showMessage('Программа приостановленна')

	def save_clicked(self):

		global sensetivity, user_id
		
		sensetivity = self.ui.sensetivity_edit.text()
		user_id = int(self.ui.vk_id.text())
		
		crudConfig(path)
		
		config = configparser.ConfigParser()
		config.read(path)
		
		config.set("Settings", "user_id", str(user_id))
		config.set("Settings", "sensetivity", str(sensetivity))
		
		with open(path, "w") as config_file:
			config.write(config_file)
			
		print("Чувствительность алгоритма = %s" % sensetivity)
		print("ID пользователя ВКонтакте установлен: %s" % user_id)

app = QtWidgets.QApplication(sys.argv)
application = mywindow()
app.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_Dark"))
application.show()

sys.exit(app.exec())
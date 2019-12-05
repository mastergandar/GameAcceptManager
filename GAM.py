#from multiprocessing import Process, Queue
from PIL import Image

import mss
import mss.tools
import numpy
import sys
import pyautogui

programm = True

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
	
	if similarity < 4000000:
		print("ИГРА НАЙДЕНА")
		global game_accepted
		game_accepted = 1
		pyautogui.moveTo (956, 520)
		pyautogui.click(button = 'left')
	
while programm == True:
	if game_accepted == 0:
		grab()
		find(game_accepted)
	if game_accepted == 1:
		waiting = str(input("Введите любой текст и нажмите 'Enter' для продолжения работы программы"))
		game_accepted = 0

	'''queue = Queue()
	Process(target=grab, args=(queue,state)).start()
	Process(target=find, args=(queue,state)).start()'''
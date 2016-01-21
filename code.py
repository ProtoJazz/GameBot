import ImageGrab
import os
import time
import win32api, win32con
import ImageOps
from numpy import *
# Globals
# ------------------
class Blank:
	seat_1 = 8119
	seat_2 = 5986
	seat_3 = 11841
	seat_4 = 10532
	seat_5 = 6597
	seat_6 = 9119
x_pad = 464
y_pad = 220
foodOnHand = {'shrimp':5,
			  'rice':10,
			  'nori':10,
			  'roe':10,
			  'salmon':5,
			  'unagi':5}
sushiTypes = {2670:'onigiri', 
			  3143:'caliroll',
			  2677:'gunkan',}
def screenGrab():
	box = (x_pad+1,y_pad+1,x_pad + 640,y_pad + 482)
	im = ImageGrab.grab(box)
	##im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
	##'.png', 'PNG')
	return im

def grab():
	box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+480)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	return a

def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	print "Click."          #completely optional. But nice for debugging purposes.	

def leftDown():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	print 'left Down'
def leftUp():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	time.sleep(.1)
	print 'left release'

def mousePos(cord):
	win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
	x,y = win32api.GetCursorPos()
	x = x - x_pad
	y = y - y_pad
	print x,y

def startGame():
	#location of first menu
	mousePos((310, 199))
	leftClick()
	time.sleep(.1)
	 
	#location of second menu
	mousePos((321, 392))
	leftClick()
	time.sleep(.1)
	 
	#location of third menu
	mousePos((583, 456))
	leftClick()
	time.sleep(.1)
	 
	#location of fourth menu
	mousePos((321, 378))
	leftClick()
	time.sleep(.1)

def clear_tables():
	mousePos((94, 202))
	leftClick()
 
	mousePos((200, 212))
	leftClick()
 
	mousePos((292, 206))
	leftClick()
 
	mousePos((389, 205))
	leftClick()
 
	mousePos((484, 207))
	leftClick()
 
	mousePos((594, 213))
	leftClick()
	time.sleep(1)

def get_seat_one():
	box = (x_pad +26,y_pad +63,x_pad +26+63,y_pad +63+16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
	return a
 
def get_seat_two():
	box = (x_pad +127,y_pad +63,x_pad +127+63,y_pad +63+16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
	return a
 
def get_seat_three():
	box = (x_pad +228,y_pad +63,x_pad +228+63,y_pad +63+16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
	return a
 
def get_seat_four():
	box = (x_pad +329,y_pad +63,x_pad +329+63,y_pad +63+16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
	return a
 
def get_seat_five():
	box = (x_pad +430,y_pad +63,x_pad +430+63,y_pad +63+16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
	return a
 
def get_seat_six():
	box = (x_pad +531,y_pad +63,x_pad +531+63,y_pad +63+16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
	return a
 
def get_all_seats():
	get_seat_one()
	get_seat_two()
	get_seat_three()
	get_seat_four()
	get_seat_five()
	get_seat_six()

def makeFood(food):
	if food == 'caliroll':
		print 'Making a caliroll'
		foodOnHand['rice'] -= 1
		foodOnHand['nori'] -= 1
		foodOnHand['roe'] -= 1 
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.1)
		foldMat()
		time.sleep(1.5)
	 
	elif food == 'onigiri':
		print 'Making a onigiri'
		foodOnHand['rice'] -= 2 
		foodOnHand['nori'] -= 1 
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.1)
		foldMat()
		time.sleep(.05)
		 
		time.sleep(1.5)
 
	elif food == 'gunkan':
		print 'Makeing a gunkan'
		foodOnHand['rice'] -= 1 
		foodOnHand['nori'] -= 1 
		foodOnHand['roe'] -= 2 
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.1)
		foldMat()
		time.sleep(1.5)
def foldMat():
	mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) 
	leftClick()
	time.sleep(.1)

def buyFood(food):
	if food == 'rice':
		mousePos(Cord.phone)
		time.sleep(.1)
		leftClick()
		mousePos(Cord.menu_rice)
		time.sleep(.05)
		leftClick()
		s = screenGrab()
		if s.getpixel(Cord.buy_rice) != (127, 127, 127):
			print 'rice is available'
			mousePos(Cord.buy_rice)
			time.sleep(.1)
			leftClick()
			mousePos(Cord.delivery_norm)
			foodOnHand['rice'] += 10
			time.sleep(.1)
			leftClick()
			time.sleep(2.5)
		else:
			print 'rice is NOT available'
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)
			 
 
			 
	if food == 'nori':
		mousePos(Cord.phone)
		time.sleep(.1)
		leftClick()
		mousePos(Cord.menu_toppings)
		time.sleep(.05)
		leftClick()
		s = screenGrab()
		print 'test'
		time.sleep(.1)
		if s.getpixel(Cord.t_nori) != (33, 30, 11):
			print 'nori is available'
			mousePos(Cord.t_nori)
			time.sleep(.1)
			leftClick()
			mousePos(Cord.delivery_norm)
			foodOnHand['nori'] += 10
			time.sleep(.1)
			leftClick()
			time.sleep(2.5)
		else:
			print 'nori is NOT available'
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)
 
	if food == 'roe':
		mousePos(Cord.phone)
		time.sleep(.1)
		leftClick()
		mousePos(Cord.menu_toppings)
		foodOnHand['roe'] += 10
		time.sleep(.05)
		leftClick()
		s = screenGrab()
		 
		time.sleep(.1)
		if s.getpixel(Cord.t_roe) != (127, 61, 0):
			print 'roe is available'
			mousePos(Cord.t_roe)
			time.sleep(.1)
			leftClick()
			mousePos(Cord.delivery_norm)
			time.sleep(.1)
			leftClick()
			time.sleep(2.5)
		else:
			print 'roe is NOT available'
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)

	"""
	mousePos(Cord.t_shrimp)

	mousePos(Cord.t_salmon)
	mousePos(Cord.t_unagi)
	mousePos(Cord.t_exit)
	 
	 
	mousePos(Cord.delivery_norm)
"""

def check_bubs():
 
	checkFood()
	s1 = get_seat_one()
	if s1 != Blank.seat_1:
		if sushiTypes.has_key(s1):
			print 'table 1 is occupied and needs %s' % sushiTypes[s1]
			makeFood(sushiTypes[s1])
		else:
			print 'sushi not found!\n sushiType = %i' % s1
 
	else:
		print 'Table 1 unoccupied'
 
	clear_tables()
	checkFood()
	s2 = get_seat_two()
	if s2 != Blank.seat_2:
		if sushiTypes.has_key(s2):
			print 'table 2 is occupied and needs %s' % sushiTypes[s2]
			makeFood(sushiTypes[s2])
		else:
			print 'sushi not found!\n sushiType = %i' % s2
 
	else:
		print 'Table 2 unoccupied'
 
	checkFood()
	s3 = get_seat_three()
	if s3 != Blank.seat_3:
		if sushiTypes.has_key(s3):
			print 'table 3 is occupied and needs %s' % sushiTypes[s3]
			makeFood(sushiTypes[s3])
		else:
			print 'sushi not found!\n sushiType = %i' % s3
 
	else:
		print 'Table 3 unoccupied'
 
	checkFood()
	s4 = get_seat_four()
	if s4 != Blank.seat_4:
		if sushiTypes.has_key(s4):
			print 'table 4 is occupied and needs %s' % sushiTypes[s4]
			makeFood(sushiTypes[s4])
		else:
			print 'sushi not found!\n sushiType = %i' % s4
 
	else:
		print 'Table 4 unoccupied'
 
	clear_tables()
	checkFood()
	s5 = get_seat_five()
	if s5 != Blank.seat_5:
		if sushiTypes.has_key(s5):
			print 'table 5 is occupied and needs %s' % sushiTypes[s5]
			makeFood(sushiTypes[s5])
		else:
			print 'sushi not found!\n sushiType = %i' % s5
 
	else:
		print 'Table 5 unoccupied'
 
	checkFood()
	s6 = get_seat_six()
	if s6 != Blank.seat_6:
		if sushiTypes.has_key(s6):
			print 'table 1 is occupied and needs %s' % sushiTypes[s6]
			makeFood(sushiTypes[s6])
		else:
			print 'sushi not found!\n sushiType = %i' % s6
 
	else:
		print 'Table 6 unoccupied'
 
	clear_tables()

def checkFood():
	for i, j in foodOnHand.items():
		if i == 'nori' or i == 'rice' or i == 'roe':
			if j <= 4:
				print '%s is low and needs to be replenished' % i
				buyFood(i)

def main():
	startGame()
	while True:
		check_bubs()

if __name__ == '__main__':
	main()


class Cord:
	 
	f_shrimp = (31, 331)
	f_rice = (94, 332)
	f_nori = (34, 392)
	f_roe = (93, 391)
	f_salmon = (46, 442)
	f_unagi = (93, 446)
	
	phone = (583, 352)
 
	menu_toppings = (578, 273)
	 
	t_shrimp = (498, 221)
	t_nori = (491,281)
	t_roe = (577, 277)
	t_salmon = (492, 335)
	t_unagi = (572, 227)
	t_exit = (592, 336)
 
	menu_rice = (558, 294)
	buy_rice = (545, 278)
	 
	delivery_norm = (492, 295)



	"""
	Plate cords:

		94 202
		200 212
		292 206
		389 205
		484 207
		594 213

	"""

	"""
	Recipes:
 
	onigiri
		2 rice, 1 nori
	 
	caliroll:
		1 rice, 1 nori, 1 roe
		 
	gunkan:
		1 rice, 1 nori, 2 roe
"""
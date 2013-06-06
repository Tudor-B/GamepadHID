#!/usr/bin/python

import os
import pygame
import gui
#import sys		# Imports pygame library that are made for developing games
if os.name == 'nt':
	from WinMouseInterface import MouseInterface
	from WinKBInterface import KBInterface
	pass
elif os.name == 'posix':
	from linterface import Interface
	pass
from remapper import remapper

pygame.init()			# Starts pygame
t = pygame.time.Clock()		# Make a tracker
interface = Interface()
os.system('cls' if os.name=='nt' else 'clear') # Clear terminal // remove "there is no soundcard"
try: 
	
	print "Number of Devices:", pygame.joystick.get_count()
	d = pygame.joystick.Joystick(0)
	d.init()			# Start pygame.joystick.Joystick(0)
	rem = remapper(d.get_name())
	maingui = gui.gui(rem)

# Gives info about the device
	print "Connected device", d.get_name()
	print d.get_name(), "have"
	print "Buttons:", d.get_numbuttons()
	print "Axes:", d.get_numaxes()
	print "Hats:", d.get_numhats()
	print "Balls:", d.get_numballs()
	print "The device ID is", d.get_id()
	print "Press button 0 to exit"
	
# Start showing the info in terminal

	def loop():
		global d, t

		while pygame.event.get(pygame.QUIT) == []:
			xy =pygame.event.get(pygame.JOYAXISMOTION) #if this isnt here you cant press buttons?!
			#xy_True=[] # call the infomation to
		# Axes Part
			
# 			xy_data = []
# 			for c in range(0, d.get_numaxes()):						#Mouse Movement
# 				xy_data+= [d.get_axis(c)]
# 			print "axis 1"
# 			print xy_data[0]*20
# 			print "axis 2"
# 			print xy_data[1]*20
			#mouse.SetRelPos(int(float(xy_data[0])), int(float(xy_data[1])))
			interface.SetRelPos(int(d.get_axis(0)*20), int(d.get_axis(1)*20))
			# Button Part Down
			downbutton = pygame.event.get(pygame.JOYBUTTONDOWN)
			for button in downbutton:
				print "Pressed button is", button.button
				if button.button == rem.buttons['start']:			# The exit button
					return
				elif button.button == rem.buttons['select']:
					maingui.Menu()
				elif button.button == rem.buttons['up']:
					interface.genEvent(rem.actions['up'], 'down')
				elif button.button == rem.buttons['right']:
					interface.genEvent(rem.actions['right'], 'down')
				elif button.button == rem.buttons['down']:
					interface.genEvent(rem.actions['down'], 'down')
				elif button.button == rem.buttons['left']:
					interface.genEvent(rem.actions['left'], 'down')
				elif button.button == rem.buttons['triangle']:
					interface.genEvent(rem.actions['triangle'], 'down')
				elif button.button == rem.buttons['square']:
					interface.genEvent(rem.actions['square'], 'down')
				elif button.button == rem.buttons['circle']:
					interface.genEvent(rem.actions['circle'], 'down')
				elif button.button == rem.buttons['cross']:
					interface.genEvent(rem.actions['cross'], 'down')
				elif button.button == rem.buttons['L1']:
					interface.genEvent(rem.actions['L1'], 'down')
				elif button.button == rem.buttons['L2']:
					interface.genEvent(rem.actions['L2'], 'down')
				elif button.button == rem.buttons['L3']:
					interface.genEvent(rem.actions['L3'], 'down')
				elif button.button == rem.buttons['R1']:
					interface.genEvent(rem.actions['R1'], 'down')
				elif button.button == rem.buttons['R2']:
					interface.genEvent(rem.actions['R2'], 'down')
				elif button.button == rem.buttons['R3']:
					interface.genEvent(rem.actions['R3'], 'down')
				#print (pygame.mouse.get_pos())
		
			# Button Part Up
			upbutton = pygame.event.get(pygame.JOYBUTTONUP)
			for button in upbutton:
				print "Button released was", button.button
				if button.button == rem.buttons['start']:			# The exit button
					return
				elif button.button == rem.buttons['select']:
					interface.genEvent(rem.actions['select'], 'up')
				elif button.button == rem.buttons['up']:
					interface.genEvent(rem.actions['up'], 'up')
				elif button.button == rem.buttons['right']:
					interface.genEvent(rem.actions['right'], 'up')
				elif button.button == rem.buttons['down']:
					interface.genEvent(rem.actions['down'], 'up')
				elif button.button == rem.buttons['left']:
					interface.genEvent(rem.actions['left'], 'up')
				elif button.button == rem.buttons['triangle']:
					interface.genEvent(rem.actions['triangle'], 'up')
				elif button.button == rem.buttons['square']:
					interface.genEvent(rem.actions['square'], 'up')
				elif button.button == rem.buttons['circle']:
					interface.genEvent(rem.actions['circle'], 'up')
				elif button.button == rem.buttons['cross']:
					interface.genEvent(rem.actions['cross'], 'up')
				elif button.button == rem.buttons['L1']:
					interface.genEvent(rem.actions['L1'], 'up')
				elif button.button == rem.buttons['L2']:
					interface.genEvent(rem.actions['L2'], 'up')
				elif button.button == rem.buttons['L3']:
					interface.genEvent(rem.actions['L3'], 'up')
				elif button.button == rem.buttons['R1']:
					interface.genEvent(rem.actions['R1'], 'up')
				elif button.button == rem.buttons['R2']:
					interface.genEvent(rem.actions['R2'], 'up')
				elif button.button == rem.buttons['R3']:
					interface.genEvent(rem.actions['R3'], 'up')
			t.tick(80)
	loop()

except Exception, e:
	print "Unhandled exception: %s"%e
	print "Shutting down now"
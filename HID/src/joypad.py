#!/usr/bin/python
# Project Network - Logitech G27 / Xbox 360 controller and others

import os
import pygame 
#import win32api
#import win32con 
import sys		# Imports pygame library that are made for developing games
from MouseInterface import MouseInterface

value = 10
pygame.init()			# Starts pygame
t = pygame.time.Clock()		# Make a tracker

mouse = MouseInterface()

# TODO: change the default value to something dynamic
x=768
y=384 
os.system('cls' if os.name=='nt' else 'clear')# Clear terminal // remove "there is no soundcard"
try: 
	
	print "Number of Devices:", pygame.joystick.get_count()
	d = pygame.joystick.Joystick(0)
	d.init()			# Start pygame.joystick.Joystick(0)
	c = pygame.mouse

# Gives info about the device
	print "Connected device", d.get_name()
	print d.get_name(), "have"
	print "Buttons:", d.get_numbuttons()
	print "Axes:", d.get_numaxes()
	print "Hats:", d.get_numhats()
	print "Balls:", d.get_numballs()
	print "Current cursor position:", c.get_pos()
	print "The device ID is", d.get_id()
	print "Press button 0 to exit"
	
# Start showing the info in terminal
		
# 	def Lclick(x, y):
# 		
# 		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x, y)
# 		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x, y)
# 		
# 	def Rclick(x, y):
# 		
# 		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x, y)
# 		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x, y)
		
	def loop():
		global d, t, x, y

		while pygame.event.get(pygame.QUIT) == []:
			xy =pygame.event.get(pygame.JOYAXISMOTION)
			#xy_True=[] # call the infomation to
		# Axes Part
			if xy != []:
				xy_data = []
				for c in range(0, d.get_numaxes()):
					xy_data+= [str(round(d.get_axis(c),1))]
					x = x + int(float(xy_data[0]))
					print x
					#xy_True+= [int(xy_data)]
#     					if xy_data[0] == "1.0":
#     						x=x+1
#     					if xy_data[0] == "-1.0":
#     						x=x-1
					#if xy_data[1] == "1.0":
					#	y=y+1
					#if xy_data[1] == "-1.0":
					#	y=y-1
				
				mouse.SetPosition( x, y )
# 				win32api.SetCursorPos((x, y))
				print "Works?"
				print xy_data
				
				#print radar
			
			# Button Part Down
			downbutton = pygame.event.get(pygame.JOYBUTTONDOWN)
			for button in downbutton:
				print "Pressed button is", button.button
				if button.button == 0:			# The exit button
					return
				elif button.button == 2:
					mouse.ClickLeft()
				elif button.button == 3:
					mouse.ClickRight()
			
				print (pygame.mouse.get_pos())
		
		# Button Part Up
			upbutton = pygame.event.get(pygame.JOYBUTTONUP)
			for button in upbutton:
				print "Button released was", button.button
			t.tick(80)
	loop()

except Exception, e:
	print "Unhandled exception: %s"%e
	print "Shutting down now"

#Nicklas Jensen

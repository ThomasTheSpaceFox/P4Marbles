#!/usr/bin/env python
import pygame.event
import pygame.key
import pygame.display
import pygame.image
import pygame.mixer
import pygame
from pygame.locals import *
import time
import os
import array
import math
import copy
import random
from threading import Thread

pygame.font.init()


class cellx:
	def __init__(self, screensurf, powx, xpos, ypos, size=120, textsize=22, label="", cellcolor=(255, 255, 255)):
		self.cellfont = pygame.font.SysFont(None, textsize)
		self.screensurf=screensurf
		self.powx=powx
		self.xpos=xpos
		self.ypos=ypos
		#cell rectangle
		self.cellrect=pygame.Rect(xpos, ypos, size, size)
		#marble spacing
		self.size=size
		self.mars=size//4
		self.label=label
		self.cellcolor=cellcolor
		self.marcolor=(20, 180, 20)
		self.marw=self.mars//2
		self.xcenter=self.xpos+(self.size//2)
		#figure out marble positions
		self.mar1=(self.xpos+(self.mars*1), self.ypos+(self.mars*2))
		self.mar2=(self.xpos+(self.mars*1), self.ypos+(self.mars*3))
		self.mar3=(self.xpos+(self.mars*2), self.ypos+(self.mars*2))
		self.mar4=(self.xpos+(self.mars*2), self.ypos+(self.mars*3))
		self.mar5=(self.xpos+(self.mars*3), self.ypos+(self.mars*2))
		self.mar6=(self.xpos+(self.mars*3), self.ypos+(self.mars*3))
		self.count=0
	def get_value(self):
		return self.count*(4**self.powx)
	def render(self):
		labx=self.cellfont.render(self.label + " " + str(self.count) + " (" + str(self.count*(4**self.powx)) + ")", True, (0, 0, 0), self.cellcolor)
		
		pygame.draw.rect(self.screensurf, self.cellcolor, self.cellrect, 0)
		pygame.draw.rect(self.screensurf, (0, 0, 0), self.cellrect, 1)
		self.screensurf.blit(labx, (self.xcenter-(labx.get_width()//2), self.ypos+2))
		#draw marbles
		if self.count>=1:
			pygame.draw.circle(self.screensurf, self.marcolor, self.mar1, self.marw)
			pygame.draw.circle(self.screensurf, (0, 0, 0), self.mar1, self.marw, 1)
		if self.count>=2:
			pygame.draw.circle(self.screensurf, self.marcolor, self.mar2, self.marw)
			pygame.draw.circle(self.screensurf, (0, 0, 0), self.mar2, self.marw, 1)
		if self.count>=3:
			pygame.draw.circle(self.screensurf, self.marcolor, self.mar3, self.marw)
			pygame.draw.circle(self.screensurf, (0, 0, 0), self.mar3, self.marw, 1)
		if self.count>=4:
			pygame.draw.circle(self.screensurf, self.marcolor, self.mar4, self.marw)
			pygame.draw.circle(self.screensurf, (0, 0, 0), self.mar4, self.marw, 1)
		if self.count>=5:
			pygame.draw.circle(self.screensurf, self.marcolor, self.mar5, self.marw)
			pygame.draw.circle(self.screensurf, (0, 0, 0), self.mar5, self.marw, 1)
		if self.count>=6:
			pygame.draw.circle(self.screensurf, self.marcolor, self.mar6, self.marw)
			pygame.draw.circle(self.screensurf, (0, 0, 0), self.mar6, self.marw, 1)
	def click(self, event):
		if self.cellrect.collidepoint(event.pos):
			if event.button==1 or event.button==4:
				self.count+=1
				if self.count==7:
					self.count=0
			elif event.button==5 or event.button==3:
				self.count-=1
				if self.count==-1:
					self.count=6
		
	
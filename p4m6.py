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
from p4mlib import cellx

pygame.display.init()
pygame.font.init()

screensurf=pygame.display.set_mode((620, 620))
pygame.display.set_caption("P4Marbles: a powers of 4 marble counting table simulator (6 row)", "P4Marbles: a powers of 4 marble counting table simulator (6 row)")

#column cell object init.
#column1
col1=[cellx(screensurf, 5, 20, 20, label="zeta", size=100),
cellx(screensurf, 4, 20, 120, label="epsilon", size=100),
cellx(screensurf, 3, 20, 220, label="delta", size=100),
cellx(screensurf, 2, 20, 320, label="gamma", size=100),
cellx(screensurf, 1, 20, 420, label="beta", size=100),
cellx(screensurf, 0, 20, 520, label="alpha", size=100)]

col2=[cellx(screensurf, 5, 200, 20, label="zeta", size=100),
cellx(screensurf, 4, 200, 120, label="epsilon", size=100),
cellx(screensurf, 3, 200, 220, label="delta", size=100),
cellx(screensurf, 2, 200, 320, label="gamma", size=100),
cellx(screensurf, 1, 200, 420, label="beta", size=100),
cellx(screensurf, 0, 200, 520, label="alpha", size=100)]

col3=[cellx(screensurf, 5, 420, 20, label="zeta", size=100),
cellx(screensurf, 4, 420, 120, label="epsilon", size=100),
cellx(screensurf, 3, 420, 220, label="delta", size=100),
cellx(screensurf, 2, 420, 320, label="gamma", size=100),
cellx(screensurf, 1, 420, 420, label="beta", size=100),
cellx(screensurf, 0, 420, 520, label="alpha", size=100)]
labelfont = pygame.font.SysFont(None, 26)
#greater/less/equal labels
c12g=labelfont.render("c1>c2", True, (0, 0, 0), (255, 255, 255))
c12l=labelfont.render("c1<c2", True, (0, 0, 0), (255, 255, 255))
c12e=labelfont.render("c1==c2", True, (0, 0, 0), (255, 255, 255))

c23g=labelfont.render("c2>c3", True, (0, 0, 0), (255, 255, 255))
c23l=labelfont.render("c2<c3", True, (0, 0, 0), (255, 255, 255))
c23e=labelfont.render("c2==c3", True, (0, 0, 0), (255, 255, 255))

c31g=labelfont.render("c3>c1", True, (0, 0, 0), (255, 255, 255))
c31l=labelfont.render("c3<c1", True, (0, 0, 0), (255, 255, 255))
c31e=labelfont.render("c3==c1", True, (0, 0, 0), (255, 255, 255))
run=1
while run:
	#combined tally/render loops
	screensurf.fill((200, 200, 250))
	#column1
	count1=0
	for f in col1:
		f.render()
		count1+=f.get_value()
	screensurf.blit(labelfont.render("Column 1: " + str(count1), True, (0, 0, 0), (255, 255, 255)), (0, 0))
	#column2
	count2=0
	for f in col2:
		f.render()
		count2+=f.get_value()
	screensurf.blit(labelfont.render("Column 2: " + str(count2), True, (0, 0, 0), (255, 255, 255)), (200, 0))
	#column3
	count3=0
	for f in col3:
		f.render()
		count3+=f.get_value()
	screensurf.blit(labelfont.render("Column 3: " + str(count3), True, (0, 0, 0), (255, 255, 255)), (400, 0))
	
	#greater/less/equal comparisons
	#column 1 & 2
	if count1>count2:
		screensurf.blit(c12g, (125, 0))
	elif count1==count2:
		screensurf.blit(c12e, (125, 0))
	else:
		screensurf.blit(c12l, (125, 0))
	#column 2 & 3
	if count2>count3:
		screensurf.blit(c23g, (325, 0))
	elif count2==count3:
		screensurf.blit(c23e, (325, 0))
	else:
		screensurf.blit(c23l, (325, 0))
	#column 3 & 1
	if count3>count1:
		screensurf.blit(c31g, (525, 0))
	elif count3==count1:
		screensurf.blit(c31e, (525, 0))
	else:
		screensurf.blit(c31l, (525, 0))
	#print(count)
	time.sleep(0.1)
	pygame.display.update()
	for event in pygame.event.get():
		if event.type==MOUSEBUTTONDOWN:
			#loop through each column upon click.
			for f in col1:
				f.click(event)
			for f in col2:
				f.click(event)
			for f in col3:
				f.click(event)
		if event.type==KEYDOWN:
			if event.key==K_ESCAPE:
				run=0
		if event.type==QUIT:
			run=0

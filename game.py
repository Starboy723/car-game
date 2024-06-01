import pygame
import random
import math
import time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((50,60))#gamewindow
height=60
#title and icon
title='car game'
clock=pygame.time.Clock()
#images
bg=pygame.image.load('road.jpg')
obg=pygame.image.load('road.jpg')
b_pos=0
o_pos=60
speed=10
pimg=pygame.image.load('car.png')
pimg_rect=pimg.get_rect()
rkey=pygame.image.load("Rightkey.jpg")
lkey=pygame.image.load('Leftkey.jpg')
b1car=pygame.image.load('B1car.png')
b1car_rect=b1car.get_rect()
b2car=pygame.image.load('B2car.png')
b2car_rect=b2car.get_rect()
bcar=pygame.image.load('Bcar.png')
bcar_rect=bcar.get_rect()
ycar=pygame.image.load('Ycar.png')
ycar_rect=ycar.get_rect()
bg1=pygame.image.load('Bg1.jpg')
carslist=[]
carslist2=[]
b1car=pygame.transform.scale(b1car,(350,350))
carx=[]
cary=[]
b2car=pygame.transform.scale(b2car,(350,350))
bcar=pygame.transform.scale(bcar,(350,350))
ycar=pygame.transform.scale(ycar,(350,350))
pimg=pygame.transform.scale(pimg,(350,350))
rkey=pygame.transform.scale(rkey,(250,300))#image transformation
rect=rkey.get_rect()
lkey=pygame.transform.scale(lkey,(250,300))#image transformation
#score text
score_font=pygame.font.Font("font3.otf",80)
over_font=pygame.font.Font("font3.otf",120)
score_x=370
score_y=1930
score=0
px=370
pimg_rect.x=370
py=1500
pimg_rect.y=1500
carsx=[20,500,250,650]
pygame.mixer.music.load('Bgmusic.mp3')
pygame.mixer.music.play(-1)
#multiple cars
for i in range(5):
	carslist.append(b1car_rect)
	carslist2.append(b1car)
	carslist2.append(b2car)
	carslist2.append(bcar)
	carslist2.append(ycar)
	carslist.append(b2car_rect)
	carslist.append(bcar_rect)
	carslist.append(ycar_rect)
	carx.append(random.choice(carsx))
	carslist[i].x=carx[i]
	cary.append(random.randint(0,0))
	carslist[i].y=cary[i]

click=False
game_on=True
#your score
def yscore():
	your_score=over_font.render("YOUR SCORE" ,True,(0,0,0))
	screen.blit(your_score,(100,400))
	screen.blit(score_img1,(500,600))
#game over
def game_over(over_x,over_y):
	over_img=over_font.render("GAME OVER",True,(0,0,0))
	screen.blit(over_img,(over_x,over_y))
#score
def show_score(score_x,score_y):
	global score_img1
	score_img=score_font.render(f'SCORE',True,(0,0,0))
	score_img1=score_font.render(str(score),True,(0,0,0))
	screen.blit(score_img,(score_x,score_y))
	screen.blit(score_img1,(410,2050))
	
#cars
def carlist(x,y,i):
		screen.blit(carslist2[i],carslist[i])
		
#Button class
class Button:
	def _init_(self,img,scale,x,y):
		self.img=img
		self.scale=scale
		self.rect=self.img.get_rect()
		self.rect.x=x
		self.rect.y=y
		#self.click=False
	def draw(self,screen):
		screen.blit(self.img,self.rect)
		pos=pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0]:
				return True
			if not pygame.mouse.get_pressed()[0]:
				return False
			
rkey_btn=Button(rkey,(250,300),800,1900)#rkey object
lkey_btn=Button(lkey,(250,300),20,1900)#lkey object
#game loop
while game_on:
		clock.tick(560)
		screen.fill((25,255,28))
		score+=1
		#road scrolling
		if b_pos>=height:
			b_pos=-height
		if o_pos>=height:
			o_pos=-height
		b_pos+=speed
		o_pos+=speed
		screen.blit(bg,(17,b_pos))
		screen.blit(obg,(17,o_pos))
		#cars loop
		for i in range(3):
			carlist(carslist[i].x,carslist[i].y,i)
			if carslist[i].y>1900:
				random.shuffle(carslist2)
				carslist[i].x=random.choice(carsx)
				carslist[i].y=-200
				carlist(carslist[i].x,carslist[i].y,i)
			if score>500:
				carslist[i].y+=30
			elif score>1000:
				carslist[i].y+=40
			elif score>1500:
				carslist[i].y+=50
			elif score>2000:
				carslist[i].y+=70
			else:
				carslist[i].y+=20
			if carslist[i].collidepoint(pimg_rect.x+118,pimg_rect.y) or pimg_rect.collidepoint(carslist[i].x+118,carslist[i].y):
				yscore()	
				game_over(130,1000)
				game_on=False
		screen.blit(bg1,(10,1860))
		screen.blit(pimg,pimg_rect)
		show_score(score_x,score_y)

		pygame.draw.rect(screen,(255,0,0),(300,1900,470,300),10)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				game_on=False
		rclick=rkey_btn.draw(screen)#rbutton
		if rclick:
					pimg_rect.x+=15
					if pimg_rect.x>=700:
						pimg_rect.x=700
		lclick=lkey_btn.draw(screen)#lbutton
		if lclick:
					pimg_rect.x+=-15
					if pimg_rect.x<=45:
						pimg_rect.x=45
		pygame.display.update()
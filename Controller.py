# File: Controller.py

import viz
from Ball import *

# Controller class inherits event handling methods from viz.EventClass
class Controller(viz.EventClass):
	
	def __init__(self):
		
		# must call constructor of EventClass first!!
		viz.EventClass.__init__(self)
		self.balls = list()
		self.timer = False
		#self.ball = Ball()
		self.callback(viz.TIMER_EVENT,self.onTimer)
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown)
		
	def onTimer(self,num):
		#print("Timer " + str(num))
		for ball in self.balls:
			if (ball.getY() + ball.radius >= 100 or  ball.getY() - ball.radius <= -100):
				print("X Axis Wall")
				ball.setVXVY(ball.getVX(), -ball.getVY())
				viz.playSound("cartoon053.wav", viz.PLAY)
			if(ball.getX() + ball.radius >= 100) or (ball.getX() - ball.radius <= -100):
				print("Y Axis Wall")
				ball.setVXVY(-ball.getVX(), ball.getVY())
				viz.playSound("cartoon053.wav", viz.PLAY)
			ball.setXY(ball.getVX() + ball.getX(), ball.getVY() + ball.getY())
		#print("X: "+ str(self.ball.getX()))
		#print("Y: "+ str(self.ball.getY()))
		
	def onKeyDown(self, key):
			if(key == " "):
				self.balls.append(Ball())
				
				if not self.timer:
					self.starttimer(1, 1/25, viz.FOREVER)
					self.timer = True
					
			if key == viz.KEY_DOWN:
				for ball in self.balls:
					ball.setVXVY(ball.getVX() * .95, ball.getVY()*.95)
			if key == viz.KEY_UP:
				for ball in self.balls:
					ball.setVXVY(ball.getVX() * 1.05, ball.getVY()*1.05)
	
	
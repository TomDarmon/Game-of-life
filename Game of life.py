from scene import *
import numpy as np
from GoL import *


A = np.array([ 	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
								[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
								[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
								[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
								[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],])
								
								
n = 200
C = np.zeros((n, n), dtype = int)
C.ravel()[:: n + 1] = 1
C.ravel()[n - 1 :: n - 1] = 1	


#C = np.random.rand(100, 100) < 0.2



class Circle:
	
	def __init__(self, x, y, size):
		self.x = x
		self.y = y
		self.size = size
		
		
	def display(self, color = 'black'):
		fill(color)
		stroke_weight(1)
		ellipse(self.x, self.y, self.size, self.size)
		no_fill()
		no_stroke()


def fill_with_circles(board, screen_size):
	rows = board.shape[0]
	cols = board.shape[1]
	screen_size_x = screen_size[1]
	
	circle_size = screen_size_x // (rows)  
	
	circles = []
	
	for i in range(rows):
		for j in range(cols):
			#circles.append(Circle(i * circle_size, j * circle_size, circle_size))
			circles.append(Circle(i * circle_size, (cols - j - 1) * circle_size, circle_size))		
	return circles
		

def display(circles, board):
	board = board.T
	board = board.flatten()
	
	for i, circle in enumerate(circles):
		if board[i] == 0:
			circle.display('black')
		if board[i] == 1:
			circle.display('white')
			
		

class MyScene(Scene):
	
	def setup(self):
		self.board = D
		self.circles = fill_with_circles(self.board, self.size)
		self.draw_grid = True
		
	def draw(self):
		if self.draw_grid == True:
			self.board = game_of_life(self.board, sleep = True)
			
		display(self.circles, self.board)
			
	def touch_began(self, touch):
		(x, y) = touch.location
		if (x > self.size[0] / 2):
			self.board = game_of_life(self.board, sleep = False)
		
			
		
run(MyScene())

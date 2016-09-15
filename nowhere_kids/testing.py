import pygame 
import time
import classes

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

UNIT = -1

size = [800,600]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")

loop = True
rectx = 100
recty = 100
rectspeedy = 0
rectspeedx = 0 

clock = pygame.time.Clock()
move = pygame.key.get_pressed()
rogue = classes.Rogue()
swordsman = classes.Swordsman()
knight = classes.Knight()
classes = [rogue,swordsman,knight]

font = pygame.font.Font(None,30)
instructions = font.render("press s, d, or f to choose your class...",True,BLACK)

class Grid():
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		
	### Edit ### moved drawing into this draw method 
	def draw(self):
		x = self.x
		y = self.y
		z = self.z
		for i in range(0, z):
			pygame.draw.line(screen, BLACK, [x, 0], [x, 600], 2)
			pygame.draw.line(screen, BLACK, [0, y], [800, y], 2)
			x += 25
			y += 25
	#############################################
			

map = Grid(25, 25, 33)
while loop == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				recty += 25
			if event.key == pygame.K_UP:
				recty -= 25
			if event.key == pygame.K_LEFT:
				rectx -= 25
			if event.key == pygame.K_RIGHT:
				rectx += 25
			if event.key == pygame.K_f:
				UNIT = 0
			if event.key == pygame.K_d:
				UNIT = 1
			if event.key == pygame.K_s:
				UNIT = 2
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				rectspeedy = 0
			if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
				rectspeedx = 0
	
	
	screen.fill(WHITE)
	if UNIT == 0 or UNIT == 1 or UNIT == 2:
		#pygame.draw.rect(screen, UNIT, [rectx, recty, 25, 25])
		classes[UNIT].draw(screen,rectx,recty)
		map.draw() ## Draw map
	else:
		screen.blit(instructions,[150,300])
	
	
	
	if rectx > size[0] - 25:
		rectx = size[0] - 25
	if recty > size[1] - 25:
		recty = size[1] - 25
	if rectx < 0:
		rectx = 0
	if recty < 0:
		recty = 0
	
	clock.tick(60)
	pygame.display.flip()
		
	
	
pygame.quit()
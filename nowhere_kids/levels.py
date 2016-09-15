import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (179, 255, 255)
COLORS = {
		"GREEN":GREEN,"RED":RED,
		"BLUE":BLUE,"BLACK":BLACK,
		"WHITE":WHITE, "CYAN":CYAN
		}

def draw_square(screen,x,y,color):
	## takes x y of first cyan 25x25 rectangle
	## draws two more rectangles 
	c = GREEN
	if (color.upper() in COLORS):
		c = COLORS[color.upper()]
	pygame.draw.rect(screen, c, [x, y, 25, 25])

def level_one(v,x,y):
	openspace = []
	for i in range(3):
		draw_square(v,x,y,"cyan")
		openspace.append([x,y])
		x+=150
		y+=0
	return openspace

def level_two(v,x,y):
	openspace = []
	for i in range(3):
		draw_square(v,x,y,"cyan")
		openspace.append([x,y])
		x+=150
		y-=50
	return openspace

def level_three(v,x,y):
	openspace = []

	draw_square(v,x,y,"cyan")
	openspace.append([x,y])

	x+=200
	y-=200
	draw_square(v,x,y,"cyan")
	openspace.append([x,y])
	
	x+=200
	y+=200
	draw_square(v,x,y,"cyan")
	openspace.append([x,y])
	return openspace

	
############## TESTING ###############
# pygame.init()
# size = [800, 500]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("I love my mistress")
# loop = True
# clock = pygame.time.Clock()

# while loop == True:
	
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			loop = False
	
# 	screen.fill(WHITE)
	
# 	level_one(screen,25,25)
	
# 	clock.tick(60)
	
# 	pygame.display.flip()
	
# pygame.quit()






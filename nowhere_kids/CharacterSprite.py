import pygame


class CharacterSprite (pygame.sprite.Sprite):

	def __init__(self, job, filetype):
		pygame.sprite.Sprite.__init__(self)
		self.folder = "images/sprites/"+job.lower()+"/"
		self.filetype = "."+filetype
		self.size = [10,10]
		self.image = {}
		self.load_image("standing0"+self.filetype)
		self.load_image("standing1"+self.filetype)
		#### Loading Complete ##### 
		####### Now for animation ########
		self.modes = ["standing","dodge","attack","critcal"]
		self.mode = 0
		self.frame_count = 0
		
	def load_image(self,filename):
		self.image[filename] = pygame.image.load(self.folder + filename).convert()
		self.image[filename].set_colorkey(BLACK)

	def draw(self, screen, x, y):
		mode = self.modes[self.mode]
		img_frame = str(self.frame_count // 30 % 2) + self.filetype
		self.frame_count += 1
		screen.blit(self.image[mode+img_frame], [x,y])
		if self.frame_count == 120:
			self.frame_count = 0

		## needs to be able to draw itself at some location

class RogueSprite (CharacterSprite):
	def __init__(self):
		CharacterSprite.__init__(self,"rogue","gif")

class SwordsmanSprite (CharacterSprite):
	def __init__(self):
		CharacterSprite.__init__(self,"swordsman","gif")

class KnightSprite (CharacterSprite):
	def __init__(self):
		CharacterSprite.__init__(self,"knight","gif")

import CharacterSprite



class Character():
	def __init__(self):
		self.sprite = CharacterSprite.RogueSprite() ## default
	def draw(self,screen,x,y):
		self.sprite.draw(screen, x,y)
################# Ally #########################

class Rogue(Character):
	def __init__(self):
		self.sprite = CharacterSprite.RogueSprite()
		self.attack = 7
		self.defense = 6
		self.movement = 7
		self.weapon = "purple"

class Swordsman(Character):
	def __init__(self):
		self.sprite = CharacterSprite.SwordsmanSprite()
		self.attack = 7
		self.defense = 10
		self.movement = 3
		self.weapon = "blue"

class Knight(Character):
	def __init__(self):
		self.sprite = CharacterSprite.KnightSprite()
		self.attack = 10
		self.defense = 5
		self.movement = 5
		self.weapon = "green"

#################################################

################# ENEMY #########################
class Ogre(Character):
	def __init__(self):
		self.attack = 12
		self.defense = 6
		self.movement = 2
		self.weapon = "red"

class Wolf(Character):
	def __init__(self):
		self.attack = 6
		self.defense = 6
		self.movement = 8
		self.weapon = "orange"
#################################################
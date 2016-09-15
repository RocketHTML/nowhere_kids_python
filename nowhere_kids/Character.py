# from Weapons import Weapon
import threading
import time


# ADVANCED_STATS = ["Crit", "Evasion"]
HP_LOCK = threading.Lock()

#######################################################################
############# WEAPON CLASS BEGIN ######################################
#######################################################################
class Weapon(threading.Thread):
	### Just an abstract class to be *inherited* from
	def __init__(self):
		threading.Thread.__init__(self)
		self.master = None
		self.is_rhand = False
		self.type = "Default"
		self.sibling = None
		self.strategy = None
		self.DISTRIBUTION = {
			"STR":.081, "DEF":.081, 
			"ACC":.081, "AGI":.081, 
			"INT":.081, 
			"HP":.541, "SP":.054
			}
		self.active = False

	def set_master(self, master, is_rhand=False):
		self.master = master
		self.is_rhand = is_rhand
		if(self.is_rhand):
			self.master.rhand = self
		else:
			self.master.lhand = self
		self.calculate_stats()
		self.activate()

	def calculate_stats(self):
		# first find proper distribution
			# average (mine and avg(mine and sibling))
				# or, simply mine 
		# then redistribute master's base stats 
			# multiple the sum of master's stats by the distribution 
		def average(dict1, dict2):
			result = dict1.copy()
			for key in dict1:
				result[key] = float((dict1[key]+dict2[key]))/2
			return result

		def redistribute(master_stats, distribution):
			result = master_stats.copy()
			total = 0
			for key in master_stats:
				total += master_stats[key]
			for key in master_stats:
				result[key] = total * distribution[key]
			return result

		## Now let's calculate the distribution 
		distribution = self.DISTRIBUTION
		if(self.sibling):
			distribution = average(distribution, 
						   average(distribution, self.sibling.DISTRIBUTION))
		## And now we redistribute master's stats 
		self.master.stats = redistribute(self.master.BASE_STATS, distribution)
	########## END OF CALCULATE_STATS FUNCTION #####################
	def activate(self):
		self.active = True
		if (self.sibling):
			self.sibling.active = True
	def deactivate(self):  # stops weapon from attacking 
		self.active = False
		if(self.sibling):
			self.sibling.active = False
		#lhand should become right hand 

	####### ONLY CALL ATTACK FROM RUN ########
	#### And only call run from character.engage #### 	
	def attack(self):
		## example of weapon basic attack
		## continues to loop until weapon is deactivated 
		while(self.active):
			time.sleep(450.0 / self.master.stats["AGI"])

			## attack an enemy
			for enemy in self.master.enemies:
				self.master.damage(enemy,1)

	def run(self):
		self.attack()

#######################################################################
############# CHARACTER CLASS BEGIN ###################################
#######################################################################
class Character():
	def __init__(self,name):
		self.name = name
		self.rhand = None
		self.lhand = None
		self.allies = []
		self.enemies = []
		self.BASE_STATS = {
			"STR":150, "DEF":150, 
			"ACC":150, "AGI":150, 
			"INT":150, 
			"HP":1000, "SP":100
			}
		self.stats = self.BASE_STATS.copy()
		## ^ until weapons are set  

	## Set Weapons and thus change stats 
	def set_rhand(self, rhand):
		rhand.set_master(self, True)
	def set_lhand(self,lhand):
		lhand.set_master(self, False)

	## How to set allies and enemies 
	def set_ally(self, character):
		self.allies.append(character)
	def set_enemy(self, character):
		self.enemies.append(character)

	## How to participate in battle
	def engage (self):
		# this function will activate your weapons 
		print self.name+": shit..."
		self.rhand.start()

	def damage (self, enemy, power):
		### power depends on the attack the weapon used 
		thisround = 0
		thisround += self.stats["STR"] * 2 * power 
		thisround -= enemy.stats["DEF"]
		## No critical rate calculation yet 
		## No evade rate calculation yet 
		### Agility will be relevant in weapon's code
		HP_LOCK.acquire()
		if(self.stats["HP"] > 0 and enemy.stats["HP"] > 0):
			enemy.stats["HP"] -= thisround
			print self.name +"("+str(self.stats["HP"])+") attacks "+\
					enemy.name+"("+str(enemy.stats["HP"])+")\n"
			if(enemy.stats["HP"] <= 0):
				print enemy.name +" has been slain..."
				self.rhand.deactivate()
		elif(self.stats["HP"] <= 0):
			self.rhand.deactivate()
		else:
			enemy.name +" is already dead..."
			self.rhand.deactivate()
		HP_LOCK.release()

### Test Code #####
##### The main program will be in its own file later ##### 
casey = Character("Casey")
brave = Weapon()
casey.set_rhand(brave)

rocket = Character("Rocket")
scythe = Weapon()
rocket.set_rhand(scythe)

badguy = Character("Jonny")
crimson = Weapon()
badguy.set_rhand(crimson)

casey.set_enemy(badguy)
casey.engage()
rocket.set_enemy(badguy)
rocket.engage()



from individual import INDIVIDUAL
import copy
import random

class POPULATION:
	def __init__(self, popSize):
		self.p = {}    # creates an empty population
		self.popSize = popSize  # stores the number of individuals in the population to be initialized
	def Initialize(self):
		for i in range(0, self.popSize): 
			self.p[i] = INDIVIDUAL(i)
	def Print(self):
		for i in self.p:
			if(i in self.p): # evaluates to True if there is an entry in the dictionary p with a key equal to i
				self.p[i].Print()
	def Evaluate(self, pb):
		for i in self.p: # this loop starts the evaluation of the individual
			self.p[i].Start_Evaluate(pb) # True activates 'play_blind' runs the robots without drawing
		for i in self.p: # this loop gives the fitness of each individual
			self.p[i].Compute_Fitness()
	def Mutate(self):
		for i in self.p:
			self.p[i].Mutate()
	def Replacewith(self, other):
		for i in self.p:
			if (self.p[i].fitness < other.p[i].fitness):
				self.p[i] = other.p[i]

	def Copy_Best_From(self, other): # copy the best individual in parents and place it into the first element of children
			self.fitnessvar = {}
			for i in other.p:
				self.fitnessvar[i] = other.p[i].fitness
			ID = max(xrange(len(self.fitnessvar)), key = lambda x: self.fitnessvar[x])
			max_value = max(self.fitnessvar)
			self.p[0] = copy.deepcopy(other.p[ID])
			del self.fitnessvar
	
	def Winner_Of_Tournament_Selection(other): # this method will select the best individual among the parents
		p1 = random.randint(0, len(other.p)-1) # randomly going to select the index of parents to compete with each other
		p2 = random.randint(0, len(other.p)-1)
		# make sure that p1 is different than p2
		while p1 == p2:
			p2 = random.randint(0, len(other.p)-1)
			p1 = random.randint(0, len(other.p)-1)
		if(other.p[p1] > other.p[p2]): # if the value on p1 is higher than the value on p2, then other.p[p1] won the tournament
			return other.p[p1]
		else:
			return other.p[p2]

	def Collect_Children_From(self, other): # simply fill the elements in children with other values of parents
		for i in range(1, len(other.p)):
			winner = other.Winner_Of_Tournament_Selection() #fill the elements of children with the best individuals of parents
			self.p[i] = copy.deepcopy(winner) # fill the elements just by copying the elements from parents
		 
	def Fill_From(self, other): # calls the methods in order to fill the elements of children
		self.Copy_Best_From(other)
		#self.Print()
		self.Collect_Children_From(other)
		#self.Print()



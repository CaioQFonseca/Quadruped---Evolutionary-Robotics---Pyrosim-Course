import random
import pyrosim
import math
import numpy as np

from robot import ROBOT


class INDIVIDUAL:
	def __init__(self, ID):

		self.genome = np.zeros((4,8)) # number of elements corresponds to the synapses weights
		for i in range(0, 4):
			for j in range(0,8):
				self.genome[i,j] = np.random.random()*2-1 # edit:code before had 4 inside the brackets/ because now it is 4 synapses, so 4 different weights
		self.fitness = 0
		self.ID = ID
	def Start_Evaluate(self, pb):
		self.sim = pyrosim.Simulator(play_paused = True, eval_time = 500, play_blind = pb)
		self.robot = ROBOT(self.sim, self.genome)
		self.sim.start() # self turn sim into a data structure stored inside of each class instance of INDIVIDUAL
	def Compute_Fitness(self):
		self.sim.wait_to_finish()
		x = self.sim.get_sensor_data(sensor_id = self.robot.P4, svi = 0)
		y = self.sim.get_sensor_data(sensor_id = self.robot.P4, svi = 1)
		z = self.sim.get_sensor_data(sensor_id = self.robot.P4, svi = 2)
		self.fitness = y[-1]
		del self.sim
	def Mutate(self):
		geneToMutaterow = random.randint(0,3) # will randomly choose which gene to mutate
		geneToMutatecol = random.randint(0,7)
		self.genome[geneToMutaterow, geneToMutatecol] = random.gauss(self.genome[geneToMutaterow, geneToMutatecol], math.fabs(self.genome[geneToMutaterow, geneToMutatecol]))
		
		if (self.genome[geneToMutaterow, geneToMutatecol] > 1):
			self.genome[geneToMutaterow, geneToMutatecol] = 1
		elif (self.genome[geneToMutaterow, geneToMutatecol] < -1):
			self.genome[geneToMutaterow, geneToMutatecol] = -1
		else:
			self.genome[geneToMutaterow, geneToMutatecol] = self.genome[geneToMutaterow, geneToMutatecol]
	
	def Print(self):
		print('['),
		print(self.ID),
		print(self.fitness),
		print('] '),
		print(''),



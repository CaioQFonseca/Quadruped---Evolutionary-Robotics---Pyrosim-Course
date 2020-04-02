import pyrosim
import matplotlib.pyplot as plt 
import random 
import numpy 
import copy
import pickle


from individual import INDIVIDUAL
from robot import ROBOT 
from population import POPULATION

parents = POPULATION(10) # creates a empty population but stores the population size
parents.Initialize()   #start a population of individuals of size 'i'
parents.Evaluate(True) # Evaluates the fitness of each individual
#exit() # exit the program immediately
parents.Print() #print ID and fitness of each individual


for i in range(1,200):
	children = POPULATION(5)
	#children.Print()
	children.Fill_From(parents)
	#children.Print()
	children.Evaluate(True)
	children.Print()
	parents = children

parents.Evaluate(False)
parents.Print()



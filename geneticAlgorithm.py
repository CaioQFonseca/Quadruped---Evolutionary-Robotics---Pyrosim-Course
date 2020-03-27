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


#children = copy.deepcopy(parents) # children copies all the data structure from parents
#children.Mutate()
#children.Evaluate(True)
#parents.Replacewith(children) # will compare the fitness of both the parents and children
# if children is better fitted than will replace parents
#parents.Print(), # print new fitness values

'''for i in range(1,200):
	children = copy.deepcopy(parents) # children copies all the data structure from parents
	children.Mutate()
	children.Evaluate(True)
	parents.Replacewith(children) # will compare the fitness of both the parents and children
	# if children is better fitted than will replace parents
	#print(i), #show each generation
	#parents.Print(), # prints the fitness and genome

parents.Evaluate(False)''' # shows the last & best fitted generation

'''parent = INDIVIDUAL()
parent.Evaluate(True) # True activates 'play_blind' not drawing the robot, False draws the robots
print(parent.fitness)

for i in range(0,100):
	child = copy.deepcopy( parent )
	child.Mutate()
	child.Evaluate(True)
	print('[g:' , i, ']' '[pw:', parent.genome, ']' '[p: ',  parent.fitness, ']','[c: ', child.fitness, ']')
	if ( child.fitness > parent.fitness):
		parent = child
		child.Evaluate(True)
		f = open('robot.p', 'w') #save individuals to a file and then load and then play them back in another program
		#opens a file that will be (w)ritten to, the second line dumps the 'parent' class instance into
		#that file, and the third line closes the file
		pickle.dump(parent, f)
		f.close()
#sensorData = sim.get_sensor_data(sensor_id = P2)
'''
'''f = plt.figure() 
panel = f.add_subplot(111) # adds a drawing panel inside the figure 
plt.plot(x)
plt.plot(y)
plt.plot(z)
#panel.set_ylim(-1, +2) # move the lower limit of the vertical axis down to y = -1 and the upper limit to y = +2
plt.show()'''


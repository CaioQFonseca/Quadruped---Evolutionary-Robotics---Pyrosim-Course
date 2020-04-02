import pyrosim
import constants as c 
import random 

class ROBOT:
	def __init__(self, sim, wts):
		self.send_objects(sim)
		self.send_joints(sim)
		self.send_sensors(sim)
		self.send_neurons(sim)
		self.send_synapses(sim,wts)

	def send_objects(self, sim):
		#self.whiteObject = sim.send_cylinder(x = 0, y = 0, z = 0.6, length = 1.0, radius = 0.1)
		#self.redObject = sim.send_cylinder(x = 0, y = 0.5, z = 1.1, r = 1, g = 0, b = 0, r1 = 0, r2 = 1, r3 = 0) # r1, r2, r3 represent the rotation vector of the cylinder
		self.O0 = sim.send_box(x = 0, y = 0, z=c.L + c.R, length =c.L, width =c.L, height=2*c.R, r=0.5, g=0.5, b=0.5)
		self.O1 = sim.send_cylinder(x = 0, y = 3*c.L/2, z = c.L/2+c.R, length = c.L, radius = c.R, r = 1, g = 0, b = 0)
		self.O2 = sim.send_cylinder(x = 0, y = c.L, z = c.L + c.R, length = c.L, radius = c.R, r = 1, g = 0, b = 0, r1 = 0, r2 = 1, r3 = 0)
		self.O3 = sim.send_cylinder(x = 3*c.L/2, y = 0, z = c.L/2+c.R, length = c.L, radius = c.R, r = 0, g = 0, b = 1)
		self.O4 = sim.send_cylinder(x = c.L, y = 0, z = c.L + c.R, length = c.L, radius = c.R, r = 0, g = 0, b = 1, r1 = 1, r2 = 0, r3 = 0)
		self.O5 = sim.send_cylinder(x = 0, y = -3*c.L/2, z = c.L/2+c.R, length = c.L, radius = c.R, r = 0, g = 1, b = 0)
		self.O6 = sim.send_cylinder(x = 0, y = -c.L, z = c.L + c.R, length = c.L, radius = c.R, r = 0, g = 1, b = 0, r1 = 0, r2 = 1, r3 = 0)
		self.O7 = sim.send_cylinder(x = -3*c.L/2, y = 0, z = c.L/2+c.R, length = c.L, radius = c.R, r = 1, g = 1, b = 0.5)
		self.O8 = sim.send_cylinder(x = -c.L, y = 0, z = c.L + c.R, length = c.L, radius = c.R, r = 1, g = 1, b = 0.5, r1 = 1, r2 = 0, r3 = 0)



	def send_joints(self, sim):
		#self.joint = sim.send_hinge_joint(first_body_id = self.whiteObject, second_body_id = self.redObject, x = 0, y = 0, z = 1.1, n1 = -1, n2 = 0, n3 = 0, lo = -3.14159/2, hi = 3.14159/2)
# n1, n2, n3 represents the normal vector of the plane for the joint rotation; and x,y,z the location of the joint;
# lo and hi represents the range of motion, in this case from -pi/2 to pi/2
		self.J0 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O2, x = 0, y = c.L/2, z = c.L+c.R, n1 = -1, n2 = 0, n3 = 0, lo = -3.14159/2, hi = 3.14159/2)	
		self.J1 = sim.send_hinge_joint(first_body_id = self.O1, second_body_id = self.O2, x = 0, y = 3*c.L/2, z = c.L+c.R, n1 = -1, n2 = 0, n3 = 0, lo = -3.14159/2, hi = 3.14159/2)
		self.J2 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O4, x = c.L/2, y = 0, z = c.L+c.R, n1 = 0, n2 = 1, n3 = 0, lo = -3.14159/2, hi = 3.14159/2)	
		self.J3 = sim.send_hinge_joint(first_body_id = self.O3, second_body_id = self.O4, x = 3*c.L/2, y = 0, z = c.L+c.R, n1 = 0, n2 = 1, n3 = 0, lo = -3.14159/2, hi = 3.14159/2)
		self.J4 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O6, x = 0, y = -c.L/2, z = c.L+c.R, n1 = 1, n2 = 0, n3 = 0, lo = -3.14159/2, hi = 3.14159/2)	
		self.J5 = sim.send_hinge_joint(first_body_id = self.O5, second_body_id = self.O6, x = 0, y = -3*c.L/2, z = c.L+c.R, n1 = 1, n2 = 0, n3 = 0, lo = -3.14159/2, hi = 3.14159/2)
		self.J6 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O8, x = -c.L/2, y = 0, z = c.L+c.R, n1 = 0, n2 = -1, n3 = 0, lo = -3.14159/2, hi = 3.14159/2)	
		self.J7 = sim.send_hinge_joint(first_body_id = self.O7, second_body_id = self.O8, x = -3*c.L/2, y = 0, z = c.L+c.R, n1 = 0, n2 = -1, n3 = 0, lo = -3.14159/2, hi = 3.14159/2)


	def send_sensors(self, sim):
		self.T0 = sim.send_touch_sensor(body_id = self.O1)
		self.T1 = sim.send_touch_sensor(body_id = self.O3)
		self.T2 = sim.send_touch_sensor(body_id = self.O5)
		self.T3 = sim.send_touch_sensor(body_id = self.O7)
		#self.P2 = sim.send_proprioceptive_sensor( joint_id = self.O0) # Proprioceptive sensor, connected to the joint instead of the object
		#self.R3 = sim.send_ray_sensor( body_id = self.redObject, x = 0, y = 1.1, z = 1.1, r1 = 0, r2 = 1, r3 = 0)
# R3: this sensor emits a ray outward from the object in which its embedded, and returns the length of that ray
# x,y,z indicates where the sensor should reside, in this case at the tip of the object
# r1,r2,r3 indicates where the sensor will point
		self.P4 = sim.send_position_sensor(body_id = self.O0)

	def send_neurons(self, sim):
		self.SN0 = sim.send_sensor_neuron( sensor_id = self.T0)
# SN0: Creates a sensor neuron which captures data arriving at, in this case, the first touch sensor
# if a number of neurons is created: each neuron adds together data arriving along its incoming
# connections, stores this sum internally and passes this value out along its outgoing connections 
		self.SN1 = sim.send_sensor_neuron( sensor_id = self.T1)
		self.SN2 = sim.send_sensor_neuron( sensor_id = self.T2)
		self.SN3 = sim.send_sensor_neuron( sensor_id = self.T3)
		self.SN = {} # dictionary to store the IDs of the four sensor neurons
		self.SN[0] = self.SN0
		self.SN[1] = self.SN1
		self.SN[2] = self.SN2
		self.SN[3]= self.SN3
		self.MN0 = sim.send_motor_neuron( joint_id = self.J1, tau = 0.3) # a motor neuron always attaches to a joint and passes its value along to it
		self.MN1 = sim.send_motor_neuron( joint_id = self.J2, tau = 0.3)
		self.MN2 = sim.send_motor_neuron( joint_id = self.J3, tau = 0.3)  
		self.MN3 = sim.send_motor_neuron( joint_id = self.J4, tau = 0.3) 
		self.MN4 = sim.send_motor_neuron( joint_id = self.J5, tau = 0.3) 
		self.MN5 = sim.send_motor_neuron( joint_id = self.J6, tau = 0.3) 
		self.MN6 = sim.send_motor_neuron( joint_id = self.J7, tau = 0.3) 

		self.MN = {}
		self.MN[0] = self.MN0
		self.MN[1] = self.MN1
		self.MN[2] = self.MN2
		self.MN[3] = self.MN3
		self.MN[4] = self.MN4
		self.MN[5] = self.MN5
		self.MN[6] = self.MN6


	def send_synapses(self, sim, wts):
		for s in self.SN:
			for j in self.MN:
			#firstMN = min(self.MN, key = self.MN.get) # gets the first motor neuron
				sim.send_synapse(source_neuron_id = self.SN[s], target_neuron_id = self.MN[j], weight = wts[s,j])
			


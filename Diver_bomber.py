from numpy import cos,sin,tan,sqrt,pi
from matplotlib import pyplot as plt

g = 9.81

'''
Stuff for drag
'''
def drag():
    pass

'''
Link for thrust of propeller : https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/thrust-equation
The diver bomber used a 3-bladed hamilton standard constant speed propeller


'''
flow_rate_density = 1.225 # kg/m^3 this can change
V_propeller = 0 # m/s this can change
Area_propeller = 38.5 # m^2
V_exit_propeller = 0 # m/s This can change
V_entrance = 0 # m/s this can change

def thrust():
    return flow_rate_density * V_propeller * Area_propeller *(V_exit_propeller - V_entrance)

'''
Stuff for Lift
'''   
def lift():
    pass

'''
Stuff for the force force of graphity 
'''
def graphity(m):
    return m * g


x_bomber_with_bomb = []
y_bomber_with_bomb = []

x_bomb = []
y_bomb = []

x_bomber = []
y_bomber =[]

x_ship = []
y_ship = []

angle_drop1 = 50
angle_drop2 = 60
angle_drop3 = 70
angle_drop4 = 80

while y_bomber_with_bomb[-1] > 457.2:  # Most SBD dropped around 1,500
    pass

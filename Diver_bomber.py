from numpy import cos,sin,tan,sqrt,pi
from matplotlib import pyplot as plt

g = 9.81

'''
Stuff for drag
'''
drag_coeffienct = 0
air_density = 0
cross_sectional_area =0

def drag(v):
    return drag_coeffienct * (v**2) * cross_sectional_area * 0.5 * air_density

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
lift_coefficient = 0
wing_area =0

def lift(v):
    return lift_coefficient * air_density * (v**2) * wing_area * 0.5

'''
Stuff for the force force of graphity 
'''
mass_earth = 0
G = 0

def graphity(r):
    return G * mass_earth / (r**2)


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

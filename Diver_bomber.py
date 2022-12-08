from numpy import cos,sin,tan,sqrt,pi
from matplotlib import pyplot as plt

g = 9.81

'''
Stuff for drag
'''
drag_coeffienct = 1.05 # Source: https://en.wikipedia.org/wiki/Drag_coefficient
def air_density(r):
    return 1.225 # kg/m^3
cross_sectional_area = 49.841 # m^2 Needs to change

def drag(v,r):
    return drag_coeffienct * (v**2) * cross_sectional_area * 0.5 * air_density(r)

'''
Link for thrust of propeller : https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/thrust-equation
The diver bomber used a 3-bladed hamilton standard constant speed propeller
'''
flow_rate_density = 1.225 # kg/m^3 this can change
V_propeller = 502.65 # m/s this can change
Area_propeller = 38.5 # m^2
V_exit_propeller = 100 # m/s This can change
V_entrance = 0 # m/s this can change

dugless_power = 1007E3 # kW

def thrust(r):
    #return dugless_power * dt / dd
    return air_density(r) * V_propeller * Area_propeller *(V_exit_propeller - V_entrance)

'''
Stuff for Lift
'''   
lift_coefficient = 0.0123764039313513
wing_area =30.2 # m^2 got from Douglas_SBD Dauntlass wikipedia

def lift(v,r):
    return lift_coefficient * air_density(r) * (v**2) * wing_area * 0.5

'''
Stuff for the force force of graphity 
'''
mass_earth = 5.97E24
G = 6.67E-11

def graphity(r):
    return G * mass_earth / (( r + 6.68E6 )**2)


x_bomber_with_bomb = [0]
y_bomber_with_bomb = [4267]

x_bomb = []
y_bomb = []

x_bomber = []
y_bomber =[]

vx_bomber_with_bomb = [0]
vy_bomber_with_bomb = [0]

angle_drop1 = 0
angle_drop2 = 60
angle_drop3 = 70
angle_drop4 = 80
dt = .5
t = 0
vx = 410
vy = 0
mass_bomber = 2964 #kg  Source: https://airpages.ru/eng/us/sbd.shtml
mass_bomb = 1000 # kg
M = 4318 #kg
# THis is the diving process

while t <10:
    ax =  thrust(y_bomber_with_bomb[-1]) * cos(angle_drop1) - drag(vx,y_bomber_with_bomb[-1]) * cos(angle_drop1) + lift(vx*cos(angle_drop1),y_bomber_with_bomb[-1]) * sin(angle_drop1) - graphity(y_bomber_with_bomb[-1])* M *cos(angle_drop1)
    ay =  lift(vx*cos(angle_drop1),y_bomber_with_bomb[-1]) * cos(angle_drop1) - graphity(y_bomber_with_bomb[-1])* M * cos(angle_drop1) + thrust(y_bomber_with_bomb[-1]) * sin(angle_drop1) - drag(vy,y_bomber_with_bomb[-1]) *sin(angle_drop1)
 
    vx += ax*dt * (1/M)
    vy += ay*dt * (1/M)

    vx_bomber_with_bomb.append(vx)
    vy_bomber_with_bomb.append(vy)
    x_bomber_with_bomb.append(x_bomber_with_bomb[-1] + vx*dt)
    y_bomber_with_bomb.append(y_bomber_with_bomb[-1] + vy*dt)
    t += dt



while y_bomber_with_bomb[-1] > 1080:  # Most SBD dropped around 1,500ft or 457.2 meters

    ax = thrust(y_bomber_with_bomb[-1]) * cos(angle_drop2) + lift(vx*cos(angle_drop2),y_bomber_with_bomb[-1]) * sin(angle_drop2) - drag(vx,y_bomber_with_bomb[-1]) * cos(angle_drop2) - graphity(y_bomber_with_bomb[-1])* M *cos(angle_drop2)
    ay = thrust(y_bomber_with_bomb[-1]) * sin(angle_drop2) + lift(vx*cos(angle_drop2),y_bomber_with_bomb[-1]) * cos(angle_drop2) - drag(vy,y_bomber_with_bomb[-1]) *sin(angle_drop2) - graphity(y_bomber_with_bomb[-1])*M * cos(angle_drop2)

    vx += ax*dt * (1/M)
    vy += ay*dt * (1/M)

    vx_bomber_with_bomb.append(vx)
    vy_bomber_with_bomb.append(vy)

    x_bomber_with_bomb.append(x_bomber_with_bomb[-1] + vx*dt)
    y_bomber_with_bomb.append(y_bomber_with_bomb[-1] + vy*dt)

  
x_bomb = x_bomber_with_bomb
y_bomb = y_bomber_with_bomb

x_bomber = x_bomber_with_bomb
y_bomber =y_bomber_with_bomb

vx_plane = []
vx_bomb = []
vy_plane = []
vy_bomb = []

vx_plane = vx_bomber_with_bomb
vx_bomb = vx_bomber_with_bomb

vy_bomb = vy_bomber_with_bomb
vy_plane = vy_bomber_with_bomb
m_bomb = 1000 
m_plane = M - 1000

while y_bomb[1] > 0:
    ax_plane =  thrust(y_bomber[-1]) * cos(angle_drop1) - drag(vx,y_bomber[-1]) * cos(angle_drop1) + lift(vx*cos(angle_drop1),y_bomber[-1]) * sin(angle_drop1) - graphity(y_bomber[-1])* M *cos(angle_drop1)
    ay_plane =  lift(vx*cos(angle_drop1),y_bomber[-1]) * cos(angle_drop1) - graphity(y_bomber[-1])* M * cos(angle_drop1) + thrust(y_bomber[-1]) * sin(angle_drop1) - drag(vy,y_bomber[-1]) *sin(angle_drop1)
 
    
    vxp = vx_plane[-1] + ax_plane*dt * (1/m_plane)
    vyp = vy_plane[-1] + ay_plane*dt * (1/m_plane)

    vx_plane.append(vxp)
    vy_plane.append(vyp)
    x_bomber.append(x_bomber[-1] + vxp*dt)
    y_bomber.append(y_bomber[-1] + vyp*dt)

    ax_bomb =  -1* drag(vx,y_bomber[-1]) * cos(angle_drop1) + lift(vx*cos(angle_drop1),y_bomber[-1]) * sin(angle_drop1) - graphity(y_bomber[-1])* M *cos(angle_drop1)
    ay_bomb =  lift(vx*cos(angle_drop1),y_bomber[-1]) * cos(angle_drop1) - graphity(y_bomber[-1])* M * cos(angle_drop1) - drag(vy,y_bomber[-1]) *sin(angle_drop1)
 
    
    vxb = vx_bomb[-1] + ax_bomb*dt * (1/m_bomb)
    vyb = vy_bomb[-1] + ay_bomb*dt * (1/m_bomb)

    vx_bomb.append(vxb)
    vy_bomb.append(vyb)
    x_bomb.append(x_bomb[-1] + vxb*dt)
    y_bomb.append(y_bomb[-1] + vyb*dt)
    t += dt

plt.scatter(x_bomber,y_bomber)
plt.scatter(x_bomb,y_bomb)
#plt.scatter(vx_bomber_with_bomb,vy_bomber_with_bomb)

#plt.show()



print(len(y_bomber_with_bomb))
print(y_bomber_with_bomb)

print(x_bomber_with_bomb)
#print(2* G * mass_earth* M/(((6.68E6 + 4267)**2) * wing_area * air_density(4267)*(410**2)))
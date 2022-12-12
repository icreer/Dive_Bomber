from numpy import cos,sin,tan,sqrt,pi,exp
from matplotlib import pyplot as plt

'''
stuff for air density
'''
presure_at_sea_level = 101325
temp = 300 # K
R0 = 8.314462618 # J/(mol*k)
R = 287.051 # J/(kg *K)

def air_density(r): # Sources: https://www.omnicalculator.com/physics/air-pressure-at-altitude
    p = presure_at_sea_level * exp((graphity(r)*r*0.02896969)/(temp * R0))
    return p/(R*temp) # kg/m^3

'''
Stuff for drag
'''
cross_sectional_area = 20.4 # m^2 Needs to change
drag_coeffienct = .05 # Source: https://en.wikipedia.org/wiki/Drag_coefficient
def drag(v,r, lift_factor):
    return drag_coeffienct * (v**2) * cross_sectional_area * 0.5 * air_density(r) * lift_factor

'''
Stuff for thrust
Link for thrust of propeller : https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/thrust-equation
The diver bomber used a 3-bladed hamilton standard constant speed propeller
'''

Area_propeller = 38.5 # m^2
V_exit_propeller =  9.005031648 #sqrt(V_propeller) # m/s This can change
V_entrance = 0 # m/s this can change

def thrust(r,ve):
    return .5* air_density(r) *(ve**2 - V_entrance**2)
   

'''
Stuff for Lift
'''   
lift_coefficient = 0.11
wing_area =30.2 # m^2 got from Douglas_SBD Dauntlass wikipedia

def lift(v,r, lift_fator):
    return lift_coefficient *lift_factor* air_density(r) * (v**2) * wing_area * 0.5

'''
Stuff for the force force of graphity 
'''
mass_earth = 5.97E24
G = 6.67E-11

def graphity(r):
    return G * mass_earth / (( r + 6.68E6 )**2)


#x_bomber_with_bomb = [0]
#y_bomber_with_bomb = [8000]

x_bomb = [0]
y_bomb = [8000]

x_bomber = [0]
y_bomber =[8000]

vx_bomber_with_bomb = [113.889]  # 113.889 is top speed m/s
vy_bomber_with_bomb = [0]

angle_drop1 = 0 * pi/100
angle_drop2 = 70 * pi /180

dt = 1
t = 0
vx = 100 # 113.889 is top speed m/s 
vy = 0
mass_bomber = 2964 #kg  Source: https://airpages.ru/eng/us/sbd.shtml
mass_bomb = 1000 # kg
M = 4318 #kg

# THis is the diving process

while t < 10:
    lift_factor =1
    ax =  thrust(y_bomber[-1],5)  - drag(vx,y_bomber[-1],lift_factor) 
    ay =  lift(vx,y_bomber[-1], lift_factor)  - graphity(y_bomber[-1])* M 
 
    vx += ax*dt * (1/M)
    vy += ay*dt * (1/M)
   # print(f'x {vx}')
   # print(f'y {vy}')

    vx_bomber_with_bomb.append(vx)
    vy_bomber_with_bomb.append(vy)
    x_bomber.append(x_bomber[-1] + vx*dt)

    y_bomber.append(y_bomber[-1] + vy*dt)

    x_bomb.append(x_bomb[-1] + vx * dt)
    y_bomb.append(y_bomb[-1 ]+ vy * dt)
    t += dt



while y_bomber[-1] > 1000:  # Most SBD dropped around 1,500ft or 457.2 meters
    total_speed = sqrt(vx**2 + vy**2)
    lift_factor = 1
    ax = thrust(y_bomber[-1],5) * cos(angle_drop2) + lift(total_speed ,y_bomber[-1], lift_factor) * sin(angle_drop2) - drag(total_speed ,y_bomber[-1], lift_factor) * cos(angle_drop2) 
    ay = thrust(y_bomber[-1],5) * sin(angle_drop2) + lift(total_speed ,y_bomber[-1], lift_factor) * cos(angle_drop2) - drag(total_speed ,y_bomber[-1], lift_factor) * sin(angle_drop2) - graphity(y_bomber[-1])* M 

    vx += ax*dt * (1/M)
    vy += ay*dt * (1/M)

    

    if vx >= 113:
        vx = 113
        vx_bomber_with_bomb.append(113)
    else:
        vx_bomber_with_bomb.append(vx)
        
    
    if abs(vy) >= 200:
        if abs(vy) == vy:
            vy = 200
            vy_bomber_with_bomb.append(vy)
        else:
            vy = -200
            vy_bomber_with_bomb.append(vy)
    else:
      vy_bomber_with_bomb.append(vy)  
    
    #print(f'x {vx_bomber_with_bomb[-1]}   f')
    #print(f'y {vy_bomber_with_bomb[-1]}   f')
    

    x_bomber.append(x_bomber[-1] + vx_bomber_with_bomb[-1]*dt)
    y_bomber.append(y_bomber[-1] + vy_bomber_with_bomb[-1]*dt)

    x_bomb.append(x_bomb[-1] + vx_bomber_with_bomb[-1]*dt)
    y_bomb.append(y_bomb[-1] + vy_bomber_with_bomb[-1]*dt)





vx_plane = []
vx_bomb = []
vy_plane = []
vy_bomb = []

vx_plane.append(vx_bomber_with_bomb[-1])
vx_bomb.append(vx_bomber_with_bomb[-1]) 

vy_bomb.append(vy_bomber_with_bomb[-1])
vy_plane.append(vy_bomber_with_bomb[-1])
m_bomb = 1000 
m_plane = M - 1000


angle_drop1 = 20 * pi/180
while  t < 40: 
    lift_factor = 2
    total_speed = sqrt(vx_plane[-1]**2 + vy_plane[-1]**2)
    ax_plane =  thrust(y_bomber[-1],10) * cos(angle_drop1) - drag(total_speed,y_bomber[-1],lift_factor) * cos(angle_drop1) + lift(total_speed,y_bomber[-1],lift_factor) * sin(angle_drop1) 
    ay_plane =  lift(total_speed,y_bomber[-1], lift_factor) * cos(angle_drop1) - graphity(y_bomber[-1])* m_plane + thrust(y_bomber[-1],10) * sin(angle_drop1) - drag(total_speed,y_bomber[-1], lift_factor) *sin(angle_drop1)
 
    
    vxp = vx_plane[-1] + ax_plane*dt * (1/m_plane)
    vyp = vy_plane[-1] + ay_plane*dt * (1/m_plane)

    

    if vxp >= 113:
        vxp = 113
        vx_plane.append(vxp)
    else:
        vx_plane.append(vxp)
        
    
    if abs(vyp) >= 200:
        if abs(vyp) == vyp:
            vyp = 200
            vy_plane.append(vyp)
        else:
            vyp = -100
            vy_plane.append(vyp)
    else:
        vy_plane.append(vyp)
    
    #print(t)
    #print(f'x {vx_plane[-1]}    p')
    #print(f'y {vy_plane[-1]}    p')

    x_bomber.append(x_bomber[-1] + vx_plane[-1]*dt)
    y_bomber.append(y_bomber[-1] + vy_plane[-1]*dt)

    lift_factor_b = 2
    ax_bomb =  -1* drag(vx,y_bomb[-1], lift_factor_b)  
    ay_bomb =   -1* graphity(y_bomb[-1])* m_bomb - drag(vy,y_bomb[-1],lift_factor_b) 
 
    if y_bomb[-1] <= 0:
        vx_bomb.append(0)
        vy_bomb.append(0)
    else:
        vx_bomb.append(vx_bomb[-1] + ax_bomb*dt * (1/m_bomb))
        vy_bomb.append(vy_bomb[-1] + ay_bomb*dt * (1/m_bomb))
        
    

    
    x_bomb.append(x_bomb[-1] + vx_bomb[-1]*dt)
    y_bomb.append(y_bomb[-1] + vy_bomb[-1]*dt)
    t += dt


plt.plot(x_bomber,y_bomber)
plt.plot(x_bomb,y_bomb)
#plt.xlim(4000, 8000)
#plt.ylim(0,2500)

plt.show()



from vpython import *
#Web VPython 3.2

atoms = []

scene.autoscale = False
sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=1000,shininess=0)
scene.range = 1

def generate_light(z, dx, dz, v, R, RS, C, x, Ms, Rs):
    while (x <= C):
        if (C-x)>RS:
            break
        R = ((RS**2-(C-x)**2))**(1/2)
        z = -R
        while (z <= R): 
            y = ((R**2-z**2)**(1/2))
            atoms.append(sphere(pos=vector(x, y, z), velocity = vector(-(C-x), y,z), mass=Ms, radius=Rs, color = color.yellow, make_trail = False, retain = 10))
            atoms.append(sphere(pos=vector(x, -y, z), velocity = vector(-(C-x), -y,z), mass=Ms, radius=Rs, color = color.yellow, make_trail = False, retain = 10))
            z = z + dz
        x = x + dx
    

z = -5
dx = 1
dz = 1
v = 1
R = 5
RS = 5
C = 40
x = C - RS
Ms = 0.0001
Rs = 0.01
while (x <= C):
    if (C-x)>RS:
        break
    R = ((RS**2-(C-x)**2))**(1/2)
    z = -R
    while (z <= R): 
        y = ((R**2-z**2)**(1/2))
        atoms.append(sphere(pos=vector(x, y, z), velocity = vector(-(C-x), y,z), mass=Ms, radius=Rs, color = color.yellow, make_trail = True, retain = 5))
        atoms.append(sphere(pos=vector(x, -y, z), velocity = vector(-(C-x), -y,z), mass=Ms, radius=Rs, color = color.yellow, make_trail =True, retain = 5))
        z = z + dz
    x = x + dx
    
k = 1.0


black_hole = sphere(pos=vector(0,0,0), velocity = vector(0,0,0), radius=0.001, mass=10000, color=color.black)
#black_hole_2 = sphere(pos=vector(-18,0,0), velocity = vector(0,4,0), radius=0.001, mass=100, color=color.black)
surface = sphere(pos = vector(C, 0, 0), radius = 0.25*RS, color = color.blue, mass = 1)


sun = sphere(pos = vector(0, 0, 0), velocity = vector(0,0,0), radius = RS, mass = 1000, color = color.yellow)
merc = sphere(pos = vector(0.2*C, 0, 0), velocity = vector(0,-5,-35), radius = 0.1*RS, mass = 1, color = color.red, make_trail = True, retain = 25)
venus = sphere(pos = vector(0.6*C, 0, 0), velocity = vector(0,5,-20), radius = 0.2*RS, mass = 1, color = color.blue, make_trail = True, retain = 25)
jupe = sphere(pos = vector(1.5*C, 0, 0), velocity = vector(0,3,15), radius = 0.6*RS, mass = 600, color= color.yellow, make_trail = True, retain = 20)

asteroid_count = 10
asteroids = []

while(asteroid_count):
     x = random()
     y = random()
     z = random()
     x = 2*(x-0.5)
     y = 2*(y - 0.5)
     z = 2*(z-0.5)
     M = (x**2 + y**2 + z**2)**(1/2)
     x = x/M*1.2*C
     y = y/M*1.2*C
     z = z/M*1.2*C
     
     asteroids.append(sphere(pos = vector(x, y, z), velocity = vector(z/3, y/3, x/3), radius = 0.05*RS, mass =0.05, color = color.red, make_trail = True, retain = 100))
     asteroid_count -=1

    
def gforce(p1,p2):
    # Calculate the gravitational force exerted on p1 by p2.
    G = 1 # Change to 6.67e-11 to use real-world values.
    # Calculate distance vector between p1 and p2.
    r_vec = p1.pos-p2.pos
    # Calculate magnitude of distance vector.
    r_mag = mag(r_vec)
    # Calcualte unit vector of distance vector.
    r_hat = r_vec/r_mag
    # Calculate force magnitude.
    force_mag = G*p1.mass*p2.mass/r_mag**2
    # Calculate force vector.
    force_vec = -force_mag*r_hat
    
    return force_vec

t = 0
dt = 0.01
while True:
    rate(1000)
    generate_light(z, dx, dz, v, R, RS, C, x, Ms, Rs)
    merc.force = gforce(merc,black_hole)
    merc.force += gforce(merc,venus)
    merc.velocity = merc.velocity + merc.force/merc.mass*dt
    merc.pos = merc.pos + merc.velocity*dt
    
    venus.force = gforce(venus,black_hole)
    venus.force += gforce(venus, merc)
    venus.velocity = venus.velocity + venus.force/venus.mass*dt
    venus.pos = venus.pos + venus.velocity*dt
    
    jupe.force = gforce(jupe,black_hole)
    jupe.velocity = jupe.velocity + jupe.force/jupe.mass*dt
    jupe.pos = jupe.pos + jupe.velocity*dt


    
    
    for asteroid in asteroids:
        asteroid.force = gforce(asteroid, black_hole)
        for other_asteroid in asteroids:
            if other_asteroid != asteroid:
                asteroid.force += gforce(asteroid, other_asteroid)
        asteroid.force += gforce(merc, asteroid)
        asteroid.force += gforce(venus, asteroid)
        asteroid.force += gforce(jupe, asteroid)
        asteroid.velocity = asteroid.velocity + asteroid.force/asteroid.mass*dt
        asteroid.pos = asteroid.pos + asteroid.velocity*dt

    
    
#        black_hole.force = gforce(black_hole, black_hole_2)
#        black_hole_2.force = gforce(black_hole_2, black_hole)
#    #    
#        
#        black_hole.velocity = black_hole.velocity + black_hole.force/black_hole.mass*dt
#        black_hole.pos = black_hole.pos + black_hole.velocity*dt
#        
#        black_hole_2.velocity = black_hole_2.velocity + black_hole_2.force/black_hole_2.mass*dt
#        black_hole_2.pos += black_hole_2.velocity*dt
#    #    
    for j in range(0,len(atoms)):
        atoms[j].force = gforce(atoms[j],black_hole)
        atoms[j].force += gforce(atoms[j],merc)
        atoms[j].force += gforce(atoms[j], venus)
        atoms[j].force += gforce(atoms[j], jupe)
        for asteroid in asteroids:
            atoms[j].force += gforce(atoms[j], asteroid)
        if (j>0):
            atoms[j].force = atoms[j].force 
        if (j>len(atoms)-1):
            atoms[j].force = atoms[j].force
    for j in range(0,len(atoms)):
        atoms[j].velocity = atoms[j].velocity + atoms[j].force/atoms[j].mass*dt
        atoms[j].pos = atoms[j].pos + atoms[j].velocity*dt
    t = t + dt
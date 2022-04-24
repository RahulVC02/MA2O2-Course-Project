from vpython import *
#Web VPython 3.2

scene.autoscale = False
sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=100,shininess=0)
scene.range = 30

atoms = []

z = -5
dz = 1
dx=1
x = 8
v = 1


while (x < 10):
    z = -5
    while (z < 5):
        atoms.append(sphere(pos=vector(-35+x,((25-(13-abs(x))**2)-z*z)**1/2,z), velocity=vector(1*v*(13-abs(x)),v*((25-(13-abs(x))**2-z*z)**1/2+10),v*z), mass=0.0001,
                     radius=0.1, color=color.yellow, make_trail = True, retain = 200))
        atoms.append(sphere(pos=vector(-35+x,-1*((25-(13-abs(x))**2)-z*z)**1/2,z), velocity=vector(1*v*(13-abs(x)),v*(-1*(25-(13-abs(x))**2-z*z)**1/2-10),v*z), mass=0.0001,
                     radius=0.1, color=color.yellow, make_trail = True, retain = 200))
        atoms.append(sphere(pos=vector(35-x,(25-(13-x)**2-z*z)**1/2,z), velocity=vector(-1*v*(13-x),v*((25-(13-x)**2-z*z)**1/2+10),v*z), mass=0.0001,
                     radius=0.1, color=color.yellow, make_trail = True, retain = 200))
              
        atoms.append(sphere(pos=vector(35-x,(25-(13-x)**2-z*z)**1/2,z), velocity=vector(-1*v*(13-x),v*(-1*(25-(13-x)*2-z*z)**1/2-10),v*z), mass=0.0001,
                    radius=0.1, color=color.yellow, make_trail = True, retain = 200))
        z = z + dz
    x = x + dx


k = 1.0
l0 = dx


black_hole = sphere(pos=vector(0,0,0), radius=5, mass=100000, color=color.black)

   
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
   
#def xdist_origin(p1):
#    r_vec=p1.pos
t = 0
dt = 0.01
while (t<0.45):
    rate(10)
   
    for j in range(0,len(atoms)):
        atoms[j].force=gforce(atoms[j],black_hole)
        atoms[j].pos = atoms[j].pos + atoms[j].velocity*dt + (atoms[j].force/atoms[j].mass)*(dt)**2
        next_force=gforce(atoms[j],black_hole)
        atoms[j].velocity = atoms[j].velocity + (((atoms[j].force)+(next_force))/(atoms[j].mass))*(dt/2)
               
    t = t + dt
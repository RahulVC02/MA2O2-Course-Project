from vpython import *
#Web VPython 3.2

scene.autoscale = False
sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=100,shininess=0)
scene.range = 30

atoms = []

z = -5
dx = 1
dz = 1
v = 1
R = 5
RS = 5
C = 40
x = 90
Ms = 0.0001
Rs = 0.05
R = 6
z = -R
while (z <= R): 
    y = ((R**2-z**2)**(1/2))
    atoms.append(sphere(pos=vector(x, y, z), velocity = vector(-20, 0,0), mass=Ms, radius=Rs, color = color.yellow, make_trail=True))
    atoms.append(sphere(pos=vector(x, -y, z), velocity = vector(-20, 0,0), mass=Ms, radius=Rs, color = color.yellow, make_trail=True))
    z = z + dz
    
for atom in atoms[-15:]:
    attach_light(atom)

for atom in atoms[:15]:
    attach_light(atom)
    
for atom in atoms:
    attach_trail(atom, radius = 0.1, retain = 10)
    
    
k = 1.0
l0 = dx

offset = 13
black_hole = sphere(pos=vector(offset,0,0), radius=5,velocity = vector(0,0,-15), mass=1E4, color=color.black, make_trail = False)
other_hole = sphere(pos=vector(-1*offset,0,0), radius=5,velocity = vector(0,0,15), mass=1E4, color=color.black, make_trail = False)

    

   
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
#while (t<0.425):
while(t<5):
    rate(60)
    black_hole.force = gforce(black_hole, other_hole)
    black_hole.velocity += black_hole.force/black_hole.mass*dt
    black_hole.pos += black_hole.velocity*dt
    
    other_hole.force = gforce(other_hole, black_hole)
    other_hole.velocity += other_hole.force/other_hole.mass*dt
    other_hole.pos += other_hole.velocity*dt
    
    
    for j in range(0,len(atoms)):
        atoms[j].force=gforce(atoms[j],black_hole)
        atoms[j].force += gforce(atoms[j], other_hole)
        atoms[j].pos = atoms[j].pos + atoms[j].velocity*dt + (atoms[j].force/atoms[j].mass)*(dt)**2
        next_force=gforce(atoms[j],black_hole)
        atoms[j].velocity = atoms[j].velocity + (((atoms[j].force)+(next_force))/(atoms[j].mass))*(dt/2)
               
    t = t + dt
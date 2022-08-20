
# Iterative solutions for n-body simulations.
<img height="300" alt="image" src="https://user-images.githubusercontent.com/76529011/185738668-57d533b5-40de-4d5d-92b7-d1c96ac2b5ba.png" align="right">


Code for investigating the behaviour of particles in the vicinity of $n$ massive objects. When a 3rd body is added to a 2-body system, no analytical solution exists. For the undertaking, we consider particles to be massless bodies, while massive bodies (understandably) have mass. 

Techniques used include the Verlet Integration, the Euler Cromer method, using Newton's Law of Gravitation. Future plans include adding relativistic physics to the simulation.

The scripts are written in VPython. It is recommended to run them on https://glowscript.org. Check out an implementation of a binary star system collapsing [here](https://www.glowscript.org/#/user/progyan.das/folder/MyPrograms/program/blackhoooole).

----------------------

### The velocity-Verlet algorithm
<img width="450" alt="image" src="https://user-images.githubusercontent.com/76529011/185738704-4d8c0f37-d331-4c7b-86a8-9953b1397a52.png" align="left">

Verlet integration is a method used to solve the Newton’s equations
of motion. It is an algorithm to perform the integration for solving
the Newton’s equations. Velocity verlet method is an algorithm which
has similarities to the leapfrog method. The only difference is that
the velocity and position are calculated at the same value fo the time
variable. The algorithm consists of clear steps to find the solution.
This method uses the approach where it explicitly incorporates the
velocity, solving the problem of the first time step in the basic Verlet
algorithm.


```
Compute 𝑥(𝑡+Δ𝑡)=𝑣(𝑡)+12𝑎(𝑡)Δ𝑡2
Compute 𝑎(𝑡+Δ𝑡) using the updated position
Compute 𝑣(𝑡+Δ𝑡)=𝑣(𝑡)+12(𝑎(𝑡)+𝑎(𝑡+Δ𝑡))Δ𝑡
 ```
 
 ------------------------
 
 
 
 ### The Euler-Crömer method
 
 At every time step $i$ we compute the position $(x, y, z)$ and the velocity along $x$ and $y$ axis $(vx, vy, vz)$

<img width="347" alt="image" align="right" src="https://user-images.githubusercontent.com/76529011/185739868-c3762986-5cfe-4cd0-bcdd-97d898140a12.png">


```
– First we calculate the distance ri from the reference celestial object.
– Calculate the values of vx,i+1, vy,i+1 and vz,i+1 as vx,i+1 = v,xi+ax,i ∆t, vy,i+1 = vy,
  i +ay,i ∆t and vz,i+1 = vz,i +az,i ∆t.
– Now compute xi+1,yi+1 and zi+1 using vx,i+1, vy,i+1 and vz,i+1 as xi+1 = xi + vx,i+1 ∆t, 
  yi+1 = yi + vy,i+1 ∆t and zi+1 = zi + vz,i+1 ∆t.
– Now compute ax,i+1, ay,i+1 and az,i+1 using the new position values xi+1, yi+1 and zi+1.
– Memorize these positions xi+1, yi+1 and zi+1 and also accelerations ax,i+1, ay,i+1 and 
  az,i+1 for the next iteration.
```
---------------------------

### Credits

This has been a group effort by Rahul Chembakasseril, Progyan Das, Varad Sardeshpande, Saniya Patwardhan, and Rahul Lalani.



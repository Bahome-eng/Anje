import numpy as np
import matplotlib.pyplot as plt

k = 10

F0 = 12       
k = 10.0      
# D = 0.05      
# beta = 1.6e-4 
# b = beta * D 
b=.1
F0 = 5.0      
omega_d = 6.0  
m = 0.1  

1/4*(b/m)**2 == k/m
b**2 == m*k*4
 
def force(t, x, v, omega_d):
    return -k * x - b * v + F0 * np.cos(omega_d * t)



nsteps = 1000
t_max = 20


x0 = 1   
v0 = 0 
w0 = np.sqrt(k/m)
F0 = 2.5

nsteps = 1000  # Number of steps


t, dt = np.linspace(0, 20, nsteps, retstep=True)


data = np.zeros((nsteps, 2))

pos = x0
vel = v0
for i, ti in enumerate(t):
    acc = force(ti, pos, vel, omega_d)/m
    vel = vel + acc * dt
    pos = pos + vel * dt
    data[i] = t[i], pos

        
       
analytical = x0 * np.cos( w0 * t)
print(b**2)
print(4*m*k)

plt.plot(data[:,0],data[:,1]) 
plt.legend()

plt.savefig()
plt.savefig("Phingegee.png")
plt. close()





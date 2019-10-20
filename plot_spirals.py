import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

num_of_spokes = 3

ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
line, = ax.plot([], [], lw=2,marker='o')
line2, = ax.plot([], [], lw=2,marker='o',color='r')
fig = plt.gcf()

def animate(i,j):
    dTheta = 1/180*np.pi
    rpm = np.arange(10,0.5,-0.5)
    r = np.arange(0.5,10,0.5)
    for k in range(j):
    	Theta = i*dTheta*rpm+k*2*np.pi/j
    	x = r * np.cos(Theta)
    	y = r * np.sin(Theta)
    	line, = ax.plot(x,y, lw=2,marker='o', color = 'b')
    
camera = Camera(fig)

for i in range(720):
    animate(i, num_of_spokes)
    camera.snap()

animation = camera.animate()
animation.save('spirals_{}.mp4'.format(num_of_spokes), fps=30, extra_args=['-vcodec', 'libx264'])

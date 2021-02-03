import numpy as np
import matplotlib as mpl
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.contour import QuadContourSet
from matplotlib.widgets import Slider

#Define display parameters
mpl.rcParams['xtick.direction'] = 'out'
mpl.rcParams['ytick.direction'] = 'out'
#delta = 0.025

#Define model parameters
lamda = 1.0
x = np.linspace(0.0, 10.0, 100)
y = np.linspace(-10.0, 10.0, 100)

#Plotting function
def compute_and_plot(ax, lamda):
    #Calculate grid values
    X, Y = np.meshgrid(x,y)
    E = np.sin(2*np.pi*np.sqrt(X**2 + (Y - 1)**2)/lamda) + np.sin(2*np.pi*np.sqrt(X**2 + (Y + 1)**2)/lamda)
    CS = QuadContourSet(ax, X, Y, E, 200)
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")

# Plot
fig = plt.figure()
plt.title('Interference Plot')
ax = fig.add_subplot(111)
compute_and_plot(ax, lamda)

#Define slider for lambda
axcolor = 'lightgoldenrodyellow'
lamda_axis  = plt.axes([0.3, 0.0125, 0.4, 0.05])
lamda_slider = Slider(lamda_axis, 'Wavelength, $\lambda$ (m)', 1.0, 10.0, valinit=1.0)

def update(ax, val):
    lamda = lamda_slider.val
    ax.cla()
    compute_and_plot(ax, lamda)
    plt.draw()

lamda_slider.on_changed(lambda val: update(ax, val))

plt.show()
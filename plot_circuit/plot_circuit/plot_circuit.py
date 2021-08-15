import matplotlib.pyplot as plt
import numpy as np

''' 
The purpose of this code is to plot in a semilog scale  
the relationaship between Vout/Vopen V.S. Rload/Rout
and % Reduction from Vopen V.S Rload/Rout
in the same plot, sharing the same x-axis, and display 
two diferent y axis. Use the Thevenin circuit as reference.

Vout/Vopen= (Rload/Rout)/(1+(Rload/Rout))
%_Reducation_from_Vopen=(1-Vout/Vopen)*100
'''
# Generate data
dr = 0.01 # Step size of Rload/Rout
Rload_Rout = np.arange(dr, 100.0, dr)       # x-axis  data  
Vout_Vopen= Rload_Rout / (1+Rload_Rout)     # y1-axis data
reduction_Vopen_percent=(1-Vout_Vopen)*100  # y2-axis data

# Create axis one object and a figure object
fig, ax1 = plt.subplots() 

# Axis-one object settings
color = 'tab:red'
ax1.set_xlabel(r'$R_{Load}/R_{Out}$')
ax1.set_ylabel(r'$V_{Out}/V_{Open}$', color=color)
ax1.semilogx(Rload_Rout, Vout_Vopen, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0,1)
ax1.set_xlim(.1,100)
ax1.grid()

# Instantiate a second axes that shares the same x-axis
ax2 = ax1.twinx()  

# Axis-two object settings
color = 'tab:blue'
ax2.set_ylabel(r'% Reducation from $V_{Open}$', color=color)  # we already handled the x-label with ax1
ax2.semilogx(Rload_Rout, reduction_Vopen_percent, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0,10)


plt.show()
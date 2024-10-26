import numpy as np
import matplotlib.pyplot as plt
# Constants
timestep = 0.01
g = 9.81
m = 1

#read from thrust curve csv file
thrustCurve = []
count = 0
with open('TSP_D12.csv', 'r') as file:
    for line in file:
        if count < 5:
            count += 1
            continue
        line = line.split(',')
        line[0] = float(line[0])
        line[1] = float(line[1])
        thrustCurve.append(line)
for line in thrustCurve:
    print(line)

#print the thrust curve
time = []
thrust = []
for line in thrustCurve:
    time.append(line[0])
    thrust.append(line[1])
plt.plot(time, thrust)
plt.show()
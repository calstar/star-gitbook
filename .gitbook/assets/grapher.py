import numpy as np
import matplotlib.pyplot as plt

# Get data from CSV file.
data = np.genfromtxt("../SIL/normal_pos_data.csv", delimiter=',', usecols = (0, 2))

time = data[:, 0]
time_step = time[0]
altitude = data[:, 1]

ax = plt.plot(time/time_step, altitude, 'o', label='Altitude', markersize=10)
plt.title("Time vs. Altitude")
plt.xlabel("Time (10000)", fontsize=16)
plt.ylabel("Altitude (feet)", fontsize=16)
plt.savefig("altitude.png", dpi=250)
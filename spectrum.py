#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

sampling = 128 
num_files = 23315  
step = 10  


frequencies = []
amplitudes = []
times = []


N = sampling
delta = 1.0 / N
f_c = 1.0 / (2.0 * delta)

for i in np.arange(0, int(N / 2)):
    n = (-N / 2) + i    
    frequencies.append(f_c + (n / (N * delta)))


for t in range(0, num_files, step):
    filename = f"spectrum-mpi-{t}.dat"
    with open(filename) as f:
        data = f.readlines()
    
    signal = []
    for i, line in enumerate(data):
        if 1 <= i <= sampling / 2:
            signal.append(float(line))
    

    amplitudes.append(signal)
    times.append(t)  


frequencies = np.array(frequencies)
amplitudes = np.array(amplitudes)
times = np.array(times)


T, F = np.meshgrid(times, frequencies)


A = np.array(amplitudes).T


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(F, T, A, cmap='viridis')


ax.set_xlabel('Frecuency (Hz)')
ax.set_zlabel('Amplitud')
ax.set_ylabel('Time (s)')


output_filename = '3D spectrum.png'
plt.savefig(output_filename)


plt.close(fig)


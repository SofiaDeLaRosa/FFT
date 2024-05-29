import matplotlib.pyplot as plt
import numpy as np


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


for i, t in enumerate(times):
    fig, ax = plt.subplots()
    ax.plot(frequencies, amplitudes[i])
    ax.set_xlabel('Frecuency (Hz)')
    ax.set_ylabel('Amplitud')
    ax.set_title(f'Time: {t}s')
    plt.tight_layout()
    output_filename = f'spectrum_{i}.png'
    plt.savefig(output_filename)
    plt.close(fig)


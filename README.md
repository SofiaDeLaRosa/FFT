<h1 align="center" style="color:red;">  High Performance Computing HPC </h1>

# Fast Fourier Transform (FFT)

Final Project of the High Performance Computing 2024-2 class, taught by [Dr. Victor de la Luz](https://github.com/itztli) (<vdelaluz@enesmorelia.unam.mx>) at *[Universidad Nacional Autónoma de México](https://www.unam.mx/)* (National Autonomous University of Mexico | UNAM) [http://www.gicc.unam.mx/](http://www.gicc.unam.mx/), in its *[Escuela Nacional de Estudios Superiores, Unidad Morelia](https://www.enesmorelia.unam.mx/)* (National School of Superior-Level Studies, *Morelia* Campus | ENES).

Author: 
[Sofia De La Rosa](https://github.com/SofiaDeLaRosa) (<chapatulita@gmail.com>)

## Introduction

The Fast Fourier Transform (FFT) is an efficient algorithm for computing the Discrete Fourier Transform (DFT) and its inverse. Developed to significantly reduce the complexity of performing Fourier transforms, the FFT is widely used in various fields such as signal processing, audio analysis, and image compression.

FFT allows us to distinguish patterns within the signal, this capability is crucial for identifying the predominant frequencies present in the signal. The FFT's efficiency and speed make it ideal for applications that require real-time signal processing, such as audio signal processing, telecommunications, and vibration analysis.

In other hand, OpenMPI; or Open Message Passing Interface, is an open-source implementation of the MPI standard, designed for high-performance computing (HPC). MPI is a communication protocol used to program parallel computers, allowing processes to communicate with each other by sending and receiving messages.

The Barber Method is a classic synchronization problem in computer science used to illustrate and solve issues related to process synchronization and resource allocation. In this problem, a barber shop with a single barber has a waiting room with a limited number of chairs for customers. If the barber is busy and all chairs are occupied, arriving customers leave. Otherwise, customers wait in an available chair or get their haircut if the barber is free. The challenge is to manage the coordination between the barber and the customers efficiently, ensuring that the barber works when there are customers and sleeps when there are none, and that customers do not wait indefinitely or leave unnecessarily.

##  Metodology

We calculate FFT of the Nirvana's unplugged concert in New York in 1994 and generate the spectra of the frequencies.
  
We use:

* [Open MPI](https://www.open-mpi.org/) versión 4.1.2
* [Python3](https://www.python.org/downloads/)
* [Matplotlib](https://matplotlib.org/)

##  Running

We chose an audio wave that we wanted to analyze, in this case, it was Nirvana's unplugged concert in New York in 1994.

Firstly, we transform the mp3 into wav format.

Then, we ran the following command to convert our file from stereo to mono:

* ffmpeg -i nirvana-unplugged-in-new-york-1994.wav -ac 1 nirvana.wav

We ran plot-wav.py. If you want to try with your file, make sure to change to your mono filename in plot-wav.py.

Then, we ran the following command to execute fft.c to read the data or generate synthetic data, counts the number of samples when reading data N, the master node divides the samples by the window size and distribute samples to slave nodes, each slave node calculates the FFT for each sample using MPI and the spectra are saved in files 'output/spectrum-mpi-<index>.dat'. 
Also, we calculate the memory allocation in MB and the benchmarks of the system, the user and the real (sum of the system and the user) in sec to measure code and parallel processing performance.

We decide the size of window and it must be a power of 2, so that the fast Fourier transform is calculated. The number of spectra is the number of samples N divided by the window size.

* mpiexec -n 2 ./fft -file nirvana.dat -window 1024 -spectrum

where n is the number of nodes, nirvana.dat is the file and 1024 is the size of the window 

## References 
 
[https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
[https://www.open-mpi.org/](https://www.open-mpi.org/)

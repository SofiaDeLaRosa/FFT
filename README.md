<h1 align="center" style="color:red;">  High Performance Computing HPC </h1>

# Fast Fourier Transform (FFT)

Final Project of the High Performance Computing 2024-2 class, taught by [Dr. Victor de la Luz](https://github.com/itztli) (<vdelaluz@enesmorelia.unam.mx>) at *[Universidad Nacional Autónoma de México](https://www.unam.mx/)* (National Autonomous University of Mexico | UNAM) [http://www.gicc.unam.mx/](http://www.gicc.unam.mx/), in its *[Escuela Nacional de Estudios Superiores, Unidad Morelia](https://www.enesmorelia.unam.mx/)* (National School of Superior-Level Studies, *Morelia* Campus | ENES).

Author: 
[Sofia De La Rosa](https://github.com/SofiaDeLaRosa) (<chapatulita@gmail.com>)

## Introduction

The Fast Fourier Transform (FFT) is an efficient algorithm for computing the Discrete Fourier Transform (DFT) and its inverse. Developed to significantly reduce the complexity of performing Fourier transforms, the FFT is widely used in various fields such as signal processing, audio analysis, and image compression.

FFT allows us to distinguish patterns within the signal, this capability is crucial for identifying the predominant frequencies present in the signal. The FFT's efficiency and speed make it ideal for applications that require real-time signal processing, such as audio signal processing, telecommunications, and vibration analysis.

In other hand, Open Message Passing Interface (OpenMPI) is an open-source implementation of the MPI standard, designed for high-performance computing (HPC). MPI is a communication protocol used to program parallel computers, allowing processes to communicate with each other by sending and receiving messages.

The Barber Method is a classic synchronization problem in computer science used to illustrate and solve issues related to process synchronization and resource allocation. Basically what it does is:

1. Ask if there is a free process to assign a task.
2. Ask if the process is over to receive results.

##  Metodology

We record an audio of birds singing and generate the spectra of the frequencies by calculating FFT in parallel using OpenMPI and the Barber Method.
  
We use:

* [Open MPI](https://www.open-mpi.org/) 4.1.2 version
* [Python3](https://www.python.org/downloads/)
* [Matplotlib](https://matplotlib.org/)

##  Running

We need to have our wav, fft.c, plot-wav.py, plot-spectrum.py, GNUmakefile, Timming, myvar.h files in the **same folder**.

Firstly, convert the mp3 into wav format.

Run the following command to convert our file from stereo to mono, make sure to rename the files to our:

* ffmpeg -i birdsong.wav -ac 1 data-bird.wav

Run plot-wav.py file, make sure to change the wav file to our.

Create a **folder called ouput**. This is where the output data of fft.c will be saved.

GNUmakefile compiles and links a C program using gcc and mpicc. In PROGRAM, we need to specify our C filename. In '$(OBJS)' and '$(PROGRAM)' section, we need to we need to **specify the path to openmpi** starting with -I/. 

For example:
**-I/usr/lib/x86_64-linux-gnu/openmpi/include/**

Compile the program with the command **make**.  

Run this command every time we want to remove temporary and object files: **make clean**.

Then, run the following command to execute fft.c that read the data or generate synthetic data, counts the number of samples when reading data N, the master node divides the samples by the window size and distribute samples to slave nodes, each slave node calculates the FFT for each sample using MPI and the spectra are saved in files 'output/spectrum-mpi-<index>.dat'. 
We ran plot-wav.py. If you want to try with your file, make sure to change to your mono filename in plot-wav.py.

Also, with the Timming files, it calculates the memory allocation in MB and the benchmarks of the system, the user and the real (sum of the system and the user) in sec to measure code and parallel processing performance.

Choose the size of window and **it must be a power of 2**, so that the fast Fourier transform is calculated. The number of spectra is the number of samples N divided by the window size.

* mpiexec -n 2 ./fft -file data-bird.dat -window 128 -spectrum

where n is the number of nodes, nirvana.dat is the file and 1024 is the size of the window 

Run spectrum.py to get a single plot of frequencies in Hz, times in s and amplitudes for all windows, every 10 windows: (in x, y, z axis respectively).

In other hand, run spectrum2.py to get a plot of frequencies in Hz and amplitudes for every 10 windows (in x, y axis respectively).

## Results

Here are the graphs of the amplitudes and frequencies with and without graphing the times respectively.

![alt text](https://github.com/SofiaDeLaRosa/FFT/blob/main/3Dspectrum.png) 

![alt text](https://github.com/SofiaDeLaRosa/FFT/blob/main/spectrum_6.png) 


## References 
 
[https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
[https://www.open-mpi.org/](https://www.open-mpi.org/)

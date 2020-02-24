# fourier.py
# plot a fourier series

# f(x) = -x, -1 <= x <= 0
#      =  x,  0 <= x <= 1

# coefficients are a_0 = 1/2
# a_n = -4/(n^2pi^2) for odd n and = 0 otherwise

# c.f. maths of waves and fields example sheet 1 Q2c

# plot f(x) and the fourier series approximation to it

import numpy as np;
import matplotlib.pyplot as plt;

# create an array of numbers -1 to 1 step 0.02
x = np.linspace(-1.0, 1.0, 100);

# plot f(x)
plt.plot(x,x,'r-');
plt.plot(-x,x,'r-');

plt.ylim(0.0,1.0);

# work out the fourier series
# use x array for the x values
# need a number of terms

n = 4;

fSeries = [];

for j in range(0,len(x)):
    # for all x, make fSeries = a_0 = 0.5
    fSeries.append(0.5);

for i in range(1,n,2):
    # this is for each term
    for j in range(0,len(x)):
        # this is for each value of x, of which there are len(x)
        # add on the term to each element of fSeries
        term = -4.0 * np.cos(i*np.pi*x[j]) / (pow(i,2) * pow(np.pi,2));
        fSeries[j] = fSeries[j] + term;
    
plt.plot(x,fSeries);

# show the graph
plt.show();




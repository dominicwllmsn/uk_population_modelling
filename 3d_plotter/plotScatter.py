# plotScatter.py
# program to read some data and plot a graph

# import the module
import matplotlib.pyplot as plt;
import numpy as np;

# open the file
readFile = open('xy.txt','r');

# create empty arrays
x = [];
y = [];

# read in the file line by line
for line in readFile:
    # split the input line based on a whitespace
    splitUp = line.split();

    # store the values in the arrays
    x.append(float(splitUp[0]));
    y.append(float(splitUp[1]));

# close the file
readFile.close();

# colours
colours = np.random.rand(len(x));

# areas 
areas = np.random.rand(len(x))*1000;

# plot a scatter graph
plt.scatter(x,y,c=colours,s=areas);

# add a title
plt.title('Scatter Plot of xy.txt');

# label the axes
plt.xlabel('x');
plt.ylabel('y');

# show the graph
plt.show();


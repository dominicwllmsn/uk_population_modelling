# plotGraph.py
# program to plot a graph

# import the module
import matplotlib.pyplot as plt;

# create some data
x = [ 1,2,3,4,5 ];
y = [ 3,1,6,9,10 ];
z = [ 4,2,8,1,5 ];

# plot the graph
plt.plot(x,y);

# label the axes
plt.xlabel('x data values');
plt.ylabel('y data values');

# give the plot a title
plt.title('A wonderful example graph');

# show the graph
plt.show();


# inputOutput2

import matplotlib.pyplot as plt

# Open file containing x and y data
xyFile = open('xyData.txt','r')
# Create empty lists to contain the x and y values respectively.
x_list = []
y_list = []
# Loop through each line of file, assign x values to x_list & y values to y_list
for line in xyFile:
    x_list.append(float(line.split()[0]))
    y_list.append(float(line.split()[1]))
   
xyFile.close()


###Calculation of line of best fit
# Create variable for number of x (or y) values, N, as well as a list containing
# x**2 values and a list containing x*y values 
N = len(x_list)
xsq_list = [x**2 for x in x_list]
xy_list = [x*y for x in x_list for y in y_list if x_list.index(x) == y_list.index(y)]

D = N*sum(xsq_list) - sum(x_list)**2
# Gradient and uncertainty on gradient of best-fit line
m = (N*sum(xy_list)-sum(x_list)*sum(y_list))/D  
dm = (N/D)**0.5                                 
# y-intercept and uncertainty on y-intercept of best-fit line
c = (sum(y_list)*sum(xsq_list)-sum(x_list)*sum(xy_list))/D  #best fi
dc = (sum(xsq_list)/D)**0.5

print('m = {0:.4f} +/- {1:.4f}*sigma, c = {2:.4f} +/- {3:.4f}*sigma'\
      .format(m,dm,c,dc))
###
### Create plot of x and y values as well as best-fit line
N = 101
x_range = max(x_list)
x_interval = x_range/N
x_value = 0
x_line = []
y_line  = []
for i in range(N):
    x_line.append(x_value)
    y_line.append(m*x_value+c)
    x_value += x_interval
    

plt.plot(x_list,y_list,'rx',x_line,y_line,'b-')
plt.axis(xmin = 0,ymin = 0)
plt.title('Graph of X versus Y')
plt.text(10,5.5,'best-fit line')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
###
# Create text file with columns of x values, y values, the best-fit y values
# and the residuals between the best-fit and true y values.
writeFile = open('best_fit.txt','w')

for i in range(len(x_list)):
    y_best = m*x_list[i]+c
    residual = y_best-y_list[i]
    writeFile.write('\t{0: .0f}\t\t{1: .2f}\t\t{2: .2f}\t\t{3: .2f}\n'\
                    .format(x_list[i],y_list[i],y_best,residual))

writeFile.close()

    


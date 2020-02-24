# inputOutput1

import math


xyFile = open('xyData.txt','r')

x_list = []
y_list = []

for line in xyFile:
    x_list.append(float(line.split()[0]))
    y_list.append(float(line.split()[1]))
   
xyFile.close()
writeFile = open('xyHypot.txt','w');

for i in range(len(x_list)):
    hypot = math.hypot(x_list[i],y_list[i])
    writeFile.write('\t{0}\t\t{1}\t\t{2}\n'.format(x_list[i],y_list[i],hypot))
    
writeFile.close()
    

    


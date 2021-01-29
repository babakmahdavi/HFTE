"""
Created on Tue Jan 15 21:06:07 2019
Last Update: Friday 29 January 09:17:00 2021
Context: Supporting material for the paper "Guidelines for Building a Realistic Algorithmic Trading Market Simulator for Backtesting while Incorporating Market Impact"
What it does: This is a simplification of the HFT game. We examine, in sequence how different classic financial strategies fair with respect to each other via an orderbook
Author: Babak Mahdavi-Damghani
Address: University of Oxford, Oxforf Man Institute of Quantitative Finance, Oxford, UK
Tel: 07815852573
email: bmd@eqrc.co.uk
"""

from numpy import *
from numpy.random import *
import numpy
import numpy as np
import matplotlib.pyplot as plt

import time

from matplotlib.lines import Line2D
from matplotlib.patches import Patch




def scenariosHT(strategy,iteration):
  s1 = [0,0,3,6,15,33,69]
  s2 = [0,0,3,-3,11,26,75]
  s3 = [0,0,-1,-3,-3,-3,-3]
  s4 = [0,0,3,5,13,28,58]
  s5 = [0,0,3,-5,15,36,78]
  s6 = [0,0,-1,-4,-6,-10,-18]
  s7 = [0,0,3,5,11,23,47]
  s8 = [0,0,3,-4,11,27,27]
  s9 = [0,0,-1,3,3,3,3]    
  s10 = [0,0,3,4,-13,31,-54]
  s11 = [0,0,-2,3,-14,-32,-54]    
  s12 = [0,0,3,-4,7,15,31]        
  s13 = [0,0,-1,-5,6,14,30]       
  s14 = [0,0,-1,-6,18,45,97]      
  s15 = [0,0,3,-3,16,-46,-104]    
  scenarios = numpy.array([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15])
  dummy = scenarios
  return dummy[strategy][returnArrayPosition(iteration)]
  
  
def returnArrayPosition(iteration):
    if iteration == 0:
        return 0
    elif  iteration == 2:
        return 1
    elif  iteration == 3:
        return 2
    elif  iteration == 5:
        return 3
    elif  iteration == 11:
        return 4
    elif  iteration == 23:
        return 5
    elif  iteration == 47:
        return 6
    else:
        return 'issue with iteration recognition'
    

s1 = [0,0,3,6,15,33,69]
s2 = [0,0,3,-3,11,26,75]
s3 = [0,0,-1,-3,-3,-3,-3]
s4 = [0,0,3,5,13,28,58]
s5 = [0,0,3,-5,15,36,78]
s6 = [0,0,-1,-4,-6,-10,-18]
s7 = [0,0,3,5,11,23,47]
s8 = [0,0,3,-4,11,27,27]
s9 = [0,0,-1,3,3,3,3]    
s10 = [0,0,3,4,-13,31,-54]
s11 = [0,0,-2,3,-14,-32,-54]    
s12 = [0,0,3,-4,7,15,31]        
s13 = [0,0,-1,-5,6,14,30]       
s14 = [0,0,-1,-6,18,45,97]      
s15 = [0,0,3,-3,16,-46,-104]    

xAxis = [0,2,3,4,11,23,47]

realMarketPrice =  numpy.multiply(s1,1/15)+numpy.multiply(s2,1/15)+numpy.multiply(s3,1/15)+numpy.multiply(s4,1/15)+numpy.multiply(s5,1/15)+numpy.multiply(s6,1/15)+numpy.multiply(s7,1/15)+numpy.multiply(s8,1/15)+numpy.multiply(s9,1/15)+numpy.multiply(s10,1/15)+numpy.multiply(s11,1/15)+numpy.multiply(s12,1/15)+numpy.multiply(s13,1/15)+numpy.multiply(s14,1/15)+numpy.multiply(s15,1/15)

randomSeed = int(time.time())    
np.random.seed(randomSeed)

fig, ax = plt.subplots(1, 1)

#plt.setp(lines, color='r', linewidth=2.0)
plt.plot(xAxis,s1,'k' ,xAxis,s2,'-k' , xAxis,s3,'-k' , xAxis,s4,'k' , xAxis,s5,'k' , xAxis,s6,'k' , xAxis,s7,'k' , xAxis,s8,'k' , xAxis,s9,'k' , xAxis,s10,'r' , xAxis,s11,'r' , xAxis,s12,'r', xAxis,s13,'r', xAxis,s14,'r', xAxis,s15,'r',linewidth=.5    ) 


h = plt.ylabel('y')
h.set_rotation(0)

#plt.title('Price fluctuation in Ecosystems with 2 strategies')
#plt.xlabel('Iteration')
ax.set_ylabel('$\Delta P$', fontsize=6)
ax.set_xlabel('Iteration', fontsize=6)

#plt.ylabel('$\Delta P$')
#plt.legend(['$s_1$', '$s_2$', '$s_3$', '$s_4$', '$s_5$', '$s_6$', '$s_7$', '$s_8$', '$s_9$', '$s_{10}$', '$s_{11}$', '$s_{12}$', '$s_{13}$', '$s_{14}$', '$s_{15}$'], loc=4)
#plt.legend(['$[s_1 ... s_{9}]$', k, '$[s_{10} ... s_{15}]$', r, loc=4)
#plt.legend([('$s_1$', '$s_{15}$'),('$s_1$', ' ')], loc=2)        
#plt.xticks(xAxis," ")    
#plt.rc('xtick', color='k', labelsize='medium', direction='out')
#ax.set_xticklabels()
ax.tick_params(axis='both', which='major', labelsize=6)
ax.tick_params(axis='both', which='minor', labelsize=6)


legend_elements = [Line2D([0], [0], color='k', lw=.5, label='2 Strategies Ecosystems: $[s_1, s_2, \ldots,s_9]$'),Line2D([0], [0], color='r', lw=.5, label='3 Strategies Ecosystems: $[s_{10}, s_{11}, \ldots,s_{15}]$')]

# Create the figure
#fig, ax = plt.subplots()
ax.legend(handles=legend_elements,  fontsize=6, loc=3)

plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)

plt.show()
fig.savefig('plotInstability.pdf')
plt.close(fig)    # close the figure



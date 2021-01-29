
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
#import numpy as np
#import numpy
import matplotlib.pyplot as plt

import time




def resample(weights):
  n = len(weights)
  indices = []
  C = [0.] + [sum(weights[:i+1]) for i in range(n)]
  u0, j = random(), 0
  for u in [(u0+i)/n for i in range(n)]:
    while u > C[j]:
      j+=1
    indices.append(j-1)
  return indices

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
    
def particlefilterHFTE(deltaPrice, iteration, weights, lambdaEWMA, resampleLambda):
    previousWeights = weights
    likelihood = zeros(15)
    weight = zeros(15)    
    totalWeight = 0
    normalisedWeight = zeros(15)   
    for s in range(0,15):
        likelihood[s] = exp(-abs(deltaPrice-scenariosHT(s,iteration)))        
        totalWeight = totalWeight + likelihood[s]
    for s in range(0,15):
        weight[s] = lambdaEWMA*(likelihood[s]/totalWeight) + (1-lambdaEWMA-resampleLambda)*previousWeights[s] + resampleLambda*1/15
    return weight
            

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


realMarketPrice =  numpy.multiply(s1,1/15)+numpy.multiply(s2,1/15)+numpy.multiply(s3,1/15)+numpy.multiply(s4,1/15)+numpy.multiply(s5,1/15)+numpy.multiply(s6,1/15)+numpy.multiply(s7,1/15)+numpy.multiply(s8,1/15)+numpy.multiply(s9,1/15)+numpy.multiply(s10,1/15)+numpy.multiply(s11,1/15)+numpy.multiply(s12,1/15)+numpy.multiply(s13,1/15)+numpy.multiply(s14,1/15)+numpy.multiply(s15,1/15)

randomSeed = int(time.time())    
np.random.seed(randomSeed)

fig, ax = plt.subplots(6, 1)


weights = [1/15,1/15,1/15,1/15,1/15,1/15,1/15,1/15,1/15,1/15,1/15,1/15,1/15,1/15,1/15]
for i in [0,2,3,5,11,23,47]:
    mu = 0
    sigma = sqrt(i)/10
    x = mu + sigma * np.random.randn()    
    marketObservedPrice[returnArrayPosition(i)] = realMarketPrice[returnArrayPosition(i)] + x
    weights = particlefilterHFTE(marketObservedPrice[returnArrayPosition(i)], i, weights, .33, .33)
    tempIdx = returnArrayPosition(i)

    if tempIdx>0:
        plt.subplot(6, 1, tempIdx)
        plt.bar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],weights) 
        plt.gca().axes.get_yaxis().set_visible(False)        
        if i<47:        
            plt.xticks(weights," ")    
            plt.rc('xtick', color='k', labelsize='large', direction='out')
        
    
plt.show()
fig.savefig('HFTEPFsAll.pdf')
plt.close(fig)    # close the figure



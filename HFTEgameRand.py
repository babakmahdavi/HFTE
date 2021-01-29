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

import numpy as np
import random


X = np.array([[0,0,0,0,0,0,0,0,0],[1,1,1,1,0,1,1,1,1], [0,0,0,0,1,0,0,0,0], [1,1,1,1,1,1,1,1,1],[0,0,0,0,-1,0,0,0,0]])
Y = np.array([ [0], [0],   [1],  [1],   [-1] ])
 
def TF(deltaOI, deltaPrice): 
    if deltaPrice>0:
        order=1 
    elif deltaPrice<0:
        order=-1
    else: 
        order = 0
    return order

def MLR(deltaOI, deltaPrice): 
    if deltaOI + 2*deltaPrice>0:
        order=1 
    elif deltaOI + 2*deltaPrice<0:
        order=-1
    else: 
        order = 0
    return order

def XOR(deltaOI, deltaPrice): 
    if (deltaOI >0) and (deltaPrice>0):
        order=1 
    elif (deltaOI >0) and (deltaPrice<0):
        order=-1
    elif (deltaOI <0) and (deltaPrice>0):
        order=-1        
    elif (deltaOI <0) and (deltaPrice<0):
        order=1
    else: 
        order = 0
    return order

def OB(volumeSell, volumeBuy, LastPrice, order):  
     
    if order == 1:
        #print 'you should buy'
        orderAlreadySet = False
        i = 0
        originalLengthBuy = len(volumeBuy)
        while i < originalLengthBuy:
            #randomNum = 9.99999
            if orderAlreadySet == False and volumeBuy[-1] == 1:         
                volumeBuy.pop(-1)# =randomNum
                #volumeBuy.remove(randomNum)                
                volumeSell = [0] + volumeSell 
                orderAlreadySet = True   
                LastPrice = LastPrice + 1 
            elif orderAlreadySet == False and volumeBuy[-1]== 0:
                if i == originalLengthBuy - 1:
                    volumeBuy[-1] = 1
                    #LastPrice = LastPrice + 0.5*(i+1) 
                else:
                    volumeBuy.pop(-1)
                    volumeSell = [0] + volumeSell    
                    LastPrice = LastPrice + 1
            i=i+1
        if not volumeBuy:  
            #print("in here")
            volumeBuy = [1]        
            #LastPrice = LastPrice + 0.5
                    
    if order == -1:
        orderAlreadySet = False
        i =0
        originalLengthSell = len(volumeSell)    
        #print(volumeSell)
        #pdb.set_trace()
        while i < originalLengthSell:
            if orderAlreadySet == False and volumeSell[0] == 1:
                volumeSell.pop(0)
                volumeBuy = volumeBuy + [0] 
                orderAlreadySet = True   
                LastPrice = LastPrice - 1
            elif orderAlreadySet == False and volumeSell[0] == 0:
                if i == originalLengthSell - 1:
                    volumeSell[0] = 1
                else:
                    volumeSell.pop(0)
                    volumeBuy =  volumeBuy + [0]
                    LastPrice = LastPrice - 1                   
            i=i+1
        if not volumeSell:  
            #print("in here")
            volumeSell = [1]    
            
            j = 0
            dummy = 0
            while j<len(volumeSell):
                dummy = dummy+volumeSell[j]
                j = j +1                
            if dummy == 0:
                volumeSell = []
            if volumeSell == []:
                volumeSell = [0]
                
            j = 0
            dummy = 0
            while j<len(volumeBuy):
                dummy = dummy+volumeBuy[j]
                j = j +1                
            if dummy == 0:
                volumeBuy = []
            if volumeBuy == []:
                volumeBuy = [0]

            #else:
                #volumeSell = [1]
        #print(volumeSell)            
        #if not volumeSell:  
            #print("in here")
            #volumeSell = [1]

    #if order == 0:
        #print('you should wait')    

    #if order == 0:
        #print('you should wait')    
        
    #for element in (volumeBuy):
        #print element         
    #print(LastPrice)        
    #for element in (volumeSell):
        #print element         
    return volumeSell, volumeBuy, LastPrice
        




class Order:
    def __init__(self, key, robot, priceIn, priceOut, signal, pnl, closed):
        self.k = key
        self.i = priceIn
        self.o = priceOut
        self.s = signal
        self.c = closed
        self.p = pnl      
        self.r = robot     

    def __init__(self, key):
        self.k = key
        self.i = 0
        self.o = 0
        self.s = 0
        self.c = True
        self.p = 0      
        self.r = 'none'              
        
    def pnl(self, key, priceIn, priceOut, signal):
        self.s = signal*(priceOut-priceIn)
        
    def priceOut(self):
        return self.o
    
    
def oneslistmaker(n):
    listofzeros = [1] * n
    return listofzeros    

NumberOfOrders = 47     ####################
orderList = [ Order(i) for i in range(NumberOfOrders)]

# seed for the OB
deltaOI = 1 
deltaPrice = 1


OBbuySide = oneslistmaker(NumberOfOrders)
OBsellSide = oneslistmaker(NumberOfOrders)


oldOI = sum(OBbuySide)-sum(OBsellSide)
oldLastPrice = 100.0

#Initialise OB
volumeSell, volumeBuy, LastPrice = OB(OBsellSide,OBbuySide,oldLastPrice,0)


numberOfSimulation = 100000
PnLStrat1 = [0]
PnLStrat2 = [0]
PnLStrat3 = [0]
outputPrice1 = [0]
outputPrice2 = [0]
outputPrice3 = [0]
inputPrice1 = [0]
inputPrice2 = [0]
inputPrice3 = [0]
signal1 = [0]
signal2 = [0]
signal3 = [0]
itStrat1 = 0
itStrat2 = 0
itStrat3 = 0

for l in range (0,numberOfSimulation):
    for i in range(1, NumberOfOrders):        
        myRandomNumber = random.randint(0,100)
        #print ("Iteration %d a" % (i))
        if myRandomNumber < 33:
            #print("in 1st group myRandomNumber is ", myRandomNumber)
            signal1.append(TF(deltaOI, deltaPrice))  ####################
            signal = signal1[itStrat1]
            volumeSell, volumeBuy, LastPrice = OB(volumeSell,volumeBuy,LastPrice,signal)
            PnLStrat1.append(0)
            #outputPrice1.append(LastPrice) #will have to update the profit at the end 
            inputPrice1.append(LastPrice)
            itStrat1 = itStrat1 + 1
        elif myRandomNumber > 33 and myRandomNumber < 66:
            #print("in 2nd group myRandomNumber is ", myRandomNumber)    
            signal2.append(MLR(deltaOI, deltaPrice))  ####################
            signal = signal2[itStrat2]
            volumeSell, volumeBuy, LastPrice = OB(volumeSell,volumeBuy,LastPrice,signal)
            PnLStrat2.append(0)
            #outputPrice2.append(LastPrice) #will have to update the profit at the end 
            inputPrice2.append(LastPrice)    
            itStrat2 = itStrat2 + 1
        else:
            #print("in 3rd group myRandomNumber is ", myRandomNumber)  
            signal3.append(XOR(deltaOI, deltaPrice))  ####################
            signal = signal3[itStrat3]
            volumeSell, volumeBuy, LastPrice = OB(volumeSell,volumeBuy,LastPrice,signal)
            PnLStrat3.append(0)
            #outputPrice3.append(LastPrice) #will have to update the profit at the end 
            inputPrice3.append(LastPrice)
            itStrat3 = itStrat3 + 1

        #volumeSell, volumeBuy, LastPrice = OB(volumeSell,volumeBuy,LastPrice,signal)
        deltaOI = oldOI + sum(volumeBuy)-sum(volumeSell)
        deltaPrice = LastPrice - oldLastPrice 
        oldLastPrice = LastPrice
        #print(volumeBuy)
        #print(LastPrice)
        #print(volumeSell)
        #print(signal)
        #for element in (volumeBuy):
            #print(element)         
        #print(LastPrice)        
        #for element in (volumeSell):
            #print(element)   
    tempPnL1 = 0    
    for k in range(1, itStrat1):  
        tempPnL1 = tempPnL1 + signal1[k]*(LastPrice-inputPrice1[k]) 
    PnLStrat1[l] = tempPnL1  
    tempPnL2 = 0    
    for k in range(1, itStrat2):  
        tempPnL2 = tempPnL2 + signal2[k]*(LastPrice-inputPrice2[k]) 
    PnLStrat2[l] = tempPnL2  
    tempPnL3 = 0            
    for k in range(1, itStrat3):  
        tempPnL3 = tempPnL3 + signal3[k]*(LastPrice-inputPrice3[k]) 
    PnLStrat3[l] = tempPnL3   
    #print(PnLStrat3)
    #print(inputPrice1)
    #print(LastPrice)
    #print(inputPrice1[2])
    outputPrice1 = [0]
    outputPrice2 = [0]
    outputPrice3 = [0]
    inputPrice1 = [0]
    inputPrice2 = [0]
    inputPrice3 = [0]
    signal1 = [0]
    signal2 = [0]
    signal3 = [0]
    itStrat1 = 0
    itStrat2 = 0
    itStrat3 = 0



#print('PnLStrat1 average is ', np.mean(PnLStrat1))
#print('PnLStrat2 average is ', np.mean(PnLStrat2))    
#print('PnLStrat3 average is ', np.mean(PnLStrat3))

print('PnLStrat1 sum is ', sum(PnLStrat1))
print('PnLStrat2 sum is ', sum(PnLStrat2))    
print('PnLStrat3 sum is ', sum(PnLStrat3))
#print(PnLStrat1)
#print(PnLStrat2)    
#print(PnLStrat3)

        


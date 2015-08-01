# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 08:20:27 2015

@author: andrew
"""

from numpy import *

# Function for defining the inlet velocity
def GetNodes(model_part,dim,pos):
    NodeSet = []
    for node in model_part.NodeIterators():
        if(absolute(node.coordinates[dim]-pos)<1*10**-4):
            NodeSet.append(node)
    return NodeSet
        

class InletVelocityFunc:
    def __init__():
        return
        
    def ApplyInletVelocity(self):
        return
        
class ParabolicInletVelocity(InletVelocityFunc):
    def __init__(inletNodes,vMax):
        self.inletNodes = inletNodes
        self.vMax = vMax
        
        yMin = inletNodes[0].coordinates[1]
        yMax = yMin
        for node in self.inletNodes:
            if(node.coordinates[1] > yMax):
                yMax = node.coordinates[1]
            elif(node.coordinates[1] < yMin):
                yMin = node.coordinates[1]
                    
        
        self.yMax = yMax
        self.yMin = yMin
        return
        
    def ApplyInletVelocity(self):
                
        for node in self.inletNodes:
            #X = node.coordinates[0]
            Y = node.coordinates[1]
            #Z = node.coordinates[2]
            
            U = absolute((Y-Ymax)(Y-Ymin)) * vMax
            
            node.SetSolutionStepValue(VELOCITY_X, U)
        
        return
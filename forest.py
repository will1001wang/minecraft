# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:44 2020

@author: SCE
"""

from mcpi.minecraft import Minecraft

mc=Minecraft.create()
def plantTree(x,y,z):
    mc.setBlocks(x+1,y+3,z+1,x-1,y+5,z-1,22)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
x,y,z=mc.player.getTilePos()
for i in range(20):
    for j in range(20):
        plantTree(x+i*5,y,z+j*5)
        
    

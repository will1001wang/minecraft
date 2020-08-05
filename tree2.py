# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:44 2020

@author: SCE
"""

from mcpi.minecraft import Minecraft

mc=Minecraft.create()
def plantTree(x,y,z):
    mc.setBlocks(x+1,y+3,z+1,x-1,y+6,z-1,22)
    mc.setBlocks(x,y,z,x,y+8,z,1)
    
x,y,z=mc.player.getTilePos()
plantTree(x,y,z)

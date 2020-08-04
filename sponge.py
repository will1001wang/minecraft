# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:44 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
w
mc=Minecraft.create()
x,y,z=mc.player.getTilePos() 
  
a=0
while a<10:
    mc.setBlocks(x-10,y-1,z,x+10,y-10,z,19)
    z=z+6
    a=a+1
    
  
    


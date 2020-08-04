# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:44 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
import random
a=0

while a<50:
    color=random.randrange(9) 
    x,y,z=mc.player.getTilePos() 
    mc.setBlock(x,y,z,38,color)
    time.sleep(0.1)    
    a+=1
    


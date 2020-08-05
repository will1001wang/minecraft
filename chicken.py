# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:44 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import random 
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
while True:
    y=pos.y+30
    x=pos.x+random.uniform(-20, 20)
    z=pos.z+random.uniform(-20, 20)
    mc.spawnEntity(x,y,z,93)
    time.sleep(0.3)
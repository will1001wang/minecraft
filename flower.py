# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:44 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,38)
    time.sleep(0.1)    

    


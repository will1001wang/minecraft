# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:44 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
time.sleep(5)


mc.setBlocks(x-69,y-1,z-69,x+69,y-1,z+69,0)

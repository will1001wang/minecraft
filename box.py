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


mc.setBlock(x-0.5,y,z,56)
mc.setBlock(x+0.5,y,z,56)
mc.setBlock(x,y,z-0.5,56)
mc.setBlock(x,y,z+0.5,56)
mc.setBlock(x+0.5,y,z-0.5,56)
mc.setBlock(x+0.5,y,z+0.5,56)
mc.setBlock(x-0.5,y,z+0.5,56)
mc.setBlock(x-0.5,y,z-0.5,56)    
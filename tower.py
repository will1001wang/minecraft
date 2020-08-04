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
mc.setBlock(x,y,z,56)
mc.setBlock(x,y+1,z,56)
mc.setBlock(x,y+2,z,56)
mc.setBlock(x,y+3,z,56)
mc.setBlock(x,y+4,z,56)
mc.setBlock(x,y+5,z,56)
mc.setBlock(x,y+6,z,56)
mc.setBlock(x,y+7,z,56)
mc.setBlock(x,y+8,z,56)
mc.setBlock(x,y+9,z,56)    
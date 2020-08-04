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
width=5
hight=10
length=5
block=89
air=0
mc.setBlocks(x,y,z,x+width,y+hight,z+length,block)
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+hight-1,z+length-1,air)
    


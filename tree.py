# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:44 2020

@author: SCE
"""

from mcpi.minecraft import Minecraft

mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x+1,y+3,z+1,x-1,y+6,z-1,22)
mc.setBlocks(x,y+5,z,x,y+8,z,1)
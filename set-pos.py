# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:44 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
 
mc=Minecraft.create()
x=260
y=-280
z=-100
mc.player.setTilePos(x,y,z)   
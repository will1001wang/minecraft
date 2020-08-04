# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:44 2020

@author: SCE
"""

import random
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
time.sleep(5)

color=random.randrange(16)
mc.setBlocks(x-15,y-1,z-15,x+15,y-1,z+15,95,color)

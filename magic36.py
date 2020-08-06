# 蠕蟲

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

number = 1 # 一次生成的數量

for i in range(8):
    for j in range(number):
        mc.spawnEntity(x, y, z, 60) # 蠹魚
    
    number = number * 2
    
    mc.postToChat("這次生成了" + str(number) + "隻蠹魚")
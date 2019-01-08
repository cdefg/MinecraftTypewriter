#!/usr/bin/python3

"""
Minecraft Typewriter by wly
"""
"""
All Characters consisted of "m# are made from Linux package "toilet" 
"""

import mcpi.minecraft as mc
import mcpi.block     as block
import os

width   = 7
marklist = [block.AIR.id, block.WOOL_RED.id, block.WOOL_ORANGE.id, block.WOOL_YELLOW.id]
markFileList = os.listdir("chars")
marks   = ' #"m'
print(marks)
distance = 20
height   = 12
displacement = 40


class TypeWriter:
	def __init__(self, pos):
		self.x, self.y, self.z = pos.x, pos.y, pos.z
		self.pos = (self.x - distance, self.y + height, self.z + displacement)

	#draw a single letter
	def printLetter(self, letter, anchor):
		letter = letter if letter in markFileList else "Blank"
		os.chdir("chars")
		with open(letter, "r") as f:
			pixLines = f.read().splitlines()

			for i in range(len(pixLines)):
				for j in range(len(pixLines[i])):
					pixBlock = marklist[marks.index(pixLines[i][j])]
					M.setBlock(anchor[0], anchor[1]-i, anchor[2]-j, pixBlock)
		os.chdir('..')
		f.close()

	#draw a string at a time
	def printWord(self, content):
		startpoint = self.pos

		for i in range(len(content)):
			_anchor = (startpoint[0], startpoint[1], startpoint[2]-width*i) 
			self.printLetter(content[i], _anchor)

		self.pos = (startpoint[0], startpoint[1], startpoint[2]+width*len(content))




if __name__ == '__main__':
	#define words to print
	words2print = "Welcome to Minecraft"

	#initialize minecraft service in background
	global M
	M = mc.Minecraft.create()

	#create a TypeWriter instance

	T = TypeWriter(M.player.getPos())

	#type words

	T.printWord(words2print)


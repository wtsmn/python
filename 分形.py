# -*- coding : utf-8 -*-
# Creation Date : 2019/11/4

from turtle import *
len = 5
angle = 90

def run (path):
	for symbol in path :
		if symbol == "f":
			forward (len)
		elif symbol == "-":
			left (angle)
		elif symbol == "+":
			right(angle)

def apply_rule(path):
	rule = "f-f+f+ff-f-f+f"
	return path.replace("f",rule)

path = "f-f-f-f"
path = apply_rule(path)
path = apply_rule(path)
path = apply_rule(path)


run (path)

speed(0)

exitonclick()
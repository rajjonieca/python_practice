import os
import sys

heroes = ["Saitama", "Mumen Rider", "Genos", "Torndado"]
print ("Original: "+str(heroes))
print("Popped: "+str(heroes.pop(1)))
print ("Popped: "+str(heroes))
print("-----------------------------------------------------------")
champions = ["Slardar", "Traxex", "Wraith King", "Sniper"]
print ("Original: "+str(champions))
print("Removed:"+str(champions.remove("Traxex")))
print ("Removed: "+str(champions))
print("-----------------------------------------------------------")
pirates = ["Monkey D. Luffy", "Eustass Kid", "Trafalgaw D. Law", "Basil Hawkins"]
print ("Orginal: "+str(pirates))
del(pirates[2])
print ("Deleted: "+str(pirates))

#modifying lists in a function

print("Length: "+str(len(heroes)))
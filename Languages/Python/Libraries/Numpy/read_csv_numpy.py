import numpy

"""
Read in csv with type assumption
"""
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",")
print(type(world_alcohol))

"""
read in csv with defined type and skipping headers
"""
world_alcohol = numpy.genfromtxt("world_alcohol.csv", dtype="U75", skip_header=1, delimiter=",")
print(world_alcohol)
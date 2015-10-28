#!/usr/bin/env python

# Author: Jan Schlenker
from tsp_vns_solver import main

# triesPerNeighboourhoodSize
for i in (2, 4, 8, 16, 32, 64):
    # maxNeighbourhoods
    for j in (2, 4, 8, 16, 32, 64):
        # how often same parameters:
        for k in xrange(3):
            main(1000, j, i)
    

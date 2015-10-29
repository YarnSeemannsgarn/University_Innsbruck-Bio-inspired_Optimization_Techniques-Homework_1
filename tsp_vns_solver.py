#!/usr/bin/env python

# Author: Jan Schlenker
from math import sqrt, pow as mathpow #necessary, because pow is built-in
from random import shuffle, randint
from tsplib_parser import parse
from sys import argv
from time import clock
from itertools import tee, izip

# Pairwise iterator for tsp distance calculator
# From: https://docs.python.org/2/library/itertools.html#recipes
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def calculateCityDistance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return sqrt(mathpow(x1-x2, 2) + mathpow(y1-y2, 2))

def calculateTSPDistance(cities):
    totalDistance = 0
    for city1, city2 in pairwise(cities):
        totalDistance += calculateCityDistance(city1, city2)
    return totalDistance

# Exchange neighbourhoods until better solution is found or max Neighbourhoods
def variableNeighbourhoodSearch(cities, maxNeighbourhoods, triesPerNeighbourhoodSize, bestValue):
    cityCount = len(cities) - 1
    initialBestValue = bestValue
    initialCities = list(cities)
    for i in xrange(maxNeighbourhoods):
        for j in xrange(triesPerNeighbourhoodSize):
            copiedCities = list(initialCities)
            for k in xrange(i+1):
                pos1 = randint(0, cityCount)
                pos2 = randint(0, cityCount)
                while(pos1 == pos2):
                    pos2 = randint(0, cityCount)
                
                tmpCity = copiedCities[pos1]
                copiedCities.pop(pos1)
                copiedCities.insert(pos2-1, tmpCity)
                newValue = calculateTSPDistance(copiedCities)
                if newValue < bestValue:
                    cities = list(copiedCities)
                    bestValue = newValue
        if(bestValue < initialBestValue):
            return (cities, bestValue)
    return (cities, bestValue)
        
# Nearest Neigbhour for initial solution
def nearestNeighbour(cities):
    unvisited = list(cities)
    city = unvisited.pop()
    nearestNeighbourCities = []
    nearestNeighbourCities.append(city)
    while(unvisited):
        minDistance = None
        cityNext = None
        for cityTmp in unvisited:
            distance = calculateCityDistance(city, cityTmp)
            if(minDistance == None or minDistance > distance):
                cityNext = cityTmp
        unvisited.remove(cityNext)
        nearestNeighbourCities.append(cityNext)
    return nearestNeighbourCities
   
def main(iterations, maxNeighbourhoods, triesPerNeighbourhoodSize):
    # Initialise cities:
    tspFile = open("./tsp225.tsp")
    cities = parse(tspFile)
    start = clock()

    # Get initial city route value from nearest neighbour algorithm
    cities = nearestNeighbour(cities)
    bestValue = calculateTSPDistance(cities)

    # Try to find better solutions
    for i in xrange(iterations):
        cities, bestValue = variableNeighbourhoodSearch(cities, maxNeighbourhoods, triesPerNeighbourhoodSize, bestValue)
        bestValue = calculateTSPDistance(cities)
        currentTime = clock()
        time = currentTime - start
        print 'iterations: {0}/{1}, value: {2}, time: {3}s\r'.format(i, iterations, bestValue, time),
    
    end = clock()
    time = end - start
    print "Best value for iterations: {0}, maxNeighbourhoods: {1}, triesPerNeighbourhoodSize: {2} ({3}s): {4}".format(iterations, maxNeighbourhoods, triesPerNeighbourhoodSize, time, bestValue)

if __name__ == "__main__":
    if(len(argv) != 4):
        print "Usage {0} <iterations> <maxNeighbourhoods> <triesPerNeighbourhoodSize>".format(argv[0])
    else:
        main(int(argv[1]), int(argv[2]), int(argv[3]))

#Author: Jan Schlenker
from math import sqrt, pow as mathpow #necessary, because pow is built-in
from random import shuffle, randint
from tsplib_parser import parse
from sys import argv

def calculateTSPDistance(cities):
    totalDistance = 0
    for i, city in enumerate(cities[:-1]):
        x1, y1 = city
        x2, y2 = cities[i+1]
        totalDistance += sqrt(mathpow(x1-x2, 2) + mathpow(y1-y2, 2))
    return totalDistance


def changeNeighbourhoods(cities, *args):
    cityCount = len(cities) - 1

    # Exchange two positions
    #pos1 = randint(0, cityCount)
    #pos2 = randint(0, cityCount)
    #while(pos1 == pos2):
        #pos2 = randint(0, cityCount)

    #tmpCity = cities[pos1]
    #cities[pos1] = cities[pos2]
    #cities[pos2] = tmpCity
        
    # Insert random choice somewhere else
    #pos1 = randint(0, cityCount)
    #pos2 = randint(0, cityCount)
    #while(pos1 == pos2):
        #pos2 = randint(0, cityCount)

    #tmpCity = cities[pos1]
    #cities.pop(pos1)
    #cities.insert(pos2-1, tmpCity)

    # Exchange multiple until better solution is found
    positions = args[0]
    tries = args[1]
    multiplier = args[2]
    bestValue = args[3]
    initialCity = list(cities)       
    for i in xrange(multiplier):
        positions = positions * 2
        for j in xrange(tries):
            copiedCities = list(initialCity)       
            for k in xrange(positions/2):
                pos1 = randint(0, cityCount)
                pos2 = randint(0, cityCount)
                while(pos1 == pos2):
                    pos2 = randint(0, cityCount)

                    tmpCity = copiedCities[pos1]
                    copiedCities[pos1] = copiedCities[pos2]
                    copiedCities[pos2] = tmpCity
                    newValue = calculateTSPDistance(copiedCities)
                    if newValue < bestValue:
                        cities = list(copiedCities)
                        bestValue = newValue
                    
        if calculateTSPDistance(cities) < bestValue:
            return

def main(iterations):
    # Initialise cities:
    tspFile = open("./tsp225.tsp")
    cities = parse(tspFile)

    # Get initial city route value
    shuffle(cities) #Complexity O(n) --> http://programmers.stackexchange.com/questions/215737/how-python-random-shuffle-works
    bestValue = calculateTSPDistance(cities)
    
    # Try to find better solutions
    for i in xrange(int(iterations)):
        copiedCities = list(cities)
        changeNeighbourhoods(copiedCities, 4, 4, 4, bestValue)
        newValue = calculateTSPDistance(copiedCities)
        if newValue < bestValue:
            bestValue = newValue
            cities = copiedCities
        print '{0}/{1} - value: {2}\r'.format(i, iterations, bestValue),
    
    print "Best value for {0} iterations: {1}".format(iterations, bestValue)

if __name__ == "__main__":
    main(argv[1])

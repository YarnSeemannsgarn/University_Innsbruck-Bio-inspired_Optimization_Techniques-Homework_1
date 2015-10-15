#Author: Jan Schlenker
from math import sqrt, pow as mathpow #necessary, because pow is built-in
from random import shuffle

def calculateTSPDistance(cities):
    totalDistance = 0
    for i, city in enumerate(cities[:-1]):
        x1, y1 = globalCities[city]
        x2, y2 = globalCities[cities[i+1]]
        totalDistance += sqrt(mathpow(x1-x2), mathpow(y1-y2))
    return totalDistance

def getNeighbourhoods():
    

def main:
    #TODO: Init global city list

    # Get initial city
    shuffledCities = shuffle(cities) #Complexity O(n) --> http://programmers.stackexchange.com/questions/215737/how-python-random-shuffle-works
    initialValue = calculateTSPDistance(shuffledCities)

if __name__ == "__main__":
    main()

import A_promptFormatter, C_talkToQWEN
import numpy as np

def getDimensions(grid):

    nRows, nCols = grid.shape

    return nRows, nCols

def getColorFrequencies(grid):

    colors, counts = np.unique(grid, return_counts=True)

    colorFrequencyDictionary = dict(zip(colors, counts))

    return colorFrequencyDictionary

def printColorAppearance(colorFrequencyDictionary):

    # print(colorFrequencyDictionary.items())

    sortedTuples = sorted(colorFrequencyDictionary.items(), key= lambda item: item[1], reverse=True)

    for color, frequency in sortedTuples:
        print(f"Color: {color} Frequency: {frequency}")







grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 2, 2],
    [0, 0, 0, 0, 0]
]

# grid = [
#     [0, 3, 0, 0, 0, 5],
#     [1, 1, 1, 0, 0, 0],
#     [0, 1, 1, 0, 0, 3],
#     [4, 1, 0, 2, 2, 2],
#     [0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 8],
#     [0, 0, 0, 0, 0, 0]
# ]


grid = np.array(grid)

nRows, nCols = getDimensions(grid)

print(nRows, nCols)

colorFrequencyDictionary = getColorFrequencies(grid)

print(colorFrequencyDictionary)

printColorAppearance(colorFrequencyDictionary)
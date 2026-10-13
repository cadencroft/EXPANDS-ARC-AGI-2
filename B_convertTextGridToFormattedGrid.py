
import sys

def getTextGrid():
    print("Paste your grid, then press Enter on an empty line:")

    lines = []

    while True:
        line = input()

        if not line.strip():
            break

        lines.append(line)

    return "\n".join(lines)


def convertTextGridToFormattedArray(textGrid):
    grid = []

    for line in textGrid.strip().splitlines():
        row = [int(num) for num in line.split()]
        grid.append(row)

    return grid


textGrid = getTextGrid()

arrayGrid = convertTextGridToFormattedArray(textGrid)

print(arrayGrid)
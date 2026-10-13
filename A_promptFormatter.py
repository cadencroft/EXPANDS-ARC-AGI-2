import json

def loadJSONFile(file):

    with open(file, "r") as f:
        data = json.load(f)

        return data

def loadTask(index, tasks):

    taskIDs = list(tasks)           # Gets the taskID of the desired index
    return taskIDs[index], tasks[taskIDs[index]]    # Gets the content of the respective taskID


def buildPrompt(taskData):

    prompt = ("You are an AI agent with the goal of solving Abstraction and Reasoning Corpus for Artificial General Intelligence (ARC-AGI) puzzles.\n\n"
    "You will be provided with examples. Each example will have an input puzzle and an output puzzle. The output puzzle is found by applying "
    "some transformation onto the input problem. You will also be provided a test which only contains the input. You will NOT be provided the test output.\n\n"
    "Your job is to discover the pattern from the examples and apply it to the test input to produce the correct test output. " \
    "Each puzzle is in the form of a 2D matrix. The matrix contains the digits 0-9 which all represent colors. The colors are as followed: " 
    "0 is Black, 1 is Blue, 2 is Red, 3 is Green, 4 is Yellow, 5 is Gray, 6 is Magenta, 7 is Orange, 8 is Cyan, 9 is Maroon. " 
    "You must return your guess for the test output with only the digits 0-9 in a matrix. You must return the same grid in 2 different formats. For the first one, do not include any brackets, commas, or other symbols, and make sure your output is nicely spaced and formatted. For the second one, format it as a 2D array.\n\n"
    "The provided data is shown below. Use only the provided data while making your test output.\n\n" 
    )

    trainExamples = taskData["train"]               # This contains an array of each training example.

    for exNum in range(len(trainExamples)):

        exInput  = trainExamples[exNum]["input"]    # This contains the input of the example
        exOutput = trainExamples[exNum]["output"]   # This contains the output of the example

        prompt += f"--Example {exNum}--\n\n"

        prompt += "Input:\n\n"
        prompt += formatGrid(exInput) + "\n"

        prompt += "Output:\n\n"
        prompt += formatGrid(exOutput) + "\n\n\n\n"


    testInput = taskData["test"][0]["input"]        # This contains the input of the test

    prompt += "--Test--\n\n"

    prompt += "Input:\n\n"
    prompt += formatGrid(testInput)

    return prompt

def formatGrid(grid):

    gridText = ""

    for row in grid:
        for num in row:
            gridText += str(num) + " "
        gridText += "\n"

    return gridText











import json

def loadJSONFile(file):

    with open(file, "r") as f:
        data = json.load(f)

        return data

def loadTask(index, tasks):

    taskIDs = list(tasks)           # Gets the taskID of the desired index
    return taskIDs[index], tasks[taskIDs[index]]    # Gets the content of the respective taskID


def buildPrompt(taskData):

    prompt = (
        "Solve the ARC-AGI puzzle by identifying the transformation "
        "in the training examples and applying it to the test input.\n\n"

        "Each puzzle is a 2D grid of digits representing colors:\n"
        "0=Black, 1=Blue, 2=Red, 3=Green, 4=Yellow, "
        "5=Gray, 6=Magenta, 7=Orange, 8=Cyan, 9=Maroon.\n\n"

        "Use only the provided examples.\n\n"

        "IMPORTANT OUTPUT FORMAT:\n"
        "Return ONLY a valid Python 2D list of integers.\n"
        "The outer list must contain a separate list for EVERY row.\n"
        "Each row must have its own square brackets.\n"
        "Separate every integer with a comma.\n"
        "Separate every row with a comma.\n"
        "Do not flatten the grid into a single list.\n"
        "Do not include explanations or Markdown.\n\n"

        "Example of the REQUIRED format:\n"
        "[[1, 2, 3],\n"
        " [4, 5, 6],\n"
        " [7, 8, 9]]\n\n"

        "Training examples:\n\n"
    )

    trainExamples = taskData["train"]

    for exNum in range(len(trainExamples)):

        exInput = trainExamples[exNum]["input"]
        exOutput = trainExamples[exNum]["output"]

        prompt += f"Example {exNum}:\n"
        prompt += "Input:\n" + formatGrid(exInput) + "\n"
        prompt += "Output:\n" + formatGrid(exOutput) + "\n\n"

    testInput = taskData["test"][0]["input"]

    prompt += "Test Input:\n" + formatGrid(testInput)

    return prompt

def formatGrid(grid):

    gridText = ""

    for row in grid:
        for num in row:
            gridText += str(num) + " "
        gridText += "\n"

    return gridText











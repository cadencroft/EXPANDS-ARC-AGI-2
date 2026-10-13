import A_promptFormatter, C_talkToQWEN


tasks = A_promptFormatter.loadJSONFile("--arc-agi_training_challenges.json")

# print(taskID, taskData)

startTaskNumber = 0
endTaskNumber = 0


for i in range(startTaskNumber, endTaskNumber+1):

    print(f"\n\n===============================\n             TASK {i}\n===============================\n\n")
    
    print("(Begin prompt)\n\n")

    taskID, taskData = A_promptFormatter.loadTask(i, tasks)

    prompt = A_promptFormatter.buildPrompt(taskData)

    print(prompt)

    print("\n\n(End prompt)\n\n")

    print("Sending prompt to Local LLM...")

    response, responseMetadata = C_talkToQWEN.sendPrompt(prompt)

    print("\n\n(Begin response)\n\n")

    print(response)

    print("\n\n(End response)\n\n")

    print("(Begin response metadata)\n\n")

    print("Total:", responseMetadata["total"], "seconds")
    print("Loading:", responseMetadata["loading"], "seconds")
    print("Prompt processing:", responseMetadata["promptProcessing"], "seconds")
    print("Generation:", responseMetadata["generation"], "seconds")

    print("\n\n(End response metadata)\n\n")


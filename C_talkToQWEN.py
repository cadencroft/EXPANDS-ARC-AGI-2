import ollama

def sendPrompt(prompt, model="qwen3.8:27b"):

    response = ollama.generate(model, prompt)

    responseMetadata = {
        "total": response.total_duration / 1e9,
        "loading": response.load_duration / 1e9,
        "promptProcessing": response.prompt_eval_duration / 1e9,
        "generation": response.eval_duration / 1e9
    }

    return response.response, responseMetadata
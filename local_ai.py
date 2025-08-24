from gpt4all import GPT4All

model = GPT4All("mistral-7b-openorca.Q4_0.gguf", device='cpu')

with model.chat_session():
    while True:
        prompt = input("\nEnter your prompt (or 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        response = model.generate(prompt, max_tokens=200)
        print("\nAI Response:\n", response)

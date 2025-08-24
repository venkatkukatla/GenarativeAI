from gpt4all import GPT4All

model_name = "mistral-7b-openorca.Q4_0.gguf"

try:
    model = GPT4All(model_name, device='cpu', allow_download=True)
    print(f"✅ Model loaded: {model_name}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    print("Switching to safe CPU mode...")
    model = GPT4All(model_name, device='cpu')

with model.chat_session():
    while True:
        prompt = input("\nEnter your prompt (or 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        try:
            response = model.generate(prompt, max_tokens=200)
            print("\nAI Response:\n", response)
        except Exception as e:
            print(f"❌ Error generating response: {e}")

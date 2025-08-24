✅ 1. Update System & Install Python

Open terminal and run:

sudo apt update && sudo apt upgrade -y

# Install Python 3 and venv
sudo apt install python3 python3-venv python3-pip -y


Check version:

python3 --version
pip3 --version


(Ensure Python ≥ 3.10)

✅ 2. Create Virtual Environment

python3 -m venv ai-env
source ai-env/bin/activate


You should see (ai-env) in your terminal.

✅ 3. Install GPT4All
pip install --upgrade pip
pip install gpt4all


Optional (for better performance):

pip install torch (Its take time to install)

✅ 4. Write Python Code

Create local_ai.py:

from gpt4all import GPT4All

model = GPT4All("mistral-7b-openorca.Q4_0.gguf", device='cpu')

with model.chat_session():
    while True:
        prompt = input("\nEnter your prompt (or 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        response = model.generate(prompt, max_tokens=200)
        print("\nAI Response:\n", response)


✅ 5. Run the Script

python local_ai.py


First run will download the model (~4GB), then answer offline.

✅ 6. Try DevOps Prompts

Examples:

Generate Kubernetes Deployment YAML for Nginx

Write a Jenkins pipeline for building a Java app

Create Terraform code for an AWS EC2 instance

Write an Ansible playbook to install Docker

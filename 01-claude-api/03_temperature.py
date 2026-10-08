"""Temperature: controls how predictable or creative Claude's answers are.

- Low (0.0): more consistent and deterministic -> facts, extraction, classification
- High (1.0): more variety -> brainstorming, creative writing
Temperature changes probabilities; it doesn't guarantee different results.
"""
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-haiku-5-5"


# --- Helper functions ---

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text


# --- Testing temperature effects ---

prompt = "Generate a one sentence movie idea. Reply with the sentence only."

for temperature in [0.0, 1.0]:
    print(f"=== Temperature {temperature} ===")
    # Ask 3 times with the same prompt to compare the variety
    for i in range(3):
        messages = []
        add_user_message(messages, prompt)
        print(f"{i + 1}. {chat(messages, temperature=temperature)}")
    print()

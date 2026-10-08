"""System prompts: guide how Claude responds by giving it a role.

The `system` parameter is optional, but the API doesn't accept
system=None, so we only add it to the request when one is provided.
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


def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text


# --- Seeing the difference ---

question = "How do I solve 5x + 2 = 3x - 4 for x?"

system = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

# Without a system prompt: Claude gives the full solution
messages = []
add_user_message(messages, question)
print("=== WITHOUT system prompt ===")
print(chat(messages))

# With the math tutor system prompt: Claude guides with questions
messages = []
add_user_message(messages, question)
print("\n=== WITH system prompt (math tutor) ===")
print(chat(messages, system=system))

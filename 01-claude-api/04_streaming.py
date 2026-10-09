"""Streaming: show Claude's response as it is generated, chunk by chunk.

- stream.text_stream yields only the text chunks (ready to display)
- stream.get_final_message() returns the complete message once streaming
  is done, so we can save it to the history (or a database)
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


def chat_stream(messages, system=None, temperature=1.0):
    """Print the response in real time and return the full message."""
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }

    if system:
        params["system"] = system

    with client.messages.stream(**params) as stream:
        for text in stream.text_stream:
            # Send each chunk to the user (here: the terminal)
            print(text, end="", flush=True)
        print()

        # Get the complete message to store it
        final_message = stream.get_final_message()

    return final_message


# --- Putting it all together ---

messages = []
add_user_message(messages, "Write a short paragraph explaining what an API is.")

final_message = chat_stream(messages)

# The full text, ready to keep the conversation going
answer = final_message.content[0].text
add_assistant_message(messages, answer)

# Extra info you'd store in a database
print("\n--- Final message info ---")
print("Stop reason:", final_message.stop_reason)
print("Input tokens:", final_message.usage.input_tokens)
print("Output tokens:", final_message.usage.output_tokens)

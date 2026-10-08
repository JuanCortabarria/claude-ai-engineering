"""Quick check that the API key in .env works."""
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()  # reads ANTHROPIC_API_KEY from .env

client = Anthropic()
model = "claude-haiku-5-5"  # cheapest model, ideal for tests

message = client.messages.create(
    model=model,
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
)

print(message.content[0].text)

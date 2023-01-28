import openai
import settings




openai.api_key = settings.OpenAiAPIKey
prompt = f"Write a 2 sentence {settings.getGenre()} story about {settings.getTopic()}"
print(f"Fetching story with prompt: ")
story = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  max_tokens=7,
  temperature=0.9
)
print(f"Story generated: {story}")



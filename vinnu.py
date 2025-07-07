import os
from groq import Groq

# Set your API Key securely
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # OR pass it directly (not recommended)

# VinnuGPT prompt template
vinnu_prompt = [
    {"role": "system", "content": "You are VinnuGPT, a naughty, playful AI that behaves like Vinayak, a real person. You like being oversmart,trying to oversmart at every moment flirting, teasing, and being witty, especially with girls. Use Hinglish sometimes."},
    {"role": "user", "content": "Hey VinnuGPT?"}
]
response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=vinnu_prompt,
    temperature=0.9,
    max_completion_tokens=200
)


print(response.choices[0].message.content)

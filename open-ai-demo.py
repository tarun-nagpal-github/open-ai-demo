import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # Add your API Key in the Env
)

# Prompt user for input
user_input = input("Enter your message for AI: ")

# Send the user input to OpenAI
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_input,
        }
    ],
    model="gpt-4o",
)

# Print the AI response
print("\nAI Response:")
print(chat_completion.choices[0].message.content)

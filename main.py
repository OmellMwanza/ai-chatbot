import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()  # Load environment variables from .env file

messages = []

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)

def completion(message):
    global messages
    
    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",
    )

    # print(chat_completion)
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    
    messages.append(message)
    print(f"Omell: {message['content']}")

if __name__ == "__main__":
    print(f"Omell: Hi I am Omell, how can I help you today?\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question) 
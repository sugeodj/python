import openai

openai.api_key = "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"

def chat_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

def chat_with_davinci(prompt, model="davinci"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

user_prompt = "Write a dinner recipe for the following ingredients: flour, milk, butter, chicken, tomato, capsicum, onion "
chatbot_response = chat_with_davinci(user_prompt)
print(chatbot_response)
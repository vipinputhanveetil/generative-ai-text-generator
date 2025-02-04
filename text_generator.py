from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="your-api-key-here")

def generate_text(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Use GPT-3.5 Turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=100,  # Limit the response length
        temperature=0.7,  # Controls creativity (0 = deterministic, 1 = creative)
    )
    return response.choices[0].message.content.strip()

# Example usage
prompt = "what is the capital of Australia?"
generated_text = generate_text(prompt)
print(generated_text)

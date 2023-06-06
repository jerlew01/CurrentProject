import openai
import clipboard
import re
import time

openai.api_key = '#api key'
organization = "#org id"

prev_text = None

while True:
    text = clipboard.paste()
    if text != prev_text:  # If the clipboard contents have changed
        prev_text = text

        # Remove the phrase "Access Code xxx-xxx-xxx"
        text = re.sub("Access Code\s*\d{3}-\d{3}-\d{3}", "", text, flags=re.IGNORECASE)

        # Split the text into lines
        lines = text.strip().split('\n')

        # If there's more than one line, the first line is the question and the rest are options
        if len(lines) > 1:
            question = lines[0]
            options = '\n'.join(lines[1:])

            # Prepare the messages for the AI
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{question}\n{options}"},
                {"role": "user", "content": "What's the answer? Only give the answer."},
            ]

            # Use the OpenAI API to generate a response
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=100
            )

            # Print the AI's response
            print(response['choices'][0]['message']['content'])
        else:
            print("No question found in the clipboard text.")
            
    time.sleep(1)  # Wait for 1 second before checking the clipboard again



    #'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'

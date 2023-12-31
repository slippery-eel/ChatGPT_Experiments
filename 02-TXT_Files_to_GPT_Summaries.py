### This script requires a folder with one or more txt files as an input.
### The script will use the GPT API to summarize the text within each of the txt files in succession
### This was useful to me in a situation when I had access to many txt files that I needed to interpret & understand quickly


import os
import openai

# OpenAI API key
openai.api_key = "xxx" # Replace with your OpenAI API Key

# Function to extract text from a text file
def extract_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to generate a GPT summary for a given text
def generate_summary(text):
    # Define the conversation
    conversation = [
        {"role": "assistant", "content": "Please summarize the text:"},
        {"role": "user", "content": text}
        
    ]

    # Make the API call with the conversation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Extract and return the assistant's summary
    return response['choices'][0]['message']['content']

# Folder containing text files
folder_path = r'C:\Users\...\Folder'  # Replace with the actual folder path (with txt files)

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):  # Assuming text files have a .txt extension
        file_path = os.path.join(folder_path, filename)
        text_content = extract_text_from_file(file_path)
        
        # Generate a summary for the text content
        summary = generate_summary(text_content)
        
        # Print the summary
        print(f"Summary for {filename}:")
        print(summary)  # Print the summary obtained from generate_summary
        print("-" * 40)  # Separator between summaries

import os
import re
from time import sleep
from halo import Halo
import openai

# ===============================
# User Configuration Section
# ===============================

# File and Folder Paths
transcripts_folder = 'transcripts'
sprs_folder = 'sprs'
system_message_file = 'system_spr.txt'  # Path to the system message file
openai_key_file = 'key_openai.txt'      # Path to the OpenAI API key file

# OpenAI Model Configuration
default_model = "gpt-3.5-turbo-1106"   # Set the default model to use
default_temperature = 0                # Set the default temperature
default_max_tokens = 2000              # Set the default max tokens
max_context_length = 16385             # Maximum token limit for the OpenAI model

# ===============================
# End of User Configuration Section
# ===============================

def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()

def extract_date_from_filename(filename):
    date_pattern = re.compile(r'(\d{8})')
    match = date_pattern.search(filename)
    if match:
        return match.group(1)
    else:
        return None

def chatbot(conversation, model=default_model, temperature=default_temperature, max_tokens=default_max_tokens):
    max_retry = 7
    retry = 0
    while True:
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=conversation,
                temperature=temperature,
                max_tokens=max_tokens,
                api_key=open_file(openai_key_file).strip()
            )

            spinner = Halo(text='Thinking...', spinner='dots')
            spinner.start()
            sleep(2)  # Adding a brief pause to avoid rapid retries
            spinner.stop()

            text = response['choices'][0]['message']['content']
            tokens = response['usage']['total_tokens']

            return text, tokens
        except Exception as oops:
            retry += 1
            print(f'Error communicating with OpenAI: "{oops}"')
            sleep(5)
            if retry >= max_retry:
                print("Max retries reached, exiting.")
                exit()

def split_text(text, max_words=1400):
    words = text.split()
    chunks = []

    current_chunk = []
    current_length = 0

    for word in words:
        current_chunk.append(word)
        current_length += 1

        if current_length >= max_words:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = 0

    # Add the last chunk if there are any remaining words
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def use_chatgpt(system_message, user_message):
    conversation = [{'role': 'system', 'content': system_message}]

    # Estimate token count
    estimated_token_count = len(user_message) // 4

    # Check if the estimated token count exceeds the max context length
    if estimated_token_count > max_context_length:
        chunks = split_text(user_message)
        print(f"Total chunks created: {len(chunks)}")  # Debugging line

        result = ''
        for i, chunk in enumerate(chunks):
            print(f"Processing chunk {i+1} of {len(chunks)}, size: {len(chunk.split())} words")  # Debugging line
            if len(conversation) > 1:
                conversation[1] = {'role': 'user', 'content': chunk}
            else:
                conversation.append({'role': 'user', 'content': chunk})
            text, _ = chatbot(conversation)
            result += text
        return result
    else:
        if len(conversation) > 1:
            conversation[1] = {'role': 'user', 'content': user_message}
        else:
            conversation.append({'role': 'user', 'content': user_message})
        text, _ = chatbot(conversation)
        return text

if __name__ == '__main__':
    system_message = open_file(system_message_file)

    if not os.path.exists(sprs_folder):
        os.makedirs(sprs_folder)

    for filename in os.listdir(transcripts_folder):
        if filename.endswith('.txt'):
            spr_path = os.path.join(sprs_folder, filename)
            if os.path.exists(spr_path):
                print(f"SPR already exists for {filename}, skipping...")
                continue

            date_of_transcript = extract_date_from_filename(filename)
            if not date_of_transcript:
                print(f"Could not extract date from filename: {filename}")
                continue

            transcript_path = os.path.join(transcripts_folder, filename)
            print(f"Processing transcript: {transcript_path}")

            transcript_text = open_file(transcript_path)

            spr_text = use_chatgpt(system_message, transcript_text)

            spr_lines = spr_text.strip().split('\n')
            spr_with_date = [
                f"- {date_of_transcript[:4]}-{date_of_transcript[4:6]}-{date_of_transcript[6:]} - {line}"
                for line in spr_lines
            ]

            enhanced_spr_text = "\n".join(spr_with_date)
            save_file(spr_path, enhanced_spr_text)
            print(f"Saved enhanced SPR to: {spr_path}")

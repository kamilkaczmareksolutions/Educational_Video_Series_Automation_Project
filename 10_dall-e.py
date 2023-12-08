import os
import re
import requests
import openai

# ===============================
# User Configuration Section
# ===============================

# Path to the illustration prompts file
prompts_file_path = "C:\\Users\\clean\\video_to_spr\\illustration_prompts.txt"

# Path to the OpenAI API key file
api_key_file_path = "C:\\Users\\clean\\video_to_spr\\key_openai.txt"

# Output directory for the generated images
output_dir_name = "Observations"  # User can change this name
output_dir_path = os.path.join("C:\\Users\\clean\\video_to_spr\\artworks", output_dir_name)

# Image size
image_size = "1024x1024"

# =================================
# End of User Configuration Section
# =================================

# Function to read and clean prompts
def read_prompts(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # Adjusted regular expression to match the updated end of each prompt
    prompts = re.findall(r'Prompt \d+:(.*?)- the focus is entirely on the visual portrayal of \w+\.', content, re.DOTALL)
    return [prompt.strip() for prompt in prompts]

# Function to extract the object name from a prompt
def extract_object_name(prompt):
    match = re.search(r"represents (\w+)\.", prompt)
    return match.group(1) if match else "unknown"

# Function to generate an image using DALL·E 3
def generate_image(prompt):
    try:
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            size=image_size,
            n=1,
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

# Function to download and save the image
def download_and_save_image(image_url, file_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)

# Read API key and set it for OpenAI
with open(api_key_file_path, 'r') as key_file:
    api_key = key_file.read().strip()

openai.api_key = api_key

# Read prompts
prompts = read_prompts(prompts_file_path)
print(f"Number of prompts extracted: {len(prompts)}")  # Debugging statement

# Create output directory if it doesn't exist
os.makedirs(output_dir_path, exist_ok=True)

# Generate an image for each prompt
for i, prompt in enumerate(prompts, start=1):
    print(f"Processing Prompt {i}")  # Debugging statement
    object_name = extract_object_name(prompt)
    image_url = generate_image(prompt)
    if image_url:
        file_path = os.path.join(output_dir_path, f"{i}_{object_name}.jpg")
        download_and_save_image(image_url, file_path)
    else:
        print(f"Failed to generate image for Prompt {i}")

print(f"All images generated. Check the directory: {output_dir_path}")

import os
import re

# ===============================
# User Configuration Section
# ===============================

# Directory Paths
source_folder = "C:\\Users\\clean\\video_to_spr\\sprs"
destination_folder = "C:\\Users\\clean\\video_to_spr\\cleaned_sprs"

# =================================
# End of User Configuration Section
# =================================

# Function to clean the text content
def clean_text(content):
    # Removing the date pattern (e.g., - 2013-08-27 - ), numbering, and "- " at the beginning of lines
    cleaned = re.sub(r'- \d{4}-\d{2}-\d{2} -\s*(\d+\.\s*)?', '', content)
    cleaned = re.sub(r'^-\s*', '', cleaned, flags=re.MULTILINE)
    return cleaned

# Function to process all files in the source directory
def process_files(source_dir, destination_dir):
    # Ensure destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    for filename in os.listdir(source_dir):
        if filename.endswith('.txt'):
            source_file_path = os.path.join(source_dir, filename)
            destination_file_path = os.path.join(destination_dir, filename)

            with open(source_file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            cleaned_content = clean_text(content)

            with open(destination_file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_content)
            print(f"Processed {filename}")

if __name__ == "__main__":
    process_files(source_folder, destination_folder)

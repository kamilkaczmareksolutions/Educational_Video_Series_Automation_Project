import os
import random

# ===============================
# User Configuration Section
# ===============================

# Directory containing the .txt files to be merged
source_directory = "C:\\Users\\clean\\video_to_spr\\cleaned_sprs"

# Name of the output file
output_file_name = "Benek.txt"

# New directory for the merged output file
output_directory = "C:\\Users\\clean\\video_to_spr\\data_for_knowledge_base\\Benek"

# ===============================
# End of User Configuration Section
# ===============================

# Path for the merged output file
output_file_path = os.path.join(output_directory, output_file_name)

def merge_and_shuffle_txt_files(directory, output_path):
    sentences = []

    # Read all sentences from files
    for filename in os.listdir(directory):
        if filename.endswith('.txt') and filename != output_file_name:
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as infile:
                sentences.extend(infile.read().split('\n'))

    # Shuffle the sentences
    random.shuffle(sentences)

    # Write shuffled sentences to the output file
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for sentence in sentences:
            if sentence:  # Avoid writing empty lines
                outfile.write(sentence + '\n')

if __name__ == '__main__':
    os.makedirs(output_directory, exist_ok=True)  # Ensure the output directory exists
    merge_and_shuffle_txt_files(source_directory, output_file_path)
    print(f"All .txt files in {source_directory} have been shuffled and merged into {output_file_path}")

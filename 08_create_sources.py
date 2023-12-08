import os
import re
from difflib import SequenceMatcher

# ===============================
# User Configuration Section
# ===============================

# Paths to the source files
timestamps_file_path = "C:\\Users\\clean\\video_to_spr\\data_for_knowledge_base\\Basic_physical_quantities\\Timestamps_Basic_physical_quantities.txt"
video_mapping_file_path = "C:\\Users\\clean\\video_to_spr\\video_url_mappings\\video_url_mapping_PLgQay90CAOBiSkPgojwl-dSDjaomQ824u.txt"

# Output file path
output_file_path = "C:\\Users\\clean\\video_to_spr\\data_for_knowledge_base\\Basic_physical_quantities\\Sources_Basic_physical_quantities.txt"

# Similarity threshold for title matching
similarity_threshold = 0.5

# =================================
# End of User Configuration Section
# =================================

def clean_title_for_matching(title):
    # Retain only letters and spaces
    return re.sub(r'[^a-zA-Z ]', '', title).strip()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_best_match(title, mapping):
    best_match = None
    highest_score = 0.0

    for key in mapping:
        similarity = similar(title, key)
        length_difference = abs(len(title) - len(key))
        
        # Calculate a combined score based on similarity and length difference
        # The length score decreases as the length difference increases
        length_score = max(0, 1 - length_difference / max(len(title), len(key)))
        combined_score = (similarity + length_score) / 2

        if combined_score > highest_score and combined_score > similarity_threshold:
            highest_score = combined_score
            best_match = key

    return best_match if highest_score > similarity_threshold else None

# Read video URL mapping file
video_url_mapping = {}
with open(video_mapping_file_path, 'r', encoding='utf-8') as mapping_file:
    for line in mapping_file:
        parts = line.strip().split(': ')
        title = ': '.join(parts[:-1])  # Handle titles with colons
        url = parts[-1]
        video_url_mapping[title] = url

# Process timestamps file and create sources references
with open(timestamps_file_path, 'r', encoding='utf-8') as timestamps_file, \
     open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write("Źródła:\n")

    for line in timestamps_file:
        if 'found in' in line:
            title_part = re.search(r'- found in \d{8} - (.+?)\.txt', line).group(1)
            cleaned_title_part = clean_title_for_matching(title_part)
            best_match = find_best_match(cleaned_title_part, video_url_mapping)
            if best_match:
                timestamp_line = next(timestamps_file)
                timestamp = re.search(r'- exact timestamp: (\d{2}:\d{2}:\d{2})', timestamp_line).group(1)
                output_file.write(f"- \"{best_match}\" ({video_url_mapping[best_match]}) - sygnatura czasowa: {timestamp}\n")

print(f"Sources file created at {output_file_path}")
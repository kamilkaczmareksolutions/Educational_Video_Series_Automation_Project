import os
import re

# ===============================
# User Configuration Section
# ===============================

# The directory to be processed
directory = "C:\\Users\\clean\\video_to_spr\\transcripts"

# ===============================
# End of User Configuration Section
# ===============================

def remove_timestamps_and_parentheses(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                content = file.read()
                # Remove timestamps
                cleaned_content = re.sub(r'\[\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\]\s*', '', content)

            # Remove lines with content in () or []
            cleaned_content = '\n'.join(line for line in cleaned_content.split('\n') 
                                        if not re.search(r'\[.*\]|\(.*\)', line))

            with open(file_path, 'w') as file:
                file.write(cleaned_content)

# Run the function
remove_timestamps_and_parentheses(directory)
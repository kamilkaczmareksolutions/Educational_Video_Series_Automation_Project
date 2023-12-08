import os

# ===============================
# User Configuration Section
# ===============================

# Directory containing the files
directory_path = "C:\\Users\\clean\\video_to_spr\\transcripts"

# Path to the file containing problematic characters
problematic_chars_file = "C:\\Users\\clean\\video_to_spr\\problematic_chars.txt"

# ===============================
# End of User Configuration Section
# ===============================

# Function to read problematic characters from a file
def read_problematic_chars(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        chars = [line.strip() for line in file.readlines()]
    return chars

# Function to rename files in directory
def rename_files_in_directory(directory_path, problematic_chars):
    renamed_files = []

    for file_name in os.listdir(directory_path):
        if file_name.endswith('.txt'):
            print(f"Original file name (raw): {repr(file_name)}")

            new_file_name = file_name
            for char in problematic_chars:
                new_file_name = new_file_name.replace(char, '')  # Replacing with empty string

            if new_file_name != file_name:
                original_file_path = os.path.join(directory_path, file_name)
                new_file_path = os.path.join(directory_path, new_file_name)
                try:
                    os.rename(original_file_path, new_file_path)
                    renamed_files.append(new_file_name)
                except Exception as e:
                    print(f"Error renaming file {file_name}: {e}")

    return renamed_files

# Main execution
if __name__ == "__main__":
    problematic_chars = read_problematic_chars(problematic_chars_file)
    renamed_files = rename_files_in_directory(directory_path, problematic_chars)
    print("Renamed Files:", renamed_files)

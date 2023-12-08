import os
import zipfile
import re
import shutil

# ===============================
# User Configuration Section
# ===============================

# Directory where the script and zip file are located
base_directory = "C:\\Users\\clean\\video_to_spr\\data_for_knowledge_base"

# Subdirectory for the files
measurements_subdirectory = "Basic_physical_quantities"

# Name of the zip file
zip_file_name = os.path.join(measurements_subdirectory, "transcripts_packed_Basic_physical_quantities.zip")

# Name of the file containing matched quotes
matched_quotes_file_name = os.path.join(measurements_subdirectory, "Matched_quotes_Basic_physical_quantities.txt")

# Name of the output file
output_file_name = os.path.join(measurements_subdirectory, "Timestamps_Basic_physical_quantities.txt")

# Temporary directory for extracted files
temp_extract_dir = "temp_extracted"

# ===============================
# End of User Configuration Section
# ===============================

# Path for the zip, matched quotes, and output files
zip_file_path = os.path.join(base_directory, zip_file_name)
matched_quotes_path = os.path.join(base_directory, matched_quotes_file_name)
output_file_path = os.path.join(base_directory, output_file_name)
temp_extract_path = os.path.join(base_directory, temp_extract_dir)

def extract_zip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted files from {zip_path} to {extract_to}")

def process_matched_quotes(quotes_path, extract_dir, output_path):
    with open(quotes_path, 'r', encoding='utf-8') as quotes_file:
        quotes_content = quotes_file.read()

    # Updated regex pattern to handle both formats
    pattern = re.compile(r'(?:\d+\. )?Q(\d+): "(.+?)"\s+- found in (\d{8} - .+?)\.txt, line\(s\)? (\d+)-\d+')

    with open(output_path, 'w', encoding='utf-8') as output_file:
        for match in pattern.finditer(quotes_content):
            quote_number, quote_text, file_name, line_number = match.groups()
            print(f"Processing Quote {quote_number}")
            file_path = os.path.join(extract_dir, file_name + '.txt')
            line_number = int(line_number)

            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f, start=1):
                        if i == line_number:
                            timestamp_match = re.search(r'\[(\d{2}:\d{2}:\d{2})', line) or re.search(r'\[(\d{2}:\d{2}:\d{2}\.\d{3})', line)
                            if timestamp_match:
                                timestamp = timestamp_match.group(1)
                                output_file.write(f"{quote_number}. Q{quote_number}: \"{quote_text}\"\n   - found in {file_name}.txt, line(s) {line_number}\n   - exact timestamp: {timestamp}\n\n")
                            else:
                                print(f"Timestamp not found for Quote {quote_number}")
            else:
                print(f"File not found for Quote {quote_number}: {file_path}")

def clean_up_temp_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    print(f"Cleaned up temporary directory: {path}")

if __name__ == '__main__':
    extract_zip_file(zip_file_path, temp_extract_path)
    process_matched_quotes(matched_quotes_path, temp_extract_path, output_file_path)
    clean_up_temp_directory(temp_extract_path)
    print(f"Processed matched quotes and stored timestamps in {output_file_path}")
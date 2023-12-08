import os
import subprocess
import re
from datetime import timedelta
from pydub import AudioSegment
from pydub.utils import make_chunks
from googleapiclient.discovery import build

# ===============================
# User Configuration Section
# ===============================

# Download Type (set only one to True)
channel = False
playlist = True
video = False

# Source URLs (set the appropriate URL based on the download type)
youtube_channel_url = "https://www.youtube.com/channel/CHANNEL_ID"  # Replace CHANNEL_ID with the actual channel ID
playlist_url = "https://www.youtube.com/playlist?list=PLgQay90CAOBjq6wIYyjP18pgDb5conXmR"  # Replace PLAYLIST_ID with the actual playlist ID
video_url = "https://www.youtube.com/watch?v=2Zq8jRqOMeg"  # Replace with the actual video URL

# Directory Paths (change these paths as needed)
download_folder = "C:\\Users\\clean\\video_to_spr\\downloaded_audio"
transcripts_folder = "C:\\Users\\clean\\video_to_spr\\transcripts"

# Video URL Mapping
video_url_mappings_directory = "C:\\Users\\clean\\video_to_spr\\video_url_mappings"

# Path to the downloaded_files.txt
downloaded_files_path = "C:\\Users\\clean\\video_to_spr\\downloaded_files.txt"

# Transcription Tool Path and Model (change these if different)
main_executable_path = "C:\\Users\\clean\\video_to_spr\\main.exe"
model_path = "C:\\Users\\clean\\video_to_spr\\ggml-medium.bin"

# YouTube API key file
youtube_api_key_file = "C:\\Users\\clean\\video_to_spr\\key_youtube.txt"

# Audio Chunk Length in Milliseconds (default: 5 minutes)
chunk_length_ms = 300000

# =================================
# End of User Configuration Section
# =================================

# Function to read YouTube API key from a file
def read_youtube_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Function to create YouTube service object
def create_youtube_service(api_key):
    return build('youtube', 'v3', developerKey=api_key)

# Function to get playlist title
def get_playlist_title(youtube, playlist_id):
    request = youtube.playlists().list(
        part='snippet',
        id=playlist_id
    )
    response = request.execute()
    if 'items' in response and response['items']:
        return response['items'][0]['snippet']['title']
    return None

# Ensure download and transcripts directories exist
os.makedirs(download_folder, exist_ok=True)
os.makedirs(transcripts_folder, exist_ok=True)

# Function to download videos as MP3
def download_videos(source_url, output_folder, youtube):
    playlist_id = source_url.split('list=')[-1]
    playlist_title = get_playlist_title(youtube, playlist_id)

    # Open the file in append mode
    with open(downloaded_files_path, 'a', encoding='utf-8') as f:
        # Add a newline before writing the new playlist info to ensure separation
        f.write(f"\n# Playlist: {playlist_title}, {playlist_id}\n")

    try:
        command = [
            "yt-dlp",
            "-x",  # Extract audio
            "--audio-format", "mp3",
            "--download-archive", downloaded_files_path,  # Use the defined path
            "--output", os.path.join(output_folder, "%(upload_date)s - %(title)s.%(ext)s"),
            "--ignore-errors",  # Continue on download errors
            source_url
        ]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while downloading videos: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def read_problematic_chars(file_path):
    chars = []
    with open(file_path, 'r', encoding='utf-8') as file:
        chars = [line.strip() for line in file.readlines()]
    return chars

def similar_file_exists(directory, base_name, extension, problematic_chars):
    base_name_clean = base_name
    for char in problematic_chars:
        base_name_clean = base_name_clean.replace(char, '')

    for file_name in os.listdir(directory):
        if file_name.startswith(base_name_clean) and file_name.endswith(extension):
            return True
    return False

# Helper function to split audio into chunks and save them to disk
def split_audio(input_file, chunk_length_ms=300000):  # Chunk length set to 5 minutes
    audio = AudioSegment.from_file(input_file)
    chunks = make_chunks(audio, chunk_length_ms)
    chunk_files = []
    for i, chunk in enumerate(chunks):
        chunk_name = f"{os.path.splitext(input_file)[0]}_chunk{i}.mp3"
        chunk.export(chunk_name, format="mp3")
        chunk_files.append(chunk_name)
    return chunk_files

def safe_file_read(file_path, default_encoding='utf-8', fallback_encoding='latin1'):
    try:
        with open(file_path, 'r', encoding=default_encoding) as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding=fallback_encoding) as f:
            return f.read()

# Function to convert hh:mm:ss.mmm format to milliseconds
def timestamp_to_ms(timestamp):
    h, m, s = timestamp.split(':')
    s, ms = s.split('.')
    return int(h) * 3600000 + int(m) * 60000 + int(s) * 1000 + int(ms)

# Function to convert milliseconds to hh:mm:ss.mmm format
def ms_to_timestamp(ms):
    hours, ms = divmod(ms, 3600000)
    minutes, ms = divmod(ms, 60000)
    seconds, ms = divmod(ms, 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02}.{int(ms):03}"

# Function to adjust timestamps in transcript
def adjust_timestamps(transcript, offset_ms):
    def adjust_match(match):
        start_ms = timestamp_to_ms(match.group(1))
        end_ms = timestamp_to_ms(match.group(2))
        adjusted_start = ms_to_timestamp(start_ms + offset_ms)
        adjusted_end = ms_to_timestamp(end_ms + offset_ms)
        return f"[{adjusted_start} --> {adjusted_end}]"

    return re.sub(r"\[(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})\]", adjust_match, transcript)

def transcribe_audio(input_folder, output_folder, model_path, problematic_chars):
    for filename in os.listdir(input_folder):
        if filename.endswith('.mp3'):
            input_file_path = os.path.join(input_folder, filename)  # Define the input file path
            base_name = os.path.splitext(filename)[0]
            output_file_path = os.path.join(output_folder, f"{base_name}.txt")

            # Check if a similar file already exists in the transcripts folder
            if similar_file_exists(output_folder, base_name, '.txt', problematic_chars):
                print(f"Transcript already exists for {filename}, skipping...")
                continue

            # Split the audio file into chunks
            chunk_files = split_audio(input_file_path, chunk_length_ms)

            # Transcribe each chunk
            transcripts = []
            total_duration_ms = 0
            for chunk_file in chunk_files:
                command = [
                    main_executable_path,
                    "-m", model_path,
                    "-l", "en",
                    "-otxt",
                    "-f", chunk_file,
                ]

                try:
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    for line in iter(process.stdout.readline, b''):
                        try:
                            print(line.decode(), end='')
                        except UnicodeDecodeError as e:
                            print(f"Unicode decode error: {e}")

                    process.stdout.close()
                    process.wait()

                    # Read and adjust the transcript
                    transcript_file = chunk_file.replace('.mp3', '.txt')
                    transcript = safe_file_read(transcript_file)
                    adjusted_transcript = adjust_timestamps(transcript, total_duration_ms)
                    transcripts.append(adjusted_transcript)
                    os.remove(transcript_file)  # Clean up transcript file

                    # Update total duration for next chunk
                    chunk_duration = len(AudioSegment.from_file(chunk_file))
                    total_duration_ms += chunk_duration
                except subprocess.CalledProcessError as e:
                    print(f"An error occurred while transcribing '{chunk_file}': {e}")
                finally:
                    os.remove(chunk_file)  # Clean up chunk file

            # Combine all successful transcripts and save to a single file
            with open(output_file_path, 'w', encoding='utf-8-sig') as f:
                f.write("\n".join(transcripts))

            print(f"Transcription completed for {filename}")

# Function to parse downloaded files and extract video IDs for each playlist
def parse_downloaded_files(file_path):
    print(f"Reading playlist data from: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    playlists = {}
    current_playlist_id = None

    for line in lines:
        if line.startswith('# Playlist:'):
            # When a new playlist is found, reset current playlist ID and start a new entry in the dictionary
            playlist_id = line.strip().split(',')[-1].strip()
            playlist_name = ' '.join(line.strip().split(' ')[2:]).split(',')[0].strip()
            current_playlist_id = playlist_id
            playlists[current_playlist_id] = {'name': playlist_name, 'videos': []}
            print(f"Found new playlist: {playlist_name} with ID: {playlist_id}")
        elif line.startswith('youtube') and current_playlist_id:
            # Add video IDs to the current playlist
            video_id = line.split()[1]
            playlists[current_playlist_id]['videos'].append(video_id)
            print(f"Added video ID {video_id} to playlist {current_playlist_id}")

    print(f"Finished parsing playlists: {playlists}")
    return playlists

# Function to fetch video URL from YouTube API
def fetch_video_url(youtube, video_id):
    request = youtube.videos().list(
        part='snippet',
        id=video_id
    )
    response = request.execute()
    if 'items' in response and response['items']:
        video_title = response['items'][0]['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_title, video_url
    return None, None

# Function to create video URL mappings for each playlist
def create_video_url_mappings(youtube, playlists, output_directory):
    os.makedirs(output_directory, exist_ok=True)

    for playlist_id, data in playlists.items():
        file_name = f"video_url_mapping_{playlist_id}.txt"
        output_path = os.path.join(output_directory, file_name)
        print(f"Creating mapping file for playlist {playlist_id} at {output_path}")

        with open(output_path, 'w', encoding='utf-8') as file:
            for video_id in data['videos']:
                print(f"Fetching URL for video ID {video_id} in playlist {playlist_id}")
                video_title, video_url = fetch_video_url(youtube, video_id)
                if video_title and video_url:
                    file.write(f"{video_title}: {video_url}\n")
                    print(f"Added URL mapping for video {video_title}")
                else:
                    print(f"Could not fetch URL for video {video_id}")

    print("All video URL mappings have been created.")

# Main process
if __name__ == "__main__":
    try:
        # Check that only one download type is set to True
        if sum([channel, playlist, video]) != 1:
            print("Error: Please set only one of 'channel', 'playlist', or 'video' to True.")
            exit(1)

        # Read YouTube API key and create service
        youtube_api_key = read_youtube_api_key(youtube_api_key_file)
        youtube = create_youtube_service(youtube_api_key)

        # Read problematic characters from file
        problematic_chars = read_problematic_chars("C:\\Users\\clean\\video_to_spr\\problematic_chars.txt")

        source_url = youtube_channel_url if channel else playlist_url if playlist else video_url
        print(f"Downloading content from: {source_url}")
        download_videos(source_url, download_folder, youtube)
        print("Transcribing audio files...")
        transcribe_audio(download_folder, transcripts_folder, model_path, problematic_chars)
        
        # Creating video URL mappings
        print("Creating video URL mappings...")
        playlists = parse_downloaded_files(downloaded_files_path)
        create_video_url_mappings(youtube, playlists, video_url_mappings_directory)
        print("Video URL mappings created successfully.")

        print("All processes completed.")

    except KeyboardInterrupt:
        print("Process was interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred during the process: {e}")

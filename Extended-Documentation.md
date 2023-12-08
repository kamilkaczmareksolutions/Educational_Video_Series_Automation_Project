# Educational Video Series Automation Project

## Introduction
This project presents a comprehensive system for automating the creation of an educational video series. Utilizing custom GPT models and YouTube content, it's designed to build a layered understanding of complex subjects, starting from foundational concepts. The project comprises several interconnected components, each contributing to the creation of a sequential, progressive learning experience.

![Project Workflow Diagram](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/2321a2a6-a149-4c32-b4b0-2070547365a1)

## Components

### 'Foundational Guide' Custom GPT
- **Role**: Serves as an instructional guide for users to understand the foundational concepts behind their queries.
- **Core Functionality**: 
  - **Stepping Back**: This model focuses on breaking down complex queries by stepping back to simpler, more basic concepts. It avoids direct explanations, instead providing the foundational concept that needs to be understood before delving into the user's specific query.
  - **Concise Responses**: Replies are concise, offering one stepping stone concept at a time to ensure clarity and simplicity.
- **Output Structure**:
  - **Initial Response**: For any user query, the model responds with what foundational concept needs to be understood first. For example, for a query about ChatGPT, it might suggest understanding the concept of deep learning before exploring ChatGPT in detail.
  - **Video Script Outline**: Provides a brief outline for a 5-minute video script focused on the foundational concept. This outline includes a breakdown of content for each minute of the video, ensuring it aligns with the core concept.
- **Visualization**:
  - **Enhancing Understanding**: The model proposes visualization ideas to enhance understanding of the foundational concept. These visualizations are designed to be simple and accessible, suitable for a non-technical audience.
  - **Building a Bigger Picture**: Each visualization idea is part of a coherent series that builds upon previous concepts, forming an integrated understanding of the broader subject matter.
  - **Interlinking Concepts**: Visualizations link new queries to previously discussed concepts, demonstrating how each new concept fits into the larger structure. This approach fosters a building-block style of learning.

!['Foundational Guide' Custom GPT](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/755fa8a4-7cd3-4619-a866-2ac5fb5cc5db)

### Whole Chain Document
- **Description**: A structured document that outlines a series of educational topics in a sequential manner.
- **Purpose**: Serves as the framework for the educational content, with each topic building upon the previous ones to gradually introduce more complex concepts.

![Whole Chain Document](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/bf68fe26-cc82-4c83-9e21-149b988be789)

### 'Research Questions' Custom GPT
- **Role**: Specifically designed to generate research questions from the content of the "Whole Chain" document.
- **Functionality**:
  - **Content Transformation**: This model transforms the structured content from each topic in the "Whole Chain" document into a set of research questions. These questions are tailored to facilitate deeper exploration and understanding of the topic.
  - **Prioritization and Roadmap**: The model adheres to a prioritization system within the "Whole Chain." It ensures that the current topic (with the highest priority) is directly addressed through the questions, indirectly leading to the next topic and ultimately contributing to the final goal of covering the last content in the last topic video.
  - **Example-Based Guidance**: For each section of the "Whole Chain" content, the model generates a series of questions that can be queried on platforms like YouTube and Google. These questions aim to delve into specific aspects of the topic, such as the fundamental role, sensory contributions, and real-world applications or implications.
- **Output Structure**:
  - The model outputs a set of research questions for each point in the "Current Content" of a topic, reflecting the priority and roadmap of the "Whole Chain."
  - Each question is formulated to encourage exploration and understanding suitable for video content creation.
- **Task Execution**: The model follows a structured approach to create questions:
  - It takes the "Current Content" from a topic within the "Whole Chain."
  - Generates research questions that are relevant, insightful, and directly address the topic at hand.
  - Ensures that the questions formed are in line with the overall progression and goals of the educational series.

!['Research Questions' Custom GPT](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/691224ec-81f0-4d9a-b7ec-0495893eb866)

### YouTube Research and Playlist Creation 
- **Process**: Involves researching answers to the generated questions on YouTube.
- **Outcome**: Compilation of relevant videos into a playlist, which serves as the primary source for the content in the educational videos.

![Playlist Creation](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/b1b32a2b-7731-474b-9da4-96b8cf228b67)

### 01_download_and_transcribe.py Script - shoutout [Const-me](https://github.com/Const-me)
- **Purpose**: Automates the process of downloading YouTube videos, extracting audio, splitting it into chunks, and transcribing the content.
- **Functions**:
  - `read_youtube_api_key`: Reads the YouTube API key from a file.
  - `create_youtube_service`: Creates a YouTube service object for API interactions.
  - `get_playlist_title`: Retrieves the title of a YouTube playlist.
  - `download_videos`: Downloads videos from YouTube as MP3 files.
  - `read_problematic_chars`: Reads a list of problematic characters for text cleaning.
  - `similar_file_exists`: Checks for the existence of similar files in the transcripts folder.
  - `split_audio`: Splits audio files into manageable chunks.
  - `safe_file_read`: Safely reads files, handling errors.
  - `timestamp_to_ms`: Converts timestamps to milliseconds.
  - `ms_to_timestamp`: Converts milliseconds to timestamp format.
  - `adjust_timestamps`: Adjusts timestamps in transcripts.
  - `transcribe_audio`: Transcribes audio chunks into text.
  - `parse_downloaded_files`: Parses downloaded files to extract video IDs.
  - `fetch_video_url`: Fetches video URLs from the YouTube API.
  - `create_video_url_mappings`: Creates mappings of video URLs for each playlist.
- **Comments**: Include user configurations for download types, source URLs, directory paths, YouTube API key file, and audio chunk length settings.

![Download and Transcribe](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/23fa4c01-483e-436f-ad43-a5c2942c3a9e)

### 02_clean_titles_and_other_things.py Script
- **Purpose**: Cleans and organizes the transcript data.
- **Functions**:
  - `read_problematic_chars`: Reads a list of problematic characters for cleaning.
  - `rename_files_in_directory`: Renames files in a directory for consistency and ease of access.
- **Comments**: Include user configuration for directory paths and the process for reading problematic characters and renaming files.

### 03_clear_timestamps.py Script
- **Purpose**: Removes timestamps and unnecessary content from the transcripts, making them cleaner and more readable.
- **Function**:
  - `remove_timestamps_and_parentheses`: Removes timestamps and content within parentheses or brackets.
- **Comments**: User configuration for specifying the directory to be processed.

### 04_create_sprs.py (Sparse Priming Representations) Script - shoutout [daveshap](https://github.com/daveshap)
- **Purpose**: Creates SPRs (Sparse Priming Representations) for advanced NLP tasks.
- **Functions**:
  - `save_file`, `open_file`, `extract_date_from_filename`, `chatbot`, `split_text`, `use_chatgpt`: Various functions for processing text and interacting with the OpenAI model.
- **Comments**: Configuration for file paths, OpenAI API key, model settings, and process descriptions for creating SPRs.

![SPR Creation](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/7616bdf0-31a6-4d84-8d25-fcd7e4269d8d)

### 05_clean_sprs.py Script
- **Purpose**: Cleans the generated Sparse Priming Representations (SPRs) for clarity and consistency.
- **Functions**:
  - `clean_text`: Cleans the text content by removing dates, numbering, and certain patterns from the lines.
  - `process_files`: Processes all files in the specified source directory, ensuring the destination directory exists and is organized.
- **Comments**: User configuration includes directory paths, and the script details the process of cleaning and organizing SPRs.

### 06_mix_and_merge_sprs.py Script
- **Purpose**: Combines and mixes all SPRs into a single, consolidated file.
- **Function**:
  - `merge_and_shuffle_txt_files`: Merges .txt files from a specified directory, shuffles the sentences for variety, and writes the shuffled content to an output file. Ensures the output directory exists and handles empty lines appropriately.
- **Comments**: User configuration for the directory containing .txt files, the output file name, and the path for the merged file.

![SPR Merging](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/a383e5d2-351e-45a5-b39d-a4b6555f6748)

### 'Presentation Logic' Custom GPT
- **Role**: Specialized in creating PowerPoint presentations tailored to specific educational topics outlined in the "Whole Chain" document.
- **Process**: 
  - **Input and Sources**: The model utilizes information from multiple sources - the "Whole Chain" document, "SAINT FILE," and predefined topic-related questions - to construct a comprehensive presentation.
  - **Customization**: Each presentation is uniquely crafted to cover the CURRENT TOPIC comprehensively by answering specific CURRENT TOPIC QUESTIONS.
- **Functionality**:
  - **Structured Slide Creation**: The model is tasked with creating a 30-slide PowerPoint presentation. Each slide is dedicated to addressing different aspects of the CURRENT TOPIC, following a precise format:
    - Slide 1: Title slide featuring the CURRENT TOPIC.
    - Slide 2: An overview of CURRENT CONTENT.
    - Slides 3-30: These slides are structured to answer the CURRENT TOPIC QUESTIONS, with each segment of questions being addressed in a group of slides. The content on these slides is derived from the SAINT FILE, with each slide containing an original explanation and a direct quote from the file.
  - **Summary and Conclusion**: The presentation includes summary slides synthesizing the key concepts discussed and a final 'Thank You' slide, inviting further questions or discussion.
- **Rules and Guidelines**:
  - The presentation must strictly use information from the SAINT FILE, and each slide should present the information in a way that is different from but consistent with the original quote.
  - The sequence and structure of the slides are fixed, with exact slide numbers allocated for each part of the presentation.
  - The model must not alter the given questions and should ensure that the presentation seamlessly integrates each part, maintaining coherence and logical flow.
- **Purpose and Goals**:
  - The aim is to create a clear, engaging, and informative presentation that directly addresses the CURRENT TOPIC (Priority 5), while also indirectly preparing the ground for NEXT TOPIC (Priority 4) and LAST TOPIC (Priority 3). This methodical approach aligns with the WHOLE CHAIN roadmap (Priority 2), ensuring that each presentation is a step towards the final educational goal.

!['Presentation Logic' Custom GPT](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/397d52a9-2444-4ffb-a02d-653af1767d8a)

### 'Matching Transcripts' Custom GPT
- **Role**: Specialized in matching quotes from the "Presentation Logic" file with corresponding content in the transcripts.
- **Process**:
  - **Understanding the Chain**: Begins by comprehending the "WHOLE CHAIN" document to understand the overarching structure and progression of topics.
  - **Extracting Quotes**: Extracts key quotes from the "Presentation Logic" file, which are essential elements to be matched with the transcripts.
  - **Complex Matching**: Undertakes the challenging task of finding contextually relevant segments in the transcripts that correspond to the extracted quotes. This involves understanding the essence of each quote and identifying similar themes or concepts in the transcripts.
- **Functionality**:
  - **Contextual Understanding**: Employs sophisticated reasoning skills to match the essence of quotes with similar content in the transcripts, acknowledging that direct text matches are unlikely. The model focuses on the broader context and meaning rather than exact words.
  - **Detailed Output**: Provides a structured output listing each quote and its best-matched transcript segment, including the specific file name and line numbers. 
- **Rules and Guidelines**:
  - The model must ensure that each quote is matched with a segment from the transcripts that closely relates to or conveys the same meaning.
  - It must maintain control over the matching process, knowing precisely which transcript file and specific lines correspond to each quote.
  - The output should be comprehensive, covering all extracted quotes and their matches, following the specified output structure.
- **Purpose and Goals**:
  - The aim is to create a rich and nuanced connection between the quotes and the transcripts, enhancing the depth and relevance of the educational content. This process contributes significantly to the ultimate goal of fulfilling the "WHOLE CHAIN" roadmap, ensuring that each matched segment aligns with the broader educational objectives of the project.

!['Matching Transcript' Custom GPT](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/da8e59c1-b36c-454f-b6a5-c1854e9ad225)

### 07_exact_timestamps.py Script
- **Purpose**: Extracts and processes exact timestamps from transcripts and matched quotes to create a structured timeline.
- **Functions**:
  - `extract_zip_file`: Extracts files from a specified zip archive into a temporary directory.
  - `process_matched_quotes`: Processes the matched quotes to identify and extract exact timestamps from the transcripts.
  - `clean_up_temp_directory`: Cleans up the temporary directory used for file extraction and processing.
- **Comments**: 
  - User configuration for directory paths, zip file name, matched quotes file, and output file name.
  - Includes regex patterns for handling various timestamp formats, ensuring accurate extraction.

![Timeline creation](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/a87bfbbd-8022-4183-82d6-e3af89a789fd)

### 08_create_sources.py Script
- **Purpose**: Generates source references by matching video titles with corresponding content and timestamps.
- **Functions**:
  - `clean_title_for_matching`: Cleans video titles to enhance the accuracy of matching with transcript content.
  - `similar`: Calculates the similarity score between two titles.
  - `find_best_match`: Identifies the best matching video title for a given piece of transcript content.
- **Comments**: 
  - User configuration for the paths to source files, output file path, and similarity threshold for title matching.
  - Implements a combined scoring system based on similarity and length difference to improve the matching accuracy.
  - Reads and processes video URL mapping file and handles titles with special characters.

![Sources creation](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/307d8a4a-c7d1-48d4-86ba-28fc3af3e9a1)

### 'Keywords Creation' Custom GPT
- **Role**: Generates a list of unique keywords based on the content of a presentation logic file.
- **Functionality**: 
  - **Extraction of Key Concepts**: The model analyzes the presentation slides, focusing on key nouns and concepts relevant to the topic.
  - **Creation of Unique Keywords**: Each slide contributes to the generation of a distinct keyword, ensuring they are all closely related to the topic and specific enough to be unique.
- **Output Structure**: 
  - A list of 30 nouns, each representing a key concept from the presentation slides. These nouns are used as variables for illustration prompts.
- **Guidelines**: 
  - Only nouns are to be used, and each keyword must be unique and directly related to the topic.
  - Avoid generic or non-topic-related keywords such as "Introduction" or "Conclusion."

!['Keywords Creation' Custom GPT](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/14aa34c9-95ba-4ea5-a5f4-b4c3cfbdd390)

### 09_creating_prompts_artworks.py Script
- **Purpose**: Automates the generation of illustration prompts based on keywords.
- **Function**:
  - `create_prompts`: Generates prompts for artwork illustrations using the provided keywords and other user-defined parameters.
- **Comments**: 
  - User configuration includes variables for illustration prompts, desired colors, and the output file path.
  - The script focuses on creating engaging and relevant prompts for artwork creation.

![Prompts for DALL·E Creation](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/b1e06bad-3688-4431-8b08-290ae929a107)

### 10_dall-e.py Script
- **Purpose**: Utilizes the DALL·E 3 model to generate images based on the created prompts.
- **Functions**:
  - `read_prompts`: Reads and cleans the illustration prompts from a file.
  - `extract_object_name`: Extracts the object name from each prompt for image generation.
  - `generate_image`: Generates an image using DALL·E 3 based on the provided prompt.
  - `download_and_save_image`: Downloads and saves the generated image to a specified directory.
- **Comments**: 
  - Configuration for the illustration prompts file, OpenAI API key, output directory, and image size.
  - The script ensures that each prompt is effectively transformed into a visual representation by DALL·E 3.

![Artworks Creation](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/65b256fd-322a-40fe-b6fa-55eafa976386)

### 'Narration Creator' Custom GPT
- **Role**: Develops a detailed and engaging narration script for the educational video series.
- **Process**:
  - **Integrating Various Sources**: Utilizes content from the 'Logic File', 'Whole Chain', and 'Matched Quotes' to create a rich and contextually accurate narration.
  - **Extracting Contextual Information**: For each quote, the model extracts the referenced line and additional lines from the transcripts, providing a deeper understanding of each point.
  - **Creating Coherent Narrative Flow**: Integrates quotes and their contextual information using the structure provided in the 'Logic File', ensuring logical continuity and a seamless narrative.
  - **Referencing the Whole Chain**: Uses the 'Whole Chain' document for broader context and background information, contributing to a holistic view of the topic.
- **Narration Style**:
  - **Conversational and Accessible Language**: The narration is crafted in a simple, conversational tone, making complex concepts accessible to a non-technical audience.
  - **Interactive Elements**: Incorporates rhetorical questions and scenarios to actively engage the audience.
  - **Regular Summarization**: Key points are regularly summarized for clarity, especially after complex sections.
  - **Relating to Everyday Examples**: Abstract concepts are connected to everyday situations, making the content more relatable.
  - **Impactful Conclusion**: The script concludes by emphasizing the relevance of the topics, leaving a lasting impact.
- **Task Execution**: The model undertakes a structured approach to develop the narration, ensuring it aligns with the presentation's content, style, and educational goals.

!['Narration Creator' Custom GPT](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/968d4ad2-7fe6-4356-9295-beb4cf5cdb1c)

### Manual Presentation Creation
- **Process**: 
  - **Utilizing Presentation Logic**: The presentation is manually created using the structured content from the `presentation_logic` file. This involves selecting relevant information, quotes, and matching them with the appropriate visuals and narration.
  - **Artwork Integration**: Artworks created by DALL·E based on the keywords and prompts are integrated into the presentation, enhancing visual appeal and reinforcing the educational content.
- **Purpose**: To create a visually engaging and content-rich presentation that is ready for recording, aligning with the overall educational theme of the project.

![Presentation Creation](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/6731fdda-99cb-4f1e-9ed4-0980864ef1d3)

### Final Recording and Editing
- **Recording**:
  - **Green Screen Technology**: Utilizes a green screen setup to record the presentation. This allows for seamless integration of the presentation with dynamic backgrounds and visual effects.
  - **Teleprompter Usage**: A teleprompter is used to ensure smooth delivery of the scripted narration, maintaining engagement and clarity.
- **Editing**:
  - **DaVinci Resolve**: Post-recording, the video is edited using DaVinci Resolve, a professional video editing software. This step involves refining the video for quality, adding transitions, and ensuring synchronization of audio, visuals, and narration.
- **Output**: The final product is a polished educational video, ready for distribution on platforms like YouTube, complete with a well-structured narrative, engaging visuals, and professional editing.

![Final Recording and Editing Process](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/75b801cf-7ed2-4c3b-b101-97c66900b9f8)

## Goal
The end goal of this project is to produce a series of educational videos, each topic building upon the previous, to create a comprehensive understanding of complex subjects. This automated system significantly enhances the efficiency of creating educational content, making it a valuable asset for educators and content creators.

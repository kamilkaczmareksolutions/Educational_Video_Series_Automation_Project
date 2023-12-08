# Educational Video Series Automation Project

#### Project Workflow Diagram
<img src="https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/b65897b5-5658-476c-9665-2589f8520979" width="500">

## Quick Overview
This repository contains a project designed to semi-automate the creation of an educational video series. It integrates custom GPTs, Python scripts, and DALL·E to develop a comprehensive understanding of complex topics.

**Note**: This is a brief overview intended to get you started quickly. For an in-depth understanding, please refer to [Extended Documentation](./Extended-Documentation.md).
This is NOT fully-automated process, because I wanted to have controll over Research, and since I'm using Chat GPT Plus subscription, I didn't want to call API so much due to unnecessary additional costs. So I'm doing things with GPT-4 via Chat GPT interface, not by calling API from Python scripts. But it's doable if someone need this, just sayn'.

## Key Components
- **Custom GPTs**: Developed for content creation, question generation, narration, and more.
- **Python Scripts**: Automate processes like transcript handling, timestamp extraction, and artwork creation.
- **Presentation and Recording**: Combines manual and automated steps for producing the final educational videos.

## How It Works
The project follows a systematic approach, from conceptualization to the final recording, ensuring each educational video is engaging and informative, and has the same structure.
Final goal is to break into smaller pieces complex topics, by going one step back and fulfilling neccessary parts of this complex one.

## Getting Started
To get started with this project, follow these steps:

1. **Clone the Repository**:

```
git clone https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project
```

2. **Set Up Environment**:
- Create a virtual environment (optional but recommended):
  ```
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```
- Install required packages (pydub, google-api-python-client, halo, openai, requests):
  ```
  pip install -r requirements.txt
  ```

3. **Create Necessary API Keys**:
- You will need to create your own API keys for OpenAI and YouTube.
- Store these keys in files named `key_openai.txt` and `key_youtube.txt` in the root directory of the project.

4. **Acknowledgments**:
- This project utilizes the SPR (Sparse Priming Representations) technique introduced by David Shapiro. [Learn more about SPR](https://github.com/daveshap/SparsePrimingRepresentations).
- Transcriptions are accelerated using the Whisper solution proposed by user Const-me. [Learn more about his repo](https://github.com/Const-me/Whisper). Be sure you download the `ggml-medium.bin` model from [here](https://huggingface.co/ggerganov/whisper.cpp/blob/main/ggml-medium.bin) and move it to main root. `Whisper.dll`, `main.exe` and `lz4.txt` should be clonned automatically on `git clone` step.

5. **Running the Scripts**:
- You should definitely first get familiar with [Extended Documentation](./Extended-Documentation.md) to catch up.
- Then change variables in each Python script.
- Then customize the scripts and models according to your specific needs or contribute with your improvements.

## Screenshots

#### Initial Input to 'Foundational Guide' Custom GPT
<img src="https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/87dd1301-ea44-4216-960f-b889557e93c6" width="500">

#### 'Presentation Logic' Step Screenshot
<img src="https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/8f766c24-2d66-46cb-9a78-812cd32f18c5" width="700">

#### Final Presentation Slide
<img src="https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/e3429e6d-78b5-43d2-9a8c-30085aa77cbe" width="700">

## To Do
- This all definitely needs to be simplified. Too many scripts. E.g. all types of `cleaning` can be included in one, etc.
- Maybe at the end it will be good to create fully-automated solution, instead of semi-.

## Contributing
Contributions to enhance and expand the project are welcome. You just need to create your own Custom GPTs (I don't think is possible to use the same, because there is need for constantly swapping files in Knowledge Base), or contact me for detailed prompts (can do this here: contact@kamilkaczmareksolutions.com).
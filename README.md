# Educational Video Series Automation Project

![Project Workflow Diagram](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/b65897b5-5658-476c-9665-2589f8520979)

*Figure: Workflow diagram of the project.*

## Quick Overview
This repository contains a project designed to automate the creation of an educational video series. It integrates custom GPT models, Python scripts, and AI tools like DALL·E to develop a comprehensive understanding of complex topics.

**Note**: This is a brief overview intended to get you started quickly. For an in-depth understanding, please refer to my [Extended Documentation](./Extended-Documentation.md).
This is NOT fully-automated process, because I wanted to have controll over Research, and since I'm using ChatGPT Plus subscription, I didn't want to call API so much for additional costs. So I'm doing things with GPT-4 via ChatGPT interface, not by calling API from Python scripts. But it's doable if someone need this, just sayn'.

## Key Components
- **Custom GPT Models**: Developed for content creation, question generation, narration, and more.
- **Python Scripts**: Automate processes like transcript handling, timestamp extraction, and artwork creation.
- **Presentation and Recording**: Combines manual and automated steps for producing the final educational videos.

## How It Works
The project follows a systematic approach, from conceptualization to the final recording, ensuring each educational video is engaging and informative, and has the same structure.

## Getting Started
To get started with this project, follow these steps:

1. **Clone the Repository**:

```
git clone [repository URL]
```

2. **Set Up Environment**:
- Create a virtual environment (optional but recommended):
  ```
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```
- Install required packages:
  ```
  pip install -r requirements.txt
  ```

3. **Create Necessary API Keys**:
- You will need to create your own API keys for OpenAI and YouTube.
- Store these keys in files named `key_openai.txt` and `key_youtube.txt` in the root directory of the project.

4. **Acknowledgments**:
- This project utilizes the SPR (Sparse Priming Representations) technique introduced by David Shapiro. [Learn more about SPR](https://github.com/daveshap/SparsePrimingRepresentations).
- Transcriptions are accelerated using the Whisper solution proposed by user Const-me. [Learn more about Whisper](https://github.com/Const-me/Whisper). Be sure you download the `ggml-medium.bin` model from [here](https://huggingface.co/ggerganov/whisper.cpp/blob/main/ggml-medium.bin) and move it to main root. `Whisper.dll`, `main.exe` and `lz4.txt` should be clonned automatically by `git clone`.

5. **Running the Scripts**:
- You should definitely first get familiar with [Extended Documentation](./Extended-Documentation.md).
- Then change variables in each Python script.
- Customize the scripts and models according to your specific needs or contribute with your improvements.

## Screenshots
![Initial Input to Foundational Guide Custom GPT](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/5d82b344-8a13-427d-b206-667155651f4a)

*Figure: Screenshot of initial input to 'Foundational Guide' Custom GPT.*

![Presentation Logic Step Screenshot](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/8b4838a5-cfde-4b35-9384-6aee529b31af)

*Figure: Screenshot of an intermediate step in the project.*

![Final Presentation Slide](https://github.com/kamilkaczmareksolutions/Educational_Video_Series_Automation_Project/assets/95218485/e3429e6d-78b5-43d2-9a8c-30085aa77cbe)

*Figure: Screenshot of a final presentation slide.*

## Contributing
Contributions to enhance and expand the project are welcome. You just need to create your own Custom GPTs (because there is need for constantly swapping files), or contact me for detailed prompts (can do this here: contact@kamilkaczmareksolutions.com).
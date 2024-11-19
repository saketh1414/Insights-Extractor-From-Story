#Insights-Extractor-From-Story

This project is all about analyzing the input story and extracting specific insights you mention from the story.
Used LLAMA-70b from groqcloud and streamlit for interface.
the model will extract key insights from the story you input.

go through the demo video:
https://drive.google.com/file/d/1-3u1-21V37F988Eibo0v0JUBUWLZdbOU/view?usp=sharing

Steps to run the project:
1. Create a virtual environment venv first--(conda create -p venv python==3.10)
2. Activate the virtual environment--(conda activate "D:\Story Analyzer\venv")
3. Install all the packages present in requirements.txt--(pip install -r requirements.txt)
4. Now run the main.py file as streamlit--(streamlit run main.py)
5. This will open a streamlit interface on your browser.
6. Now paste your story and the specific insight you want to extract from the story.
7. This will generate all the insights of specified topic present in the story.

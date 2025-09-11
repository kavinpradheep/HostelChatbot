# Hostel Chatbot

A Streamlit-based chatbot for Kongu Engineering College that helps students interactively explore hostel rules and Standard Operating Procedures (SOP).

## Live Demo

👉 [Try the Hostel Chatbot](https://hostelchatbot.streamlit.app/)

## Features

- Conversational Q&A about hostel rules and SOPs
- Uses official hostel SOP PDF as knowledge base
- Semantic search for relevant answers
- Powered by Gemini LLM
- Simple web interface

## Setup (For Local Development)

1. **Clone the repository** and add `HostelSOP R1.pdf` to the project folder.
2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
3. **Set up your Google API key** in a `.env` file:
    ```
    GOOGLE_API_KEY=your_google_api_key_here
    ```
4. **Run the app:**
    ```sh
    streamlit run app.py
    ```

## Usage

- Ask questions about hostel rules in the chat box.
- The chatbot responds based on the official SOP.

## Project Structure

```
.
├── app.py
├── HostelSOP R1.pdf
├── requirements.txt
├── .env
└── .gitignore
```

## Technologies

- Streamlit
- LangChain
- Google Gemini LLM
- HuggingFace Sentence Transformers
- DocArray

---

**Developed for Kongu Engineering College

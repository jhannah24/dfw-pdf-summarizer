# DFW Weighs In

**DFW Weighs In** is a Python application that summarizes PDF documents and rewords the summaries in the distinct style of David Foster Wallace. With an intuitive Gradio-based interface, users can upload a PDF and receive creative, high-quality explanations from DFW.

## Features

- **PDF Summarization**: Uses LangChain's `PyPDFLoader` to load, split, and summarize PDF documents effectively.  
- **David Foster Wallace Rewording**: Transforms summaries into a distinctive literary style using OpenAI's GPT model and custom prompt templates.  
- **User-Friendly Interface**: A simple, accessible Gradio interface for uploading PDFs and retrieving results.  
- **Secure Environment**: Manages sensitive data like API keys with `dotenv`.  

## Technologies Used

- **Python**: Core programming language.  
- **LangChain**: For document processing and summarization chains.  
- **OpenAI API**: Powers the summarization and rewording functionality.  
- **Gradio**: Provides an interactive web interface for users.  
- **dotenv**: For securely managing environment variables.  

## Installation and Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/jhannah24/dfw-pdf-summarizer.git
    ```
2. **Create a virtual environment:**
   ```bash
    python3 -m venv env
   ```
3. **Activate the virtual environment:**
   
    Windows
    ```bash
    .\env\Scripts\activate
    ```
    Linux/MacOS
    ```bash
    source env/bin/activate
    ```
4. **Install Required Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```  
5. **Run the application:**
    ```bash
    python main.py
    ```

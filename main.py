from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
import gradio as gr
import os

# Load environment variables from .env
load_dotenv(dotenv_path='./pdf.env')

# Retrieve the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Ensure it's set in the .env file.")

# Initialize the LLM (language model) with text-davinci-003
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

# Function to summarize the PDF
def summarize_pdf(pdf_file):
    try:
        # Load the PDF from the file input
        loader = PyPDFLoader(pdf_file.name)
        docs = loader.load_and_split()

        # Create the summary chain
        chain = load_summarize_chain(llm, chain_type="map_reduce")

        # Generate the summary using the chain
        result = chain.invoke({"input_documents": docs})
        summary = result.get("output_text", "Summary could not be generated.")
        
        # Reword the summary as if written by David Foster Wallace
        prompt = PromptTemplate(
            input_variables = ["summary"],
            template = "Reword the summary as if you are David Foster Wallace: {summary}"
        )
        reworded_summary = llm.invoke(prompt.format(summary=summary)).strip()

        return reworded_summary
    except Exception as e:
        return f"An error occurred: {e}"

# Function to launch the Gradio interface
def main():
    # Set up the Gradio interface
    input_pdf = gr.File(label="Upload the PDF file")
    output_summary = gr.Textbox(label="Summary")

    interface = gr.Interface(
        fn=summarize_pdf,
        inputs=[input_pdf],
        outputs=output_summary,
        title="DFW Weighs In",
        description="David Foster Wallace explains your PDF."
    )

    interface.launch(share=True)

main()

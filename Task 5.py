#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install PyMuPDF


# In[2]:


pip install summa


# In[3]:


import fitz  # PyMuPDF library for PDF parsing
from summa import summarizer  # Summa library for text summarization

def upload_pdf(filepath):
    """
    Simulates uploading a PDF.

    Args:
        filepath (str): Path to the PDF file.

    Returns:
        str: Text content extracted from the PDF.
    """
    with fitz.open(filepath) as pdf:
        text = ""
        for page in pdf:
            text += page.get_text()
    return text

def preprocess_text(text):
    """
    Simulates basic text pre-processing.

    Args:
        text (str): Text content from the PDF.

    Returns:
        str: Preprocessed text
    """
    # Remove headers, footers, and page numbers (replace with regex or libraries)
    lines = text.splitlines()
    cleaned_lines = [line for line in lines if not (line.startswith("----") or line.isdigit())]
    return " ".join(cleaned_lines)  # Join lines with spaces

def summarize_text(text, max_words=500):
    """
    Summarizes text using extractive summarization.

    Args:
        text (str): Preprocessed text content.
        max_words (int): Maximum number of words in the summary. Default is 500.

    Returns:
        str: Summarized text within max_words.
    """
    summary = summarizer.summarize(text, words=max_words)
    return summary

def main():
    # Simulate user upload
    pdf_path = "C:\\Users\\USER\\Downloads\\Operations Management.pdf"  # Update with your PDF path
    text = upload_pdf(pdf_path)

    # Preprocess text
    preprocessed_text = preprocess_text(text)

    # Summarize text
    summary = summarize_text(preprocessed_text)

    # Display summary
    print(f"Summary (500 words):\n{summary}")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





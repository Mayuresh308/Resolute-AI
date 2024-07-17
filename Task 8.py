#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pytesseract


# In[2]:


import pytesseract
from PIL import Image

# Set the path to Tesseract executable if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Use Tesseract to do OCR on the image
            text = pytesseract.image_to_string(img)
            return text.strip()
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

def main():
    # Path to the image
    image_path = "C:\\Users\\USER\\Downloads\\one.png"  # Replace with your image path
    
    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)
    
    if extracted_text:
        print(f"Text extracted from {image_path}:\n{extracted_text}")

if __name__ == '__main__':
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





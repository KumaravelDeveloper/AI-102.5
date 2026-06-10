import os

import streamlit as st
import google.generativeai as genai
from docx import Document
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")
st.header("AI Story Generator")
prompt=st.text_input("Enter your story content:")
a="You are a Story Generator , generates a creatives stories based on the content given by the user., The features of the story based on the character design and the back story of the character should write with proper logic, And genre selection also include the key elements of the story like the plot, setting, conflict, and resolution"
if st.button("submit"):
    response=model.generate_content(a+prompt)
    st.write(response.text)
    document = Document()
    document.add_paragraph(response.text)
    document.save("Story.docx")
    st.download_button(label="Download Story",  file_name="Story.docx", data =open("Story.docx", "rb"), mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
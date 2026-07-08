import streamlit as stlt
from workflow import process_docs

stlt.set_page_config(page_title ="Elchai AI Demo")

stlt.title("Elchai AI Workflow Assistant")

uploaded = stlt.file_uploader("Upload Document")

if uploaded:
    content= uploaded.read().decode('utf-8')
    result =process_docs(content)
    stlt.success("Workflow Generated")
    stlt.write(result)
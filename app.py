# pid_reader_project/frontend/app.py
import streamlit as st
from PIL import Image
import tempfile
import os
import sys
sys.path.append("../backend")
from main import process_pid_image

st.set_page_config(page_title="P&ID Reader App", layout="wide")
st.title("🧠 P&ID Diagram Reader")

uploaded_file = st.file_uploader("Upload P&ID Diagram (PNG only)", type=["png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Diagram", use_column_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    if st.button("🔍 Process Diagram"):
        with st.spinner("Processing diagram..."):
            graph_json, vis_path = process_pid_image(tmp_file_path)

        st.success("✅ Processing complete")
        st.subheader("Detected Lines")
        st.image(vis_path, caption="Lines Detected", use_column_width=True)

        st.subheader("Extracted Graph (JSON)")
        st.code(graph_json, language='json')
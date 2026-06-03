import streamlit as st
import tempfile
import os
from converter.core import DownMark

st.set_page_config(
    page_title="DownMark",
    page_icon="D",
    layout="wide"
)

st.markdown("""
    <style>
        :root {
            --bg: #e6d1b5;
            --surface: #f0dec8;
            --text: #2b2b2b;
            --muted: #6b6b6b;
            --accent: #b7dfc5;
            --accent-soft: #eef8f2;
            --border: #d8c3a6;
        }

        html, body, .stApp, [data-testid="stAppViewContainer"] {
            background: var(--bg) !important;
            color: var(--text) !important;
        }

        [data-testid="stAppViewContainer"] > .main {
            background: var(--bg) !important;
        }

        .block-container {
            background: transparent !important;
        }

        .main { max-width: 720px; margin: auto; }
        .block-container { padding-top: 3rem; }
        h1 { text-align: center; color: var(--text); }
        .caption { text-align: center; color: var(--muted); margin-bottom: 2rem; }

        [data-testid="stHeader"], [data-testid="stToolbar"] {
            background: transparent !important;
        }

        [data-testid="stSidebar"] {
            background: var(--surface) !important;
            border-right: 1px solid var(--border) !important;
        }

        [data-testid="stExpander"],
        [data-testid="stVerticalBlock"] > div > div {
            background: transparent !important;
            border-color: var(--border) !important;
        }

        [data-testid="stFileUploader"] {
            background: var(--surface) !important;
            border: 1px dashed var(--border) !important;
            border-radius: 12px !important;
            padding: 0.75rem !important;
        }

        [data-testid="stFileUploader"] button {
            background-color: var(--accent) !important;
            color: #1f3b2f !important;
            border: 1px solid #91c9ac !important;
            transition: transform 120ms ease, box-shadow 150ms ease, background-color 150ms ease;
        }
        [data-testid="stFileUploader"] button:active {
            transform: scale(0.98);
        }

        .stButton > button {
            width: 100%;
            background-color: var(--accent) !important;
            color: #1f3b2f;
            border: 1px solid #91c9ac;
            padding: 0.6rem 1.2rem;
            border-radius: 10px;
            font-size: 1rem;
            font-weight: 600;
            transition: transform 120ms ease, box-shadow 150ms ease, background-color 150ms ease;
        }
        .stButton > button:hover {
            background-color: #a7d6b9 !important;
        }
        .stButton > button:active {
            transform: scale(0.98);
            box-shadow: 0 2px 0 rgba(0, 0, 0, 0.08);
        }
        .stDownloadButton > button {
            width: 100%;
            background-color: var(--accent) !important;
            color: #1f3b2f !important;
            border: 1px solid #91c9ac !important;
            padding: 0.6rem 1.2rem;
            border-radius: 10px;
            font-size: 1rem;
            font-weight: 600;
            transition: transform 120ms ease, box-shadow 150ms ease, background-color 150ms ease;
        }
        .stDownloadButton > button:hover {
            background-color: #a7d6b9 !important;
        }
        .stDownloadButton > button:active {
            transform: scale(0.98);
            box-shadow: 0 2px 0 rgba(0, 0, 0, 0.08);
        }

        [data-testid="stAlert"] {
            background: var(--surface) !important;
            border-color: var(--border) !important;
            color: var(--text) !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("DownMark to Markdown 🌿")
st.markdown('<p class="caption">A Python utility to cleanly convert PDFs into structured Markdown. Optimized for LLM data ingestion and RAG pipelines.</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "docx", "doc", "xlsx", "xls", "pptx", "ppt", "html", "htm"],
    help="Supported formats: PDF, Word, Excel, PowerPoint, HTML"
)

use_ocr = st.checkbox(
    "Enable OCR fallback (for scanned/image-based PDFs)",
    value=False
)

if uploaded_file is not None:

    st.markdown(f"**File selected:** `{uploaded_file.name}` ({round(uploaded_file.size / 1024, 1)} KB)")

    if st.button("Convert to Markdown ✨"):

        with st.spinner(f"Converting `{uploaded_file.name}`..."):
            try:
                _, file_extension = os.path.splitext(uploaded_file.name)

              
                with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name

                dm = DownMark()
                markdown_result = dm.convert(tmp_path, ocr_fallback=use_ocr)

                os.unlink(tmp_path)

                output_filename = os.path.splitext(uploaded_file.name)[0] + ".md"

                st.success("Conversion complete. Your file is ready to download.")

                st.download_button(
                    label=f"Download {output_filename}",
                    data=markdown_result.encode("utf-8"),
                    file_name=output_filename,
                    mime="text/markdown"
                )

                left, right = st.columns(2, gap="large")
                with left:
                    st.subheader("Raw Markdown")
                    st.code(markdown_result, language="markdown")
                with right:
                    st.subheader("Preview")
                    st.markdown(markdown_result)

            except ValueError as e:
                st.error(f"Unsupported file type: {e}")
            except FileNotFoundError as e:
                st.error(f"File not found: {e}")
            except Exception as e:
                st.error(f"Conversion failed: {e}")

else:
    st.info("Upload a file above to get started.")

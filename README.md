# DownMark

A personal project to optimize token usage in LLM workflows by converting documents to clean, structured Markdown. Markdown is a native, low-friction format for most LLM pipelines.

DownMark is a Python utility to cleanly convert PDFs into structured Markdown. It also supports Word, Excel, PowerPoint, and HTML through a CLI and a simple Streamlit UI.

## Highlights

- Focused on Markdown output suitable for ingestion and RAG pipelines
- CLI and web UI
- Optional OCR path for scanned PDFs
- Post-processing to normalize Markdown output

## Supported Formats

| Format | Extension | Library used |
|--------|-----------|--------------|
| PDF | `.pdf` | `pdfminer.six` + optional OCR via `pytesseract` |
| Word | `.docx` `.doc` | `python-docx` |
| Excel | `.xlsx` `.xls` | `openpyxl` |
| PowerPoint | `.pptx` `.ppt` | `python-pptx` |
| HTML | `.html` `.htm` | `beautifulsoup4` + `markdownify` |

## Installation

```bash
git clone https://github.com/MohammedAmine-dev/DownMark.git
cd DownMark
pip install -e .
```

OCR (for scanned PDFs) requires the Tesseract binary:

```bash
# Windows
choco install tesseract

# macOS
brew install tesseract
```

## CLI Usage

```bash
# Convert a file (saves report.md next to report.pdf)
downmark report.pdf

# Specify an output directory
downmark report.pdf --output ./notes/

# Print Markdown directly to terminal
downmark page.html --stdout

# Enable OCR for scanned / image-based PDFs
downmark scanned.pdf --ocr

# Show version
downmark --version
```

## Web UI

```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Project Structure

```
DownMark/
├── cli.py                  # Click CLI entry-point
├── app.py                  # Streamlit drag-and-drop UI
├── converter/
│   ├── core.py             # Router: dispatches to correct converter
│   ├── pdf_converter.py
│   ├── docx_converter.py
│   ├── xlsx_converter.py
│   ├── pptx_converter.py
│   └── html_converter.py
├── utils/
│   ├── file_handler.py     # File type detection and I/O
│   └── md_cleaner.py       # Markdown post-processing
└── samples/                # Test files
```




## License

MIT. See [LICENSE](./LICENSE).

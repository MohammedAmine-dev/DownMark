# DownMark 📄➜ Markdown

> Convert PDF, Word, Excel, PowerPoint and HTML files into clean, LLM-ready Markdown — from the command line or a drag-and-drop web UI.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-0.1.0-orange)

---

## Features

| Format | Extension | Library used |
|--------|-----------|--------------|
| PDF | `.pdf` | `pdfminer.six` + optional OCR via `pytesseract` |
| Word | `.docx` `.doc` | `python-docx` |
| Excel | `.xlsx` `.xls` | `openpyxl` |
| PowerPoint | `.pptx` `.ppt` | `python-pptx` |
| HTML | `.html` `.htm` | `beautifulsoup4` + `markdownify` |

---

## Installation

```bash
git clone https://github.com/yourusername/DownMark.git
cd DownMark
pip install -e .
```

> **Note for scanned PDFs**: OCR requires the Tesseract binary.
> Windows: `choco install tesseract`
> macOS: `brew install tesseract`

---

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

---

## Web UI

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

<!-- Add a screenshot or GIF here -->
<!-- ![DownMark UI](./assets/demo.gif) -->

---

## Project Structure

```
DownMark/
├── cli.py                  # Click CLI entry-point
├── app.py                  # Streamlit drag-and-drop UI
├── converter/
│   ├── core.py             # Router — dispatches to correct converter
│   ├── pdf_converter.py
│   ├── docx_converter.py
│   ├── xlsx_converter.py
│   ├── pptx_converter.py
│   └── html_converter.py
├── utils/
│   ├── file_handler.py     # File type detection & I/O
│   └── md_cleaner.py       # Markdown post-processing
├── tests/
│   └── test_converters.py
└── samples/                # Test files
```

---

## Running Tests

```bash
pytest tests/ -v
```

---

## Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Commit your changes: `git commit -m "feat: add my feature"`
4. Push and open a Pull Request

---

## License

MIT — see [LICENSE](./LICENSE)

# ==========================================
# converter/pdf_converter.py
# ==========================================
# RESPONSIBILITY:
#   Convert a PDF file to a Markdown string.
#
# LIBRARIES:
#   pip install pdfminer.six
#   pip install pytesseract Pillow   ← only needed for OCR fallback
#
# KEY CONCEPTS:
#   - pdfminer extracts text from digital (text-based) PDFs
#   - pytesseract is OCR — it reads text from images (scanned PDFs)
#   - You only use OCR when pdfminer returns almost no text
#
# YOUR TASKS:
#   1. Import extract_text from pdfminer.high_level
#   2. Call it with LAParams() for better layout handling
#   3. If len(text.strip()) < 100 AND ocr_fallback=True → use tesseract
#   4. Wrap each page with a '\n---\n' separator
# ==========================================

from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams


def convert_pdf(file_path: str, ocr_fallback: bool = False) -> str:
    """
    Extracts text from a PDF and returns it as a Markdown string.

    Primary path:
        text = extract_text(file_path, laparams=LAParams())

    OCR fallback (only if ocr_fallback=True AND text is too short):
        - You'll need: from PIL import Image; import pytesseract
        - Convert PDF pages to images, then call pytesseract.image_to_string(img)
        - Hint: pdf2image.convert_from_path() gives you PIL images per page

    Returns: Markdown string
    """
    text = extract_text(file_path,laparams=LAParams())
    
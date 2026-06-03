import fitz  # PyMuPDF
import pytesseract
from PIL import Image

def convert_pdf(file_path: str, ocr_fallback: bool = False) -> str:
    markdown_pages = []
    total_text_length = 0
    
    try:
        doc = fitz.open(file_path)
    except Exception as e:
        return f"Error opening PDF: {e}"
        
    for page in doc:
        text = page.get_text()
        page_content = text.strip()
        total_text_length += len(page_content)
        
        if page_content:
            markdown_pages.append(page_content)

    if total_text_length < 100 and ocr_fallback:
        try:
            markdown_pages = []
            for page in doc:
                pix = page.get_pixmap()
                mode = "RGBA" if pix.alpha else "RGB"
                img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
                text = pytesseract.image_to_string(img)
                if text.strip():
                    markdown_pages.append(text.strip())
        except Exception as e:
            return f"OCR Failed. Ensure Tesseract is installed on your OS. Error: {e}"
            
    doc.close()
    
    final_markdown = "\n\n---\n\n".join(markdown_pages)
    return final_markdown
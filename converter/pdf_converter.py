from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LAParams
import pytesseract
from PIL import Image

try:
    from pdf2image import convert_from_path
except ImportError:
    convert_from_path = None

def convert_pdf(file_path: str, ocr_fallback: bool = False) -> str:
  
    markdown_pages = []
    total_text_length = 0
    
    for page_layout in extract_pages(file_path, laparams=LAParams()):
        page_text = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                page_text.append(element.get_text().strip())
        
        page_content = "\n\n".join(page_text).strip()
        total_text_length += len(page_content)
        
        if page_content:
            markdown_pages.append(page_content)

    if total_text_length < 100 and ocr_fallback:
        if convert_from_path is None:
            return "Error: pdf2image library is required for OCR. Run: pip install pdf2image"
            
        try:
            images = convert_from_path(file_path)
            markdown_pages = []
            
            for i, image in enumerate(images):
                text = pytesseract.image_to_string(image)
                markdown_pages.append(text.strip())
        except Exception as e:
            return f"OCR Failed. Ensure Tesseract is installed on your OS. Error: {e}"

    final_markdown = "\n\n---\n\n".join(markdown_pages)
    
    return final_markdown
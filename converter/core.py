from utils.file_handler import detect_file_type, resolve_output_path
from utils.md_cleaner import clean_markdown

import os 

from converter.pdf_converter import convert_pdf
from converter.docx_converter import convert_docx
from converter.xlsx_converter import convert_xlsx
from converter.pptx_converter import convert_pptx
from converter.html_converter import convert_html

from pathlib import Path

CONVERTER_MAP: dict = {
    'pdf': convert_pdf,
    'docx': convert_docx,
    'pptx': convert_pptx,
    'html':convert_html,
    'xlsx':convert_xlsx
}


class DownMark:
 
    def convert(self, file_path: str, ocr_fallback: bool = False) -> str:
       

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Could not find file: {file_path}")
        
        ext = detect_file_type(file_path)
        converter_func = CONVERTER_MAP[ext]
        raw_markdown = converter_func(file_path,ocr_fallback=ocr_fallback)
        return clean_markdown(raw_markdown)

    def convert_to_file(
        self,file_path: str,output_path: str | None = None,ocr_fallback: bool = False,) -> str:
       
        md = self.convert(file_path,ocr_fallback)
        resolved_path = resolve_output_path(file_path,output_path)
        Path(resolved_path).write_text(md, encoding='utf-8')
        return str(resolved_path)
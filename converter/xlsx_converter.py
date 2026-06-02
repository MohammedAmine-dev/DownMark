import openpyxl

def convert_xlsx(file_path: str, **kwargs) -> str:
    """
    Converts every sheet in an Excel workbook to a Markdown section.
    """
    wb = openpyxl.load_workbook(file_path, data_only=True)
    markdown_sections = []

    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]
        
        rows = list(sheet.iter_rows(values_only=True))
        
        cleaned_rows = [row for row in rows if any(cell is not None for cell in row)]
        
        if not cleaned_rows:
            continue  

        md_table = _sheet_to_md(sheet_name, cleaned_rows)
        markdown_sections.append(md_table)

    return "\n\n".join(markdown_sections)


def _sheet_to_md(sheet_name: str, rows: list[tuple]) -> str:
    """Helper: converts sheet rows into a Markdown section (heading + GFM table)."""
    
    table_md = [f"## {sheet_name}\n"]
    
    for row_index, row in enumerate(rows):
        row_data = [str(cell).replace('\n', ' ') if cell is not None else "" for cell in row]
        
        row_string = "| " + " | ".join(row_data) + " |"
        table_md.append(row_string)
        
        if row_index == 0:
            separator = "|-" + "-|-".join(["-" * max(3, len(col)) for col in row_data]) + "-|"
            table_md.append(separator)

    return "\n".join(table_md)
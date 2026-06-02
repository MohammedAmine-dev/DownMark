from pathlib import Path

# TODO: Fill this map — keys are lowercase extensions, values are format strings
# e.g. '.pdf' -> 'pdf', '.docx' -> 'docx', '.doc' -> 'docx', etc.
EXTENSION_MAP: dict[str, str] = {
".pdf":"pdf",
".docx":"docx",
".doc":"docx",
".html":"html",
".pptx":"pptx",
".xlsx":"xlsx"}



def detect_file_type(path: str) -> str:
    ext = Path(path).suffix.lower()
    if ext  not in EXTENSION_MAP :
        raise ValueError(f" unsupported file extension {ext}")
    else:
        return EXTENSION_MAP[ext]


def resolve_output_path(input_path: str, output_dir: str | None = None) -> str:
   
    p=Path(input_path)
    if output_dir == None :
        out=p.with_suffix(".md")
        return str(out)
    else:
        out = Path(output_dir) / f"{p.stem}.md"
        return str(out)



def read_file_bytes(path: str) -> bytes:
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"File not found: {path}")
    return p.read_bytes()
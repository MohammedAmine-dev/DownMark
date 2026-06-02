import sys
import click
from converter.core import DownMark

@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--output", "-o", default=None, help="Output directory for .md file")
@click.option("--stdout", is_flag=True, help="Print Markdown to stdout instead of writing a file")
@click.option("--ocr", is_flag=True, help="Enable OCR fallback for scanned PDFs")
@click.version_option(version="0.1.0", prog_name="downmark")

def main(file, output, stdout, ocr):
    """
    DownMark — Convert documents to clean Markdown.
    """
    dm = DownMark()
    
    try:
        if stdout:
            result = dm.convert(file, ocr_fallback=ocr)
            click.echo(result)
            
        else:
            saved_path = dm.convert_to_file(file, output_path=output, ocr_fallback=ocr)
            
            click.echo(click.style(f"✅ Saved to: {saved_path}", fg='green'))
            
    except (ValueError, FileNotFoundError) as e:
        click.echo(click.style(f"❌ Error: {e}", fg='red'))
        sys.exit(1)

if __name__ == "__main__":
    main()
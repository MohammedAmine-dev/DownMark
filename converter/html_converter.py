from bs4 import BeautifulSoup
import markdownify

TAGS_TO_REMOVE = ['script', 'style', 'nav', 'footer', 'aside', 'header', 'iframe', 'noscript']

def convert_html(file_path: str, **kwargs) -> str:
    """
    Reads an HTML file, strips noisy elements, and converts the body to Markdown.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'lxml')

    for tag_name in TAGS_TO_REMOVE:
        for tag in soup.find_all(tag_name):
            tag.decompose()  


    content_to_convert = str(soup.body) if soup.body else str(soup)

    markdown_text = markdownify.markdownify(content_to_convert, heading_style='ATX')

    return markdown_text.strip()
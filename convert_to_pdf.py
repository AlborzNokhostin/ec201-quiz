#!/usr/bin/env python3
"""
Convert markdown to HTML and then to PDF using macOS textutil and cupsfilter
"""

import subprocess
import markdown
import sys

def markdown_to_pdf(md_file, pdf_file):
    """Convert markdown file to PDF"""

    # Read markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['extra', 'nl2br', 'sane_lists'])

    # Add CSS styling for better PDF output
    styled_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            color: #333;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
            border-bottom: 2px solid #bdc3c7;
            padding-bottom: 8px;
        }}
        h3 {{
            color: #555;
            margin-top: 25px;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
        }}
        pre {{
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin-left: 0;
            color: #555;
            font-style: italic;
        }}
        ul, ol {{
            margin-left: 20px;
        }}
        li {{
            margin: 8px 0;
        }}
        strong {{
            color: #2c3e50;
        }}
        hr {{
            border: none;
            border-top: 2px solid #bdc3c7;
            margin: 30px 0;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

    # Save HTML temporarily
    html_file = md_file.replace('.md', '.html')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(styled_html)

    print(f"✓ Created HTML file: {html_file}")

    # Convert HTML to PDF using wkhtmltopdf or similar
    # Try using cupsfilter (built into macOS)
    try:
        subprocess.run([
            'cupsfilter',
            html_file,
            '>', pdf_file
        ], check=True, shell=True)
        print(f"✓ Created PDF: {pdf_file}")
    except:
        # Alternative: just open the HTML in browser and user can print to PDF
        print(f"\nHTML file created: {html_file}")
        print(f"To create PDF: Open the HTML file in your browser and use Print > Save as PDF")
        subprocess.run(['open', html_file])

if __name__ == '__main__':
    markdown_to_pdf(
        '/Users/Alborz/Desktop/Warwick/Macro 2/Week_8_Seminar_Answers.md',
        '/Users/Alborz/Desktop/Warwick/Macro 2/Week_8_Seminar_Answers.pdf'
    )

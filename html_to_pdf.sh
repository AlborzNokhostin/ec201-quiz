#!/bin/bash
# Convert HTML to PDF using macOS native tools

HTML_FILE="/Users/Alborz/Desktop/Warwick/Macro 2/Week_8_Seminar_Answers.html"
PDF_FILE="/Users/Alborz/Desktop/Warwick/Macro 2/Week_8_Seminar_Answers.pdf"

# Method 1: Use wkhtmltopdf if available
if command -v wkhtmltopdf &> /dev/null; then
    echo "Using wkhtmltopdf..."
    wkhtmltopdf "$HTML_FILE" "$PDF_FILE"
    echo "✓ PDF created: $PDF_FILE"
    exit 0
fi

# Method 2: Use python weasyprint
if python3 -c "import weasyprint" 2>/dev/null; then
    echo "Using weasyprint..."
    python3 -c "from weasyprint import HTML; HTML('$HTML_FILE').write_pdf('$PDF_FILE')"
    echo "✓ PDF created: $PDF_FILE"
    exit 0
fi

# Method 3: Use Chrome/Chromium headless
if command -v "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" &> /dev/null; then
    echo "Using Chrome headless..."
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
        --headless \
        --disable-gpu \
        --print-to-pdf="$PDF_FILE" \
        "$HTML_FILE"
    echo "✓ PDF created: $PDF_FILE"
    exit 0
fi

# Method 4: Manual instruction
echo "❌ No automated PDF converter found."
echo ""
echo "Please create PDF manually:"
echo "1. Open: $HTML_FILE"
echo "2. Press Cmd+P (Print)"
echo "3. Save as PDF to: $PDF_FILE"
echo ""
open "$HTML_FILE"

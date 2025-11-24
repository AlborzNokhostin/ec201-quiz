#!/usr/bin/env python3
"""
Add slide references to all quiz questions based on topic and week
"""

import re

# Comprehensive mapping of topics to lecture slides
SLIDE_REFERENCES = {
    # Week 1: Global Imbalances
    1: {
        "Balance of Payments Components": "Lecture 1, Slides 5-8",
        "NIIP and Valuation": "Lecture 1, Slides 12-18",
        "Global Creditors and Debtors": "Lecture 1, Slides 9-11",
        "Dark Matter and Return Differential": "Lecture 1, Slides 20-25",
        "US Valuation Effects": "Lecture 1, Slides 15-18",
    },
    # Week 2: Sustainability
    2: {
        "Finite vs Infinite Horizon": "Lecture 2, Slides 8-15",
        "Transversality Condition": "Lecture 2, Slides 16-20",
        "Perpetual Deficits": "Lecture 2, Slides 21-25",
        "Debt Growth and Sustainability": "Lecture 2, Slides 18-22",
        "Accounting Identities": "Lecture 2, Slides 5-7",
    },
    # Week 3: Theory of Current Account
    3: {
        "Small Open Economy Model": "Lecture 3, Slides 4-8",
        "Euler Equation and Optimization": "Lecture 3, Slides 12-16",
        "Temporary vs Permanent Shocks": "Lecture 3, Slides 20-28",
        "Anticipated Income Shocks": "Lecture 3, Slides 29-32",
        "Budget Constraint": "Lecture 3, Slides 9-11",
        "Consumption Smoothing": "Lecture 3, Slides 17-19",
    },
    # Week 4: Terms of Trade & Interest Rates
    4: {
        "Terms of Trade": "Lecture 4, Slides 5-12",
        "World Interest Rate Changes": "Lecture 4, Slides 15-22",
        "Income and Substitution Effects": "Lecture 4, Slides 18-21",
        "Tariffs": "Lecture 4, Slides 25-30",
    },
    # Week 5: Production Economy
    5: {
        "Production Economy": "Lecture 5, Slides 4-10",
        "Investment Decision": "Lecture 5, Slides 11-18",
        "Total Factor Productivity": "Lecture 5, Slides 19-25",
        "Government Spending": "Lecture 5, Slides 26-30",
    },
}

def add_slide_references(html_content):
    """Add slideRef field to all questions that don't have it"""

    # Pattern to match question objects
    question_pattern = r'(\{[\s\S]*?week:\s*(\d+),[\s\S]*?topic:\s*"([^"]+)"[\s\S]*?explanation:\s*"[^"]*")(,?\s*slideRef:[^}]*)?([\s\S]*?\})'

    def replace_question(match):
        before = match.group(1)
        week = int(match.group(2))
        topic = match.group(3)
        has_slide_ref = match.group(4)
        after = match.group(5)

        # If already has slideRef, skip
        if has_slide_ref:
            return match.group(0)

        # Get slide reference for this week/topic
        slide_ref = None
        if week in SLIDE_REFERENCES:
            week_refs = SLIDE_REFERENCES[week]
            # Try exact match first
            if topic in week_refs:
                slide_ref = week_refs[topic]
            else:
                # Try partial match
                for key in week_refs:
                    if key in topic or topic in key:
                        slide_ref = week_refs[key]
                        break

        # If no specific reference found, use generic week reference
        if not slide_ref:
            slide_ref = f"Lecture {week}, Slides 1-30"

        # Add slideRef before the closing brace
        return f'{before},\n                slideRef: "{slide_ref}"{after}'

    # Apply replacements
    modified = re.sub(question_pattern, replace_question, html_content)

    return modified

def main():
    # Read the HTML file
    with open('/Users/Alborz/Desktop/Warwick/Macro 2/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    print("Adding slide references to questions...")

    # Add slide references
    modified_content = add_slide_references(content)

    # Count how many were added
    original_count = content.count('slideRef:')
    new_count = modified_content.count('slideRef:')
    added = new_count - original_count

    print(f"Added {added} slide references")
    print(f"Total questions with slide references: {new_count}")

    # Write back
    with open('/Users/Alborz/Desktop/Warwick/Macro 2/index.html', 'w', encoding='utf-8') as f:
        f.write(modified_content)

    print("✓ Slide references added successfully!")

if __name__ == '__main__':
    main()

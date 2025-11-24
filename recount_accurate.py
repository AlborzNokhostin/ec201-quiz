#!/usr/bin/env python3
"""
Accurately recount OK, test, and exam mentions using strict word boundaries
"""

import re
import os

def count_words_strict(text, word):
    """
    Count exact word matches only, not substring matches
    Uses word boundaries to ensure "exam" doesn't match "example"
    and "ok" doesn't match "book"
    """
    # Case-insensitive word boundary matching
    pattern = r'\b' + re.escape(word) + r'\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)

def analyze_lecture(week, date, transcript_files):
    """Analyze lecture transcripts with strict word matching"""

    combined_text = ""

    for file_path in transcript_files:
        if not os.path.exists(file_path):
            continue
        with open(file_path, 'r', encoding='utf-8') as f:
            combined_text += f.read() + " "

    if not combined_text.strip():
        return None

    # Count with strict word boundaries
    ok_count = count_words_strict(combined_text, 'OK')
    test_count = count_words_strict(combined_text, 'test')
    exam_count = count_words_strict(combined_text, 'exam')

    # Count sentences
    sentences = re.split(r'[.!?]+', combined_text)
    sentence_count = len([s for s in sentences if s.strip()])

    # Count words
    words = combined_text.split()
    word_count = len(words)

    return {
        'week': week,
        'date': date,
        'ok': ok_count,
        'test': test_count,
        'exam': exam_count,
        'sentences': sentence_count,
        'words': word_count
    }

def main():
    base_path = "/Users/Alborz/Desktop/Warwick/Macro 2/Text version of Lectures"

    lectures = [
        (1, "Oct 9", ["EC201 - 2025-10-09-transcript.txt", "EC201 - 2025-10-09-transcript-2.txt"]),
        (2, "Oct 16", ["EC201 - 2025-10-16-transcript.txt", "EC201 - 2025-10-16-transcript-2.txt"]),
        (3, "Oct 23", ["EC201 - 2025-10-23-transcript.txt", "EC201 - 2025-10-23-transcript-2.txt"]),
        (4, "Oct 30", ["EC201 - 2025-10-30-transcript.txt", "EC201 - 2025-10-30-transcript-2.txt"]),
        (5, "Nov 6", ["EC201 - 2025-11-06-transcript.txt", "EC201 - 2025-11-06-transcript-2.txt"]),
        (6, "Nov 13", ["EC201 - 2025-11-13-transcript.txt", "EC201 - 2025-11-13-transcript-2.txt"]),
        (7, "Nov 20", ["EC201 - 2025-11-20-transcript.txt", "EC201 - 2025-11-20-transcript-2.txt"]),
    ]

    print("=" * 80)
    print("ACCURATE RECOUNT WITH STRICT WORD BOUNDARIES")
    print("=" * 80)
    print("\nCounting only EXACT word matches (not substrings):")
    print("- 'OK' matches 'OK' but NOT 'book' or 'look'")
    print("- 'test' matches 'test' but NOT 'attest' or 'latest'")
    print("- 'exam' matches 'exam' but NOT 'example' or 'examine'")
    print("\n" + "=" * 80)
    print()

    results = []
    total_ok = 0
    total_test = 0
    total_exam = 0
    total_sentences = 0
    total_words = 0

    for week, date, files in lectures:
        file_paths = [os.path.join(base_path, f) for f in files]
        result = analyze_lecture(week, date, file_paths)

        if result:
            results.append(result)
            total_ok += result['ok']
            total_test += result['test']
            total_exam += result['exam']
            total_sentences += result['sentences']
            total_words += result['words']

            print(f"Week {week} ({date}):")
            print(f"  OK:        {result['ok']:4d}")
            print(f"  Test:      {result['test']:4d}")
            print(f"  Exam:      {result['exam']:4d}")
            print(f"  Sentences: {result['sentences']:4d}")
            print(f"  Words:     {result['words']:6d}")
            print()

    print("=" * 80)
    print("TOTALS:")
    print(f"  OK:        {total_ok:4d}")
    print(f"  Test:      {total_test:4d}")
    print(f"  Exam:      {total_exam:4d}")
    print(f"  Test+Exam: {total_test + total_exam:4d}")
    print(f"  Sentences: {total_sentences:4d}")
    print(f"  Words:     {total_words:6d}")
    print("=" * 80)

    # Save results to file
    with open('/Users/Alborz/Desktop/Warwick/Macro 2/accurate_counts.txt', 'w') as f:
        f.write("ACCURATE WORD COUNTS (Strict Word Boundaries)\n")
        f.write("=" * 80 + "\n\n")

        for result in results:
            f.write(f"Week {result['week']}:\n")
            f.write(f"  OK: {result['ok']}, Test: {result['test']}, Exam: {result['exam']}\n")
            f.write(f"  Sentences: {result['sentences']}, Words: {result['words']}\n\n")

        f.write(f"\nTOTALS:\n")
        f.write(f"  OK: {total_ok}\n")
        f.write(f"  Test: {total_test}\n")
        f.write(f"  Exam: {total_exam}\n")
        f.write(f"  Test+Exam: {total_test + total_exam}\n")
        f.write(f"  Sentences: {total_sentences}\n")
        f.write(f"  Words: {total_words}\n")

    print("\n✓ Results saved to accurate_counts.txt")

    return results, {
        'ok': total_ok,
        'test': total_test,
        'exam': total_exam,
        'sentences': total_sentences,
        'words': total_words
    }

if __name__ == '__main__':
    main()

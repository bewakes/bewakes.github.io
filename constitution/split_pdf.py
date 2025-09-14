#!/usr/bin/env python3
"""
PDF Splitter Script

Splits a PDF file into two parts at a specified page number.
The first part contains pages 1 to split_page-1, and the second part contains pages from split_page to the end.
"""

import argparse
import sys
from pathlib import Path

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("Error: PyPDF2 is required. Install it with: pip install PyPDF2")
    sys.exit(1)


def split_pdf(input_file, split_page, output_prefix=None):
    """
    Split a PDF file into two parts at the specified page number.

    Args:
        input_file (str): Path to the input PDF file
        split_page (int): Page number where to split (1-indexed)
        output_prefix (str): Prefix for output files. If None, uses input filename
    """
    try:
        # Read the input PDF
        reader = PdfReader(input_file)
        total_pages = len(reader.pages)

        if split_page < 1 or split_page > total_pages:
            print(f"Error: Split page {split_page} is out of range. PDF has {total_pages} pages.")
            return False

        # Generate output filenames
        input_path = Path(input_file)
        if output_prefix is None:
            output_prefix = input_path.stem

        part1_name = f"{output_prefix}_part1.pdf"
        part2_name = f"{output_prefix}_part2.pdf"

        # Create first part (pages 1 to split_page-1)
        if split_page > 1:
            writer1 = PdfWriter()
            for page_num in range(split_page - 1):
                writer1.add_page(reader.pages[page_num])

            with open(part1_name, 'wb') as output1:
                writer1.write(output1)
            print(f"Created {part1_name} with pages 1-{split_page-1}")
        else:
            print("No pages before split point - skipping part 1")

        # Create second part (pages split_page to end)
        if split_page <= total_pages:
            writer2 = PdfWriter()
            for page_num in range(split_page - 1, total_pages):
                writer2.add_page(reader.pages[page_num])

            with open(part2_name, 'wb') as output2:
                writer2.write(output2)
            print(f"Created {part2_name} with pages {split_page}-{total_pages}")

        return True

    except Exception as e:
        print(f"Error processing PDF: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Split a PDF file into two parts at a specified page number")
    parser.add_argument("input_file", help="Path to the input PDF file")
    parser.add_argument("split_page", type=int, help="Page number where to split (1-indexed)")
    parser.add_argument("-o", "--output-prefix", help="Prefix for output files (default: input filename)")

    args = parser.parse_args()

    # Check if input file exists
    if not Path(args.input_file).exists():
        print(f"Error: Input file '{args.input_file}' not found")
        sys.exit(1)

    # Split the PDF
    success = split_pdf(args.input_file, args.split_page, args.output_prefix)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Build the constitution webpage by injecting JSON data
"""

import json
import os
from pathlib import Path

def load_constitution_data():
    """Load the constitution JSON data"""
    with open('constitution.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_qna_data():
    """Load the merged Q&A JSON file"""
    qa_file = Path('qna.json')

    if not qa_file.exists():
        print("Warning: qna.json not found, attempting to create it by merging part files...")
        # Fallback to old method if merged file doesn't exist
        qa_dir = Path('/qa')
        all_qna = []

        for i in range(1, 10):  # part1.json to part9.json
            part_file = qa_dir / f'part{i}.json'
            if part_file.exists():
                with open(part_file, 'r', encoding='utf-8') as f:
                    part_qna = json.load(f)
                    if isinstance(part_qna, list):
                        all_qna.extend(part_qna)
                        print(f"Loaded {len(part_qna)} Q&A items from {part_file.name}")

        # Save merged file for future use
        with open(qa_file, 'w', encoding='utf-8') as f:
            json.dump(all_qna, f, ensure_ascii=False, indent=2)
        print(f"Created merged qna.json with {len(all_qna)} items")
        return all_qna

    # Load the merged file
    with open(qa_file, 'r', encoding='utf-8') as f:
        all_qna = json.load(f)

    print(f"Loaded {len(all_qna)} Q&A items from merged qna.json")
    return all_qna

def build_webpage():
    """Build the final webpage with injected JSON data"""
    # Load data
    constitution_data = load_constitution_data()
    qna_data = load_qna_data()

    # Read the HTML template
    with open('template.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Convert data to JSON strings
    constitution_json = json.dumps(constitution_data, ensure_ascii=False, separators=(',', ':'))
    qna_json = json.dumps(qna_data, ensure_ascii=False, separators=(',', ':'))

    # Replace placeholders
    html_content = html_content.replace('INSERT_CONSTITUTION_JSON_HERE', constitution_json)
    html_content = html_content.replace('INSERT_QNA_JSON_HERE', qna_json)

    # Write the final webpage
    output_path = '../docs/constitution.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Constitution webpage built successfully: {output_path}")

    # Print statistics
    total_parts = len(constitution_data['constitution']['parts'])
    total_articles = sum(len(part['articles']) for part in constitution_data['constitution']['parts'])

    print(f"\nStatistics:")
    print(f"- Constitution Parts: {total_parts}")
    print(f"- Total Articles: {total_articles}")
    print(f"- Q&A Items: {len(qna_data)}")
    print(f"- File size: {os.path.getsize(output_path) / 1024 / 1024:.1f} MB")

if __name__ == "__main__":
    build_webpage()

#!/usr/bin/env python3
"""
Nepal Constitution HTML to Structured JSON Parser
Parses the Nepal Constitution HTML file into structured JSON format
"""

import re
import json
from bs4 import BeautifulSoup
from typing import Dict, List, Any, Optional

class ConstitutionParser:
    def __init__(self, html_file_path: str):
        self.html_file_path = html_file_path
        self.soup = None
        self.constitution_data = {
            "constitution": {
                "title": "",
                "publicationDate": "",
                "preamble": {"text": ""},
                "tableOfContents": [],
                "parts": [],
                "schedules": []
            }
        }

    def load_html(self):
        """Load and parse the HTML file"""
        with open(self.html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.soup = BeautifulSoup(content, 'html.parser')

    def extract_title(self):
        """Extract the main title"""
        title_pattern = r'THE CONSTITUTION OF NEPAL'
        text = self.soup.get_text()
        if re.search(title_pattern, text):
            self.constitution_data["constitution"]["title"] = "THE CONSTITUTION OF NEPAL"

    def extract_publication_date(self):
        """Extract publication date"""
        date_pattern = r'(\d{4}\.\d+\.\d+)'
        text = self.soup.get_text()
        match = re.search(date_pattern, text)
        if match:
            self.constitution_data["constitution"]["publicationDate"] = match.group(1)

    def extract_preamble(self):
        """Extract preamble text"""
        preamble_start = "We, the Sovereign People of Nepal"
        preamble_end = "system of governance."

        text = self.soup.get_text()
        start_idx = text.find(preamble_start)
        if start_idx != -1:
            end_idx = text.find(preamble_end, start_idx) + len(preamble_end)
            preamble_text = text[start_idx:end_idx].strip()
            self.constitution_data["constitution"]["preamble"]["text"] = preamble_text

    def extract_table_of_contents(self):
        """Extract table of contents"""
        toc_entries = []

        # Find TOC section
        paragraphs = self.soup.find_all('p')
        in_toc = False

        for p in paragraphs:
            text = p.get_text().strip()
            if 'Table of Contents' in text:
                in_toc = True
                continue

            if in_toc and text:
                # Parse TOC entries
                lines = text.split('br/')
                for line in lines:
                    line = line.strip()
                    if re.match(r'Part-?\d+', line):
                        match = re.search(r'Part-?(\d+)', line)
                        if match:
                            part_num = int(match.group(1))
                            title = re.sub(r'Part-?\d+\s*', '', line).strip()
                            toc_entries.append({
                                "type": "part",
                                "number": part_num,
                                "title": title
                            })
                    elif re.match(r'Schedule-?\d+', line):
                        match = re.search(r'Schedule-?(\d+)', line)
                        if match:
                            schedule_num = int(match.group(1))
                            title = re.sub(r'Schedule-?\d+\s*', '', line).strip()
                            toc_entries.append({
                                "type": "schedule",
                                "number": schedule_num,
                                "title": title
                            })
                    elif line == 'Preamble':
                        toc_entries.append({
                            "type": "preamble",
                            "title": "Preamble"
                        })

                # Stop after first TOC block
                if toc_entries:
                    break

        self.constitution_data["constitution"]["tableOfContents"] = toc_entries

    def extract_parts_and_articles(self):
        """Extract all parts and their articles"""
        paragraphs = self.soup.find_all('p')
        current_part = None
        current_article = None

        for p in paragraphs:
            raw_text = str(p)
            text = p.get_text().strip()
            if not text:
                continue

            # Check for Part header - handle <br/> tags properly
            if re.search(r'Part-\d+', text):
                part_match = re.search(r'Part-(\d+)\s*<br\s*/?>\s*([^<]*)', raw_text)
                if part_match:
                    if current_part:
                        if current_article:
                            current_part["articles"].append(current_article)
                        self.constitution_data["constitution"]["parts"].append(current_part)

                    part_num = int(part_match.group(1))
                    part_title = part_match.group(2).strip()

                    current_part = {
                        "number": part_num,
                        "title": part_title,
                        "articles": []
                    }
                    current_article = None
                    continue

            # Check for Article start
            article_match = re.match(r'(\d+)\.\s*([^:]+):\s*(.*)', text, re.DOTALL)
            if article_match:
                if current_article and current_part:
                    current_part["articles"].append(current_article)

                article_num = article_match.group(1)
                article_title = article_match.group(2).strip()

                current_article = {
                    "number": f"{article_num}.",
                    "title": article_title,
                    "content": []
                }

                # Parse the full raw text which includes the article content
                self._parse_article_content(raw_text, current_article)
                continue

            # Continue parsing content for current article
            if current_article and current_part:
                self._parse_article_content(raw_text, current_article)

        # Add the last part
        if current_part:
            if current_article:
                current_part["articles"].append(current_article)
            self.constitution_data["constitution"]["parts"].append(current_part)

    def _parse_article_content(self, raw_html: str, article: Dict):
        """Parse article content for subsections and sub-subsections"""
        if not raw_html.strip():
            return

        # Split by <br/> tags first
        segments = re.split(r'<br\s*/?>', raw_html)

        for segment in segments:
            # Clean HTML tags but preserve text
            segment_text = re.sub(r'<[^>]+>', '', segment).strip()
            if not segment_text:
                continue

            # Skip the article declaration line itself (e.g., "7. Official language: (1) content")
            article_declaration_match = re.match(r'^\d+\.\s*[^:]+:\s*(.*)', segment_text)
            if article_declaration_match:
                # Extract content that comes after the article declaration
                remaining_content = article_declaration_match.group(1).strip()
                if remaining_content:
                    # Parse this remaining content
                    self._parse_content_segment(remaining_content, article)
                continue

            # Parse regular content segments
            self._parse_content_segment(segment_text, article)

    def _parse_content_segment(self, segment_text: str, article: Dict):
        """Parse a single content segment for subsections and sub-subsections"""
        if not segment_text.strip():
            return

        # Check for numbered subsection pattern: (1), (2), etc.
        subsection_match = re.match(r'\((\d+)\)\s*(.*)', segment_text, re.DOTALL)
        if subsection_match:
            subsection_num = subsection_match.group(1)
            subsection_text = subsection_match.group(2).strip()

            subsection = {
                "type": "subsection",
                "identifier": f"({subsection_num})",
                "text": subsection_text,
                "items": []
            }

            # Check for lettered sub-subsections within this text
            self._extract_sub_subsections(subsection_text, subsection)
            article["content"].append(subsection)
            return

        # Check for lettered sub-subsection pattern: (a), (b), etc.
        sub_subsection_match = re.match(r'\(([a-z])\)\s*(.*)', segment_text, re.DOTALL)
        if sub_subsection_match:
            letter = sub_subsection_match.group(1)
            sub_text = sub_subsection_match.group(2).strip()

            # Add to the last subsection if it exists
            if article["content"] and article["content"][-1].get("type") == "subsection":
                article["content"][-1]["items"].append({
                    "type": "sub_subsection",
                    "identifier": f"({letter})",
                    "text": sub_text
                })
            else:
                # Create a standalone sub-subsection
                article["content"].append({
                    "type": "sub_subsection",
                    "identifier": f"({letter})",
                    "text": sub_text
                })
            return

        # Regular text content - merge with previous subsection or sub-subsection if it exists
        if segment_text and not re.match(r'^\d+\.\s*[^:]+:', segment_text):
            # Try to merge with the last sub-subsection first
            if (article["content"] and
                article["content"][-1].get("type") == "subsection" and
                article["content"][-1].get("items") and
                len(article["content"][-1]["items"]) > 0):

                # Merge with the last sub-subsection in the last subsection
                last_subsection = article["content"][-1]
                last_sub_item = last_subsection["items"][-1]

                if last_sub_item.get("type") == "sub_subsection":
                    current_text = last_sub_item["text"]
                    if current_text and not current_text.endswith(' '):
                        last_sub_item["text"] = current_text + " " + segment_text
                    else:
                        last_sub_item["text"] = current_text + segment_text
                    return

            # Try to merge with the last subsection if no sub-items
            elif (article["content"] and
                  article["content"][-1].get("type") == "subsection" and
                  len(article["content"][-1].get("items", [])) == 0):

                # Append to the last subsection's text
                current_text = article["content"][-1]["text"]
                if current_text and not current_text.endswith(' '):
                    article["content"][-1]["text"] = current_text + " " + segment_text
                else:
                    article["content"][-1]["text"] = current_text + segment_text
            else:
                # Create standalone text if no subsection to merge with
                article["content"].append({
                    "type": "text",
                    "text": segment_text
                })

    def _extract_sub_subsections(self, text: str, subsection: Dict):
        """Extract lettered sub-subsections from subsection text"""
        # Look for patterns like (a) text, (b) text, etc.
        pattern = r'\(([a-z])\)\s*([^(]*?)(?=\([a-z]\)|$)'
        matches = re.findall(pattern, text)

        if matches:
            # Remove the sub-subsections from the main text
            cleaned_text = re.sub(r'\([a-z]\)[^(]*', '', text).strip()
            subsection["text"] = cleaned_text

            # Add the sub-subsections
            for letter, sub_text in matches:
                subsection["items"].append({
                    "type": "sub_subsection",
                    "identifier": f"({letter})",
                    "text": sub_text.strip()
                })

    def parse(self) -> Dict[str, Any]:
        """Main parsing function"""
        print("Loading HTML file...")
        self.load_html()

        print("Extracting title...")
        self.extract_title()

        print("Extracting publication date...")
        self.extract_publication_date()

        print("Extracting preamble...")
        self.extract_preamble()

        print("Extracting table of contents...")
        self.extract_table_of_contents()

        print("Extracting parts and articles...")
        self.extract_parts_and_articles()

        return self.constitution_data

    def save_json(self, output_path: str):
        """Save parsed data to JSON file"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.constitution_data, f, ensure_ascii=False, indent=2)
        print(f"Constitution data saved to {output_path}")

def main():
    parser = ConstitutionParser('/Users/bibek/projects/constitution/constitution.html')
    constitution_data = parser.parse()
    parser.save_json('/Users/bibek/projects/constitution/constitution.json')

    # Print some statistics
    parts_count = len(constitution_data["constitution"]["parts"])
    total_articles = sum(len(part["articles"]) for part in constitution_data["constitution"]["parts"])

    print(f"\nParsing completed!")
    print(f"Total Parts: {parts_count}")
    print(f"Total Articles: {total_articles}")
    print(f"Table of Contents entries: {len(constitution_data['constitution']['tableOfContents'])}")

if __name__ == "__main__":
    main()
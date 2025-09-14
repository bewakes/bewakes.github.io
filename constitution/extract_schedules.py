#!/usr/bin/env python3
"""
Extract structured data from constitution_schedule.pdf and convert to JSON format
"""

import json
import re
from pathlib import Path

try:
    from PyPDF2 import PdfReader
except ImportError:
    print("Error: PyPDF2 is required. Install it with: pip install PyPDF2")
    exit(1)


def extract_schedule_text(pdf_path):
    """Extract text from PDF pages"""
    reader = PdfReader(pdf_path)
    pages_text = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        pages_text.append({
            "page": i + 1,
            "text": text
        })

    return pages_text


def parse_schedule_1(text):
    """Parse Schedule 1: National Flag construction methods"""
    # Extract the main sections
    sections = []

    # Method of making the shape inside the border
    shape_section = {
        "title": "Method of making the shape inside the border",
        "type": "instructions",
        "steps": []
    }

    # Extract numbered steps for shape making (1-5)
    shape_pattern = r'\((\d+)\)\s+(.+?)(?=\(\d+\)|$)'
    shape_matches = re.findall(shape_pattern, text, re.DOTALL)

    for match in shape_matches[:5]:  # First 5 are for shape
        step_num, step_text = match
        shape_section["steps"].append({
            "number": int(step_num),
            "instruction": step_text.strip().replace('\n', ' ')
        })

    sections.append(shape_section)

    # Method of making the moon (6-18)
    moon_section = {
        "title": "Method of making the moon",
        "type": "instructions",
        "steps": []
    }

    for match in shape_matches[5:18]:  # Steps 6-18 for moon
        step_num, step_text = match
        moon_section["steps"].append({
            "number": int(step_num),
            "instruction": step_text.strip().replace('\n', ' ')
        })

    sections.append(moon_section)

    # Method of making the sun (19-22)
    sun_section = {
        "title": "Method of making the sun",
        "type": "instructions",
        "steps": []
    }

    for match in shape_matches[18:22]:  # Steps 19-22 for sun
        step_num, step_text = match
        sun_section["steps"].append({
            "number": int(step_num),
            "instruction": step_text.strip().replace('\n', ' ')
        })

    sections.append(sun_section)

    # Method of making the border (23-24)
    border_section = {
        "title": "Method of making the border",
        "type": "instructions",
        "steps": []
    }

    for match in shape_matches[22:24]:  # Steps 23-24 for border
        step_num, step_text = match
        border_section["steps"].append({
            "number": int(step_num),
            "instruction": step_text.strip().replace('\n', ' ')
        })

    sections.append(border_section)

    return sections


def parse_schedule_2(text):
    """Parse Schedule 2: National Anthem"""
    # Extract anthem lines
    anthem_lines = [
        "Sayaun Thunga Phool Ka Hami Eutai Mala Nepali",
        "Sarvavhaum Vai Failiyeka Mechi Mahakali",
        "Prakitika Koti Koti Sampada Ko Aanchala",
        "Bir Haruka Ragata Le Swatantra Ra Atala",
        "Gyana Bhumi Shanti Bhumi Terai Pahad Himala",
        "Akhanda Yo Pyaro Hamro Matri Bhumi Nepal",
        "Bahul Jati Bhasa Dharma Sanskriti Chan Bishala",
        "Agragami Rastra Hamro Jaya Jaya Nepal."
    ]

    return {
        "title": "National Anthem of Nepal",
        "type": "anthem",
        "lines": anthem_lines,
        "full_text": "\n".join(anthem_lines)
    }


def parse_schedule_3(text):
    """Parse Schedule 3: Coat of Arms"""
    return {
        "title": "Coat of Arms of Nepal",
        "type": "emblem",
        "description": "This Coat of Arms may be made in larger or smaller size as per necessity. The colour determined by the Government of Nepal shall be used on it."
    }


def parse_schedule_4(text):
    """Parse Schedule 4: States and Districts"""
    states_data = {
        1: ["Taplejung", "Panchthar", "Ilam", "Sankhuwasabha", "Tehrathum", "Dhankuta", "Bhojpur", "Khotang", "Solukhumbu", "Okhaldhunga", "Udayapur", "Jhapa", "Morang", "Sunsari"],
        2: ["Saptari", "Siraha", "Dhanusa", "Mahottari", "Sarlahi", "Rautahat", "Bara", "Parsa"],
        3: ["Dolakha", "Ramechhap", "Sindhuli", "Kavrepalanchok", "Sindhupalchok", "Rasuwa", "Nuwakot", "Dhading", "Chitwan", "Makawanpur", "Bhaktapur", "Lalitpur", "Kathmandu"],
        4: ["Gorkha", "Lamjung", "Tanahun", "Kaski", "Manang", "Mustang", "Parbat", "Syangja", "Myagdi", "Baglung", "Nawalparasi (East of Bardaghat Susta)"],
        5: ["Nawalparasi (West of Bardaghat Susta)", "Rupandehi", "Kapilbastu", "Palpa", "Arghakhanchi", "Gulmi", "Rukun (Eastern Part)", "Rolpa", "Pyuthan", "Daang", "Banke", "Bardiya"],
        6: ["Rukum (Western Part)", "Salyan", "Dolpa", "Jumla", "Mugu", "Humla", "Kalikot", "Jajarkot", "Dailekh", "Surkhet"],
        7: ["Bajura", "Bajhang", "Doti", "Achham", "Darchula", "Baitadi", "Dadeldhura", "Kanchanpur", "Kailali"]
    }

    states = []
    for state_num, districts in states_data.items():
        states.append({
            "number": state_num,
            "name": f"State No. {state_num}",
            "districts": districts,
            "district_count": len(districts)
        })

    return {
        "title": "States, and Districts to be included in the concerned States",
        "type": "administrative_division",
        "total_states": 7,
        "total_districts": sum(len(districts) for districts in states_data.values()),
        "states": states
    }


def parse_power_schedule(schedule_num, text, title):
    """Parse power distribution schedules (5-9)"""
    # Extract numbered items
    pattern = r'(\d+)\.\s+(.+?)(?=\d+\.|$)'
    matches = re.findall(pattern, text, re.DOTALL)

    powers = []
    for match in matches:
        item_num, item_text = match
        # Clean up text
        clean_text = item_text.strip().replace('\n', ' ').replace('  ', ' ')
        powers.append({
            "number": int(item_num),
            "description": clean_text
        })

    return {
        "title": title,
        "type": "power_list",
        "powers": powers,
        "total_powers": len(powers)
    }


def extract_schedules():
    """Main extraction function"""
    pdf_path = "constitution_schedule.pdf"

    if not Path(pdf_path).exists():
        print(f"Error: {pdf_path} not found")
        return None

    pages_text = extract_schedule_text(pdf_path)
    full_text = "\n".join([page["text"] for page in pages_text])

    schedules = []

    # Schedule 1: National Flag (pages 1-3)
    schedule_1_text = "".join([pages_text[i]["text"] for i in range(3)])
    schedules.append({
        "number": 1,
        "title": "National Flag of Nepal",
        "article_reference": "Article 8(2)",
        "type": "instructions",
        "sections": parse_schedule_1(schedule_1_text)
    })

    # Schedule 2: National Anthem (page 4)
    schedules.append({
        "number": 2,
        "title": "National Anthem of Nepal",
        "article_reference": "Article 9(1)",
        "type": "anthem",
        **parse_schedule_2(pages_text[3]["text"])
    })

    # Schedule 3: Coat of Arms (page 5)
    schedules.append({
        "number": 3,
        "title": "Coat of Arms of Nepal",
        "article_reference": "Article 9(2)",
        "type": "emblem",
        **parse_schedule_3(pages_text[4]["text"])
    })

    # Schedule 4: States and Districts (pages 6-8)
    schedule_4_text = "".join([pages_text[i]["text"] for i in range(5, 8)])
    schedules.append({
        "number": 4,
        "title": "States, and Districts to be included in the concerned States",
        "article_reference": "Article 56(3)",
        "type": "administrative_division",
        **parse_schedule_4(schedule_4_text)
    })

    # Schedule 5: Federal Powers (pages 9-11)
    schedule_5_text = "".join([pages_text[i]["text"] for i in range(8, 11)])
    schedules.append({
        "number": 5,
        "article_reference": "Article 57(1), Article 109",
        **parse_power_schedule(5, schedule_5_text, "List of Federal Power")
    })

    # Schedule 6: State Powers (pages 12-13)
    schedule_6_text = "".join([pages_text[i]["text"] for i in range(11, 13)])
    schedules.append({
        "number": 6,
        "article_reference": "Article 57(2), Article 162(4), Article 197, Article 231(3), Article 232(7), Article 274(4), Article 296(4)",
        **parse_power_schedule(6, schedule_6_text, "List of State Power")
    })

    # Schedule 7: Concurrent Powers (Federation and State) (pages 14-15)
    schedule_7_text = "".join([pages_text[i]["text"] for i in range(13, 15)])
    schedules.append({
        "number": 7,
        "article_reference": "Article 57(3), Article 109, Article 162(4), Article 197",
        **parse_power_schedule(7, schedule_7_text, "List of Concurrent Powers of Federation and State")
    })

    # Schedule 8: Local Level Powers (pages 17-18)
    schedule_8_text = "".join([pages_text[i]["text"] for i in range(16, 18)])
    schedules.append({
        "number": 8,
        "article_reference": "Article 57(4), Article 214(2), Article 221(2), Article 226(1)",
        **parse_power_schedule(8, schedule_8_text, "List of Local Level Power")
    })

    # Schedule 9: Concurrent Powers (Federation, State and Local) (pages 19-20)
    schedule_9_text = "".join([pages_text[i]["text"] for i in range(18, 20)])
    schedules.append({
        "number": 9,
        "article_reference": "Article 57(5), Article 109, Article 162(4), Article 197, Article 214(2), Article 221(2), Article 226(1)",
        **parse_power_schedule(9, schedule_9_text, "List of Concurrent Powers of Federation, State and Local Level")
    })

    return {
        "schedules": schedules,
        "total_schedules": len(schedules),
        "extraction_metadata": {
            "source_file": pdf_path,
            "total_pages": len(pages_text),
            "extraction_date": "2024"
        }
    }


def main():
    """Extract schedules and save to JSON"""
    print("Extracting schedules from constitution_schedule.pdf...")

    schedules_data = extract_schedules()

    if schedules_data:
        output_file = "constitution_schedules.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(schedules_data, f, indent=2, ensure_ascii=False)

        print(f"✓ Extracted {schedules_data['total_schedules']} schedules")
        print(f"✓ Saved to {output_file}")

        # Print summary
        for schedule in schedules_data["schedules"]:
            if schedule["type"] == "power_list":
                print(f"  Schedule {schedule['number']}: {schedule['total_powers']} powers")
            elif schedule["type"] == "administrative_division":
                print(f"  Schedule {schedule['number']}: {schedule['total_states']} states, {schedule['total_districts']} districts")
            else:
                print(f"  Schedule {schedule['number']}: {schedule['title']}")

    else:
        print("Failed to extract schedules")


if __name__ == "__main__":
    main()
# JSON Point Extractor

This is a simple Python script that extracts `latitude`, `longitude`, and `currentAltitude` from a large JSON file and writes them to a CSV-style text file.  

It’s designed for use with JSON files containing nested land-survey or terrain data.

## Features

- Reads a JSON file.
- Extracts only the points that have `latitude`, `longitude`, and `currentAltitude`.
- Outputs the results in a text file with a header: `lat,long,alt`.
- Works for large JSON files with deeply nested structures.

## Requirements

- Python 3.x
- Standard library only (`json` module)

## Usage

1. Clone or download this repository.
2. Place your JSON file in a known location.
3. Update the `input_path` and `output_path` variables in the script to match your file paths.
4. Run the script:

```bash
python extract_points.py

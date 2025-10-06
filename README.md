JSON Point Extractor

This is a simple Python script that extracts latitude, longitude, and currentAltitude from a large JSON file and writes them to a CSV-style text file.

It’s designed for use with JSON files containing nested land-survey or terrain data.

Features

Reads a JSON file.

Extracts only the points that have latitude, longitude, and currentAltitude.

Outputs the results in a text file with a header: lat,long,alt.

Works for large JSON files with deeply nested structures.

Requirements

Python 3.x

Standard library only (json module)

Usage

Clone or download this repository.

Place your JSON file in a known location.

Update the input_path and output_path variables in the script to match your file paths.

Run the script:

python extract_points.py


Check the output text file. Example:

lat,long,alt
-29.984465830242808,24.70066054633428,1130.3679999523163
-29.984458828642854,24.700578699998786,1130.3139999523162
...

Notes

The script recursively searches all nested dictionaries and lists in the JSON.

Only entries containing all three fields (latitude, longitude, currentAltitude) will be included in the output.

The output file is saved in a simple CSV-like format, compatible with Excel or Google Sheets.

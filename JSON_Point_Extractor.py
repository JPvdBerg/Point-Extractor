import json

input_path = r"C:\Users\drunk\Documents\_Projects\Divvie JSON\Lieberwalt nr 2.json"
output_path = r"C:\Users\drunk\Documents\_Projects\Divvie JSON\extracted_points.txt"

def extract_points(obj, results):
    """Recursively search for dicts with latitude, longitude, and currentAltitude."""
    if isinstance(obj, dict):
        if all(k in obj for k in ("latitude", "longitude", "currentAltitude")):
            results.append((obj["latitude"], obj["longitude"], obj["currentAltitude"]))
        for v in obj.values():
            extract_points(v, results)
    elif isinstance(obj, list):
        for item in obj:
            extract_points(item, results)

def main():
    print("Reading JSON file...")
    with open(input_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    print("Extracting points...")
    results = []
    extract_points(data, results)

    print(f"Found {len(results)} points. Writing to text file...")
    with open(output_path, "w", encoding="utf-8") as out_file:
        # write header
        out_file.write("lat,long,alt\n")
        # write each point
        for lat, lon, alt in results:
            out_file.write(f"{lat},{lon},{alt}\n")

    print(f"Done. Output written to: {output_path}")

if __name__ == "__main__":
    main()

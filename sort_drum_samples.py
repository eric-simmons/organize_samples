import os
import re
import shutil

pattern = r'(hh|oh|hihat|shaker|casaba|closedhat|openhat|clap|cp|snare|sd|tom|ride|cymbal|cym|conga|perc|aux|chime|cow|clave|kick|bd|clav)'

source_dir = 'unsorted_samples'
sorted_samples_dir = "sorted_samples"

keyword_to_dir = {
    'bd': 'sorted_samples/KICK',
    'kick': 'sorted_samples/KICK',
    'hh': 'sorted_samples/HATS_SHAKE',
    'oh': 'sorted_samples/HATS_SHAKE',
    'hihat': 'sorted_samples/HATS_SHAKE',
    'shaker': 'sorted_samples/HATS_SHAKE',
    'casaba': 'sorted_samples/HATS_SHAKE',
    'closedhat': 'sorted_samples/HATS_SHAKE',
    'openhat': 'sorted_samples/HATS_SHAKE',
    'clap': 'sorted_samples/CLAP_SNARE',
    'cp': 'sorted_samples/CLAP_SNARE',
    'snare': 'sorted_samples/CLAP_SNARE',
    'sd': 'sorted_samples/CLAP_SNARE',
    'tom': 'sorted_samples/TOMS',
    'ride': 'sorted_samples/CYMBAL',
    'cymbal': 'sorted_samples/CYMBAL',
    'cym': 'sorted_samples/CYMBAL',
    'perc': 'sorted_samples/PERC_DRUM',
    'aux': 'sorted_samples/PERC_DRUM',
    'chime': 'sorted_samples/PERC_DRUM',
    'cow': 'sorted_samples/PERC_DRUM',
    'clave': 'sorted_samples/PERC_DRUM',
    'clav': 'sorted_samples/PERC_DRUM',
    'conga': 'sorted_samples/PERC_DRUM'
}

remaining_files = []

for dirpath, dirnames, filenames in os.walk(source_dir):
    print("Searching directory:", dirpath) 
    for filename in filenames:
        source_path = os.path.join(dirpath, filename)  
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            keyword = match.group().lower()
            if keyword in keyword_to_dir:
                dest_dir = os.path.join(sorted_samples_dir, keyword_to_dir[keyword]) 
                dest_path = os.path.join(dest_dir, filename)
                try:
                    shutil.move(source_path, dest_path)
                    print(f"Moved {filename} to {dest_path}")
                except FileNotFoundError:
                    print(f"FileNotFoundError: {source_path} not found. Skipping...")
            else:
                remaining_files.append(source_path)
        else:
            remaining_files.append(source_path)
print("Remaining files:")
for i, filename in enumerate(remaining_files):
    print(f"{i+1}. {filename}")

while remaining_files:
    keyword_input = input("Enter a keyword to search for in the remaining files (or 'quit' to exit): ")
    if keyword_input.lower() == 'quit':
        break

    matching_files = []
    for filename in remaining_files:
        if keyword_input.lower() in filename.lower():
            matching_files.append(filename)

    if matching_files:
        dest_dir_input = input(f"Enter a directory name in sorted_samples to move the matching files ({', '.join(matching_files)}): ")
    
        dest_dir = os.path.join(sorted_samples_dir, dest_dir_input)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for filename in matching_files:
            print(f"{filename} filename RIGHT HERE ")
            dest_path = os.path.join(sorted_samples_dir, dest_dir_input, os.path.basename(filename))
            shutil.move(filename, dest_path)
            print(f"Moved {filename} to {dest_path}")

    all_files = os.listdir(source_dir)
    remaining_files = [filename for filename in all_files if os.path.isfile(os.path.join(source_dir, filename))]

    if not remaining_files:
        all_files = os.listdir(source_dir)
        remaining_files = [filename for filename in all_files if os.path.isfile(os.path.join(source_dir, filename))]

    print("Remaining files:")
    print(", ".join(remaining_files))

print("All files sorted!")
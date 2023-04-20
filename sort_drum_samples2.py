import os
import re
import shutil

# Define the regex pattern to search for keywords
pattern = r'(hh|oh|hihat|shaker|casaba|closedhat|openhat|clap|cp|snare|sd|tom|ride|cymbal|cym|conga|perc|aux|chime|cow|clave|kick|bd|clav)'

# Define the source directory to search for files and its subdirectories recursively
source_dir = 'unsorted_samples'
sorted_samples_dir = "sorted_samples"

# Define the dictionary to map keywords to destination directories
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

def find_remaining_files(source_dir):
    remaining_files = []
    # Walk through the source directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(source_dir):
        print("Searching directory:", dirpath)
        for filename in filenames:
            source_path = os.path.join(dirpath, filename)
            remaining_files.append(source_path)
            print(remaining_files)
    return remaining_files

def move_files_by_keyword(keyword_to_dir):
    moved_files = []
    remaining_files = find_remaining_files(source_dir)
    for source_path in remaining_files:
        filename = os.path.basename(source_path)
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            keyword = match.group().lower()
            if keyword in keyword_to_dir:
                dest_dir = os.path.join(sorted_samples_dir, keyword_to_dir[keyword])
                os.makedirs(dest_dir, exist_ok=True)  
                # create destination directory if not exists
                dest_path = os.path.join(dest_dir, filename)
                shutil.move(source_path, dest_path)
                print(f"Moved file: {filename} -> {dest_path}")
                moved_files.append(dest_path)
    return moved_files
                
def move_files_by_input():
    remaining_files = find_remaining_files(source_dir)
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


print("All files sorted!")


move_files_by_keyword(keyword_to_dir)
move_files_by_input()


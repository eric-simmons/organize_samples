import os
folder_path = input("Enter the path to the folder: ")
file_extension = input("Enter the file extension (ending): ")
all_files = os.listdir(folder_path)
files_to_delete = []
for filename in all_files:
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):

        if not filename.endswith(file_extension):
    
            files_to_delete.append(filename)
print("Files to be deleted:")
for filename in files_to_delete:
    print(filename)
confirm = input("Do you want to proceed with deletion? (yes/no): ")

if confirm.lower() == "yes":
    for filename in files_to_delete:
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)
        print(f"Deleted file: {filename}")
else:
    print("Deletion cancelled.")

import os
import shutil

# Base folder path
base_folder = "/Users/ayushprasad/Desktop/Master Folder - Research/Full Setups"

# Loop through Bandwise and True 3d folders
for subfolder in os.listdir(base_folder):
    subfolder_path = os.path.join(base_folder, subfolder)
    
    # Skip if not a folder
    if not os.path.isdir(subfolder_path):
        continue

    # Loop through .ipynb files inside each subfolder
    for file in os.listdir(subfolder_path):
        if file.endswith(".ipynb"):
            file_path = os.path.join(subfolder_path, file)
            folder_name = os.path.splitext(file)[0]
            new_folder_path = os.path.join(subfolder_path, folder_name)
            
            # Create new folder and move file
            os.makedirs(new_folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(new_folder_path, file))
            
            print(f"Moved '{file}' → '{new_folder_path}/'")

print("✅ Done! All .ipynb files inside Bandwise and True 3d organized into folders.")
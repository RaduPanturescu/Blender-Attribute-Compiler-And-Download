import os
import zipfile
import time

# Define the path to the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Loop over the saved .blend files on the desktop
for file_name in os.listdir(desktop_path):
    if file_name.endswith(".blend"):

        # Construct the paths to the .blend file and the .zip file
        blend_file_path = os.path.join(desktop_path, file_name)
        zip_file_path = os.path.join(desktop_path, file_name[:-6] + ".zip")

        # Create a new .zip file and add the .blend file to it
        with zipfile.ZipFile(zip_file_path, mode="w") as zip_file:
            zip_file.write(blend_file_path, arcname=file_name)

        # Remove the original .blend file
        os.remove(blend_file_path)
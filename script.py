import bpy
import random
import os
import json
import zipfile
import time

# Define the name of the parent collection containing the sub-collections
parent_collection_name = "NFT"

# Define the number of final 3D files to generate
num_files = 5

# Define the path to the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define the path to the metadata file
metadata_file_path = os.path.join(desktop_path, "metadata.json")

# Load the metadata from the file
with open(metadata_file_path, "r") as f:
    metadata = json.load(f)

# Create a new collection for the random mesh combination
new_collection_name = "VARIANT1"
new_collection = bpy.data.collections.new(new_collection_name)
bpy.context.scene.collection.children.link(new_collection)

# Loop over each child collection of the parent collection and select the mesh based on the metadata
for child_collection in bpy.data.collections[parent_collection_name].children:
    meshes = child_collection.all_objects
    selected_mesh = None
    for attribute in metadata["attributes"]:
        if attribute["trait_type"] == child_collection.name:
            for obj in meshes:
                if obj.name.startswith(attribute["value"]):
                    selected_mesh = obj
                    break
            break
    if selected_mesh is None:
        selected_mesh = random.choice(meshes)
    new_collection.objects.link(selected_mesh)

# Loop over the number of files to generate
for i in range(num_files):
    # Remove the parent collection from the mesh combination
    bpy.data.collections.remove(bpy.data.collections[parent_collection_name], do_unlink=True)

    # Save the resulting mesh combination as a new .blend file
    file_name = "Mesh Combination {}.blend".format(i + 1)
    file_path = os.path.join(desktop_path, file_name)
    bpy.ops.wm.save_as_mainfile(filepath=file_path)

    # Add the parent collection back to the scene after saving the file
    bpy.context.scene.collection.children.link(bpy.data.collections[parent_collection_name])

    # Remove the randomly selected meshes from the "VARIANT1" collection
    for obj in new_collection.objects:
        new_collection.objects.unlink(obj)
    bpy.data.collections.remove(new_collection, do_unlink=True)
    new_collection = bpy.data.collections.new(new_collection_name)
    bpy.context.scene.collection.children.link(new_collection)


#####------ blender -b your_blend_file.blend -P your_script.py ------#####
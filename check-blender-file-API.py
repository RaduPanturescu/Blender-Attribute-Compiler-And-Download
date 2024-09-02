import os
from flask import Flask, request, jsonify, send_file, after_this_request, Response
import subprocess
from werkzeug.wsgi import FileWrapper


app = Flask(__name__)

# checks if the .blend file has been created launches the .zip converter
@app.route('/generate-file')
def check_complete():
    
    # Define the path to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    cmd = 'blender -b sex.blend -P test-script.py'

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: {stderr.decode('utf-8')}")
        return jsonify({'message': 'error'}), 202
    else:
        # Define the path to the .blend file
        blend_file_path = os.path.join(desktop_path, "Mesh Combination 1.blend")

        # Check if the .blend file is complete (i.e., no temp file)
        if any(fname.endswith('.blend') for fname in os.listdir(desktop_path)):
            # If the file is complete, launch the script to convert it to .zip
            subprocess.run(["python", os.path.join(desktop_path, "zip-convert.py")])
        else:
            return jsonify({'message': 'Processing Request'}), 202


        file_path = os.path.join(desktop_path, "Mesh Combination 1.zip")

        # Check if the file exists
        if os.path.exists(file_path):

            # Send the file to the user
            def generate_file_stream():
                with open(file_path, 'rb') as file:
                    wrapper = FileWrapper(file)
                    for data in wrapper:
                        yield data
                os.remove(file_path)

            return Response(generate_file_stream(), headers={'Content-Disposition': f'attachment;filename={"Mesh Combination 1.zip"}'})

        else:
            return "File not found", 404


if __name__ == '__main__':
    app.run(debug=True)

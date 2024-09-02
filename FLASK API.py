from flask import Flask, request, jsonify, send_file


app = Flask(__name__)

@app.route('/')
def index():
    return 'test'

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(file.filename)
    return jsonify({'message': 'File uploaded successfully'})

# downloading a text file 'example.txt'
# @app.route('/download')
# def download_file():
#     return send_file('example.txt', as_attachment=True)

# downloading a .rar file
@app.route('/download')
def download_file():
    return send_file('example.rar', as_attachment=True)

if __name__ == '__main__':
    app.run()



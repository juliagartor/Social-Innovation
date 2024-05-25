from flask import Flask, request, jsonify
from analysis import melanoma, radio # Import your model function
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/analyze', methods=['GET','POST'])
def analyze():
    # Log a message when the route is called
    logging.info('Received POST request to /analyze')
    logging.info('Request files: %s', request.files)

    if 'image' not in request.files:
        print('No image provided')
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Image not correct formated.'}), 400
    
    # Save the file to disk
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    # Print the file path for debugging purposes
    print(f'File saved to: {file_path}')

    if 'consult' in request.form:
        print('consult')
        return jsonify(radio(file_path))

    print('melanoma')

    return jsonify(melanoma(file_path))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

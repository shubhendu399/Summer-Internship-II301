from flask import Flask, request, jsonify, send_from_directory
from boltiotai import openai
import os

# Initialize the Flask application
app = Flask(__name__, static_folder='public')

# Set the OpenAI API key
API_KEY = 'j91VplXZeajJ5nQR-_PR3_FPJZlwi1gcAZpUvjRoX5Q'
openai.api_key = API_KEY

@app.route('/generate-content', methods=['POST'])
def generate_content():
    """
    Endpoint to generate educational content based on the provided course title.
    It uses OpenAI's GPT-3.5-turbo model to generate the content.
    """
    try:
        data = request.json
        course_title = data.get('courseTitle', '')

        if not course_title:
            return jsonify({'error': 'Course title is required'}), 400

        response = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are a curriculum development assistant."},
                {"role": "user", "content": f"Generate an educational content outline for the course title: {course_title}. Include objectives, sample syllabus, learning outcomes (Knowledge, Comprehension, Application), assessment methods, and recommended readings."}
            ],
        )

        if response and 'choices' in response and len(response['choices']) > 0:
            content = response['choices'][0]['message']['content'].strip()
            return jsonify({'content': content})
        else:
            return jsonify({'error': 'No content generated'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def serve_home():
    """
    Serves the home page of the application.
    """
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    """
    Serves static files such as CSS and JavaScript files from the public directory.
    """
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    # Run the Flask application on port 3005
    app.run(port=3005)


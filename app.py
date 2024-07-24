from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv



# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError("No API key found. Please set your API key in the .env file.")

# Configure the API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-shayari', methods=['GET'])
def generate_shayari():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({'error': 'Keyword is required'}), 400

    try:
        response = model.generate_content(f"Create a Shayari based on {keyword} in English")
        shayari = response.text
        return jsonify({'shayari': shayari})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("No API_KEY environment variable set")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_questions', methods=['POST'])
def get_questions():
    topic = request.json.get('topic')
    
    url = "https://egp.dashboard.scale.com/api/v4/applications/2ee05581-6dfc-4580-9b0f-345e9741a135/process"
    
    payload = {
        "inputs": {
            "knowledge_base_ids": [
                "9947842f-ddd7-4a73-b2c0-227c79e22871"
            ],
            "query": topic
        }
    }
    
    headers = {
        'x-api-key': API_KEY
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        questions_text = json.loads(response_data['message']['content'])['llm']
        
        # Parse the questions and answers
        questions = []
        current_question = None
        current_options = []
        
        for line in questions_text.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            if line.startswith(('A)', 'B)', 'C)', 'D)')):
                current_options.append(line)
            elif line.startswith('**Correct Answer:'):
                correct_answer = line.split('**Correct Answer:')[1].strip()
                # Remove any trailing '**' and whitespace
                if correct_answer.endswith('**'):
                    correct_answer = correct_answer[:-2].strip()
                if current_question and current_options:
                    questions.append({
                        'question': current_question,
                        'options': current_options,
                        'correct_answer': correct_answer
                    })
                current_question = None
                current_options = []
            elif not line.startswith('**'):
                current_question = line
        
        return jsonify({'questions': questions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_study_guide', methods=['POST'])
def get_study_guide():
    incorrect_questions = request.json.get('incorrect_questions', [])
    
    if not incorrect_questions:
        return jsonify({'error': 'No incorrect questions provided'}), 400
    
    # Take the first question (since we're now sending one at a time)
    query = incorrect_questions[0]
    
    url = "https://egp.dashboard.scale.com/api/v4/applications/451b14b6-b46a-47f8-bca0-94d00ae69be8/process"
    
    payload = {
        "inputs": {
            "knowledge_base_ids": [
                "9947842f-ddd7-4a73-b2c0-227c79e22871"
            ],
            "query": query
        }
    }
    
    headers = {
        'x-api-key': API_KEY
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        study_guide = json.loads(response_data['message']['content'])['llm']
        
        return jsonify({'study_guide': study_guide})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 
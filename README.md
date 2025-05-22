# Wine Study Quiz App

A web application that generates wine-related quizzes and provides study guides for incorrect answers.

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your API key:
   ```
   API_KEY=your_api_key_here
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Deployment to Render

1. Create a free account on [Render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure the service:
   - Name: wine-study-quiz (or your preferred name)
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Add your environment variable:
   - Key: `API_KEY`
   - Value: Your API key
6. Click "Create Web Service"

Your application will be deployed and available at `https://your-app-name.onrender.com`

## Environment Variables

- `API_KEY`: Your Scale API key for accessing the question and study guide generation services 
# Mood Analyzer

Mood Analyzer is a web application that allows you to analyze the mood of any text you provide. It uses OpenAI's GPT-3 model to perform sentiment analysis and provides you with the predicted mood of the text.

## Features

- Analyze the mood of any text input.
- Predict whether the text's mood is positive, negative, or neutral.
- User authentication system for signup and login.
- Securely store user data in a MongoDB database.

## Tech stack

- Flask: A lightweight Python web framework.
- Flask-PyMongo: MongoDB integration for Flask.
- OpenAI API: Used for text analysis.
- HTML, CSS, and JavaScript for the frontend.
- MongoDB ATLAS for storing user data

## Setup

Follow these steps to set up and run Mood Analyzer on your local machine:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sharunnd/mood-analyzer.git
   cd mood-analyzer

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   
4. **Set Environment Variables:**
   Create a .env file in the project root directory and add the following variables:
   ```bash
   MONGO_URI=your_mongodb_connection_string
   SECRET_KEY=your_secret_key_for_sessions
   OPENAI_API_KEY=your_openai_api_key

5. **Run the Application:**
   ```bash
   python run.py

6. **Access the Application:**
   Open a web browser and go to http://localhost:5000
   
### Usage
  Enter text in the provided textarea.
  Click the "Analyze" button.
  The predicted mood of the text will be displayed.

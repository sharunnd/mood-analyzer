from flask import Blueprint, render_template,render_template, redirect, url_for, flash,request
from .forms import SignupForm,LoginForm
from . import app,mongo
import bcrypt
import os


dashboard_bp = Blueprint('dashboard', __name__)



@app.route('/', methods=['GET', 'POST'])
def dashboard():
    mood_result = None
    error_message = None

    if request.method == 'POST':
        text = request.form['text']

        try:
            import openai
            openai.api_key = os.getenv('OPENAI_API_KEY')
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Analyze the mood of the following text: '{text}' and predict whether the mood of the text is Positive, Negative, or Neutral.",
                max_tokens=50,
                temperature=1.2
            )
            mood_result = response.choices[0].text.strip()

            # Redirect to a new route with the mood analysis result
            return redirect(url_for('mood_result_page', mood_result=mood_result))

        except Exception as e:
            print(f"Error: {e}")
            error_message = "Error occurred during analysis. Please try again later."

    return render_template('index.html', mood_result=mood_result, error_message=error_message)


@app.route('/result')
def mood_result_page():
    mood_result = request.args.get('mood_result', 'No result')  # Get mood_result from the URL parameter
    return render_template('result.html', mood_result=mood_result)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    error_message = None

    if form.validate_on_submit():
        try:
            username = form.username.data
            password = form.password.data

            # Check if the username already exists in the database
            existing_user = mongo.db.users.find_one({'username': username})
            if existing_user:
                flash('Username already exists. Please choose a different username.', 'error')
                return redirect(url_for('signup'))

            # Hashing the password before storing it
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Create a new user document with hashed password
            new_user = {
                'username': username,
                'password': hashed_password.decode('utf-8')  # Decode the bytes to store as a string
            }
            mongo.db.users.insert_one(new_user)

            flash('Account created successfully! You can now log in.', 'success')
            return redirect(url_for('login'))  # Assuming you have a login route

        except Exception as e:
            print(f"Error: {e}")
            error_message = "Error occurred during signup. Please try again later."

    return render_template('signup.html', form=form, error=error_message)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error_message = None

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check if the username exists in the database
        existing_user = mongo.db.users.find_one({'username': username})
        if existing_user and bcrypt.checkpw(password.encode('utf-8'), existing_user['password'].encode('utf-8')):
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to the dashboard or another secure page after login
        else:
            error_message = 'Invalid username or password. Please try again.'

    return render_template('login.html', form=form, error=error_message)



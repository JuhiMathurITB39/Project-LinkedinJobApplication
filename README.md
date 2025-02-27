#LinkedIn Job Application Bot  
Automate your LinkedIn job applications using Selenium and Python.  
This bot logs in, navigates to Easy Apply jobs, fills in details, and submits applications—saving you hours of manual work!  

## Features  
Automatically logs into LinkedIn  
Scrapes job listings with Easy Apply  
Auto-fills phone number  
Skips complex applications requiring additional inputs  
Secure login using environment variables (.env)  
Simple one-time setup  

## Project Structure  
linkedin-job-bot/ │-- linkedin_bot.py # Main script for automation │-- requirements.txt # Dependencies │-- .gitignore # Prevents sensitive files from uploading │-- README.md # Project documentation └── .env (Do NOT upload) # Stores LinkedIn credentials

## Installation & Setup  

### 1️ Clone the Repository  
git clone https://github.com/your-username/linkedin-job-bot.git
cd linkedin-job-bot

2️ Install Dependencies
Make sure you have Python 3.8+ installed, then run:
pip install -r requirements.txt

3️ Set Up Environment Variables
Create a .env file inside the project folder and add your LinkedIn login details:
LINKEDIN_EMAIL=your-email@example.com
LINKEDIN_PASSWORD=your-password
PHONE_NUMBER=your-phone-number

4️ Run the Bot
python linkedin_bot.py

How It Works
1 Opens LinkedIn and logs in
2️ Navigates to Python Developer jobs in India
3️ Clicks Easy Apply on job listings
4️ Fills in the phone number (if empty)
5️ Submits the application
6️ Closes the pop-up and moves to the next job

Notes
CAPTCHA Handling: The bot pauses after login for manual CAPTCHA solving.
Easy Apply Only: The bot applies only to jobs with the Easy Apply button.
Customization: You can change job titles, locations, or automation behavior by modifying the script.

Troubleshooting
Bot not working?
Ensure Google Chrome is installed.
Update chromedriver by running:
pip install --upgrade webdriver-manager

If CAPTCHA appears, manually solve it and continue.

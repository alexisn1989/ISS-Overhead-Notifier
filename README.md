🛸 ISS Overhead Notifier
A Python automation app that tracks the International Space Station
and sends you an email notification when it passes over Virginia Beach at night!
📋 About
This project combines two real world APIs to track the ISS position
in real time and check if it's currently nighttime at your location.
When both conditions are true — ISS is overhead AND it's dark outside —
you get an email so you can go outside and spot it with the naked eye!
✨ Features

🛸 Real time ISS position tracking
🌅 Automatic sunrise/sunset detection
📧 Email notification when ISS is visible
🔄 Checks every 60 seconds automatically
📍 Configured for Virginia Beach, VA

🖥️ Example Output
Checking ISS position...
ISS is overhead and it's dark! Sending email...
Email sent! 🛸

Subject: Look Up! 🛸
The ISS is overhead in Virginia Beach right now!
Go outside and look up!
🛠️ Built With

Python 3
Requests library
smtplib (built into Python)
datetime (built into Python)
Open Notify API — ISS position
Sunrise Sunset API — daylight detection

🌐 APIs Used

ISS Location: http://api.open-notify.org/iss-now.json
Sunrise/Sunset: https://api.sunrisesunset.io/json

🚀 How to Run

Make sure Python is installed
Install requests:

pip install requests

Set up environment variables:

MY_EMAIL=your_gmail@gmail.com
MY_PASSWORD=your_app_password

Clone this repository:

git clone https://github.com/alexisn1989/iss-overhead-notifier

Run the program:

python main.py
📁 Project Structure
iss-overhead-notifier/
└── main.py  ← main program
📦 Requirements
requests
🔒 Security
This project uses environment variables to protect email credentials.
Never hardcode passwords in your code!
Create a .env file:
MY_EMAIL=your_email_here
MY_PASSWORD=your_app_password_here
💡 What I Learned

Working with multiple APIs simultaneously
Real time data tracking with while loops
Time based conditions with datetime
Automated email notifications with smtplib
Environment variables for security
Geographic coordinate comparisons
Parsing time strings from API responses
Scheduling checks with time.sleep()

👨‍💻 Author
Alexi — Aspiring Python Developer
Currently completing Angela Yu's 100 Days of Code bootcamp
📍 Virginia Beach, VA | Open to remote opportunities
🔗 LinkedIn: your-linkedin-url
🐙 GitHub: github.com/alexisn1989

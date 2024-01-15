# ISS Tracker and Notifier
## Overview
Hello everyone! I'm Mert, and today is Day 33 of my "100 Days of Python" challenge. In this project, I've developed an ISS Tracker and Notifier using Python. This script tracks the International Space Station (ISS) and sends an email notification if the ISS is overhead and it is nighttime at your location.

## Project Description
The ISS Tracker and Notifier script use the Open Notify API to get the current location of the ISS and the Sunrise-Sunset API to check if it is nighttime at your location. If the ISS is overhead and it is nighttime, it sends an email notification.

## Requirements
Before running the script, make sure you have the required Python packages installed. You can install them using the following command:

```bash
pip install requests
```
## Configuration
Set the following parameters in the script:

* MY_LAT: Your latitude.
* MY_LONG: Your longitude.
* MY_EMAIL: Your Gmail email address.
* PASSWORD: Your Gmail email application password.
* RECEIVER: The email address to receive notifications.
  
## How to Run
Run the script using the following command:

```bash
python main.py
```
## How it Works
The script checks if the ISS is overhead and if it is nighttime at your location. If both conditions are met, it sends an email notification.

## Important Note
For security reasons, it is recommended to use an application-specific password for your Gmail account and not your main account password.

## Auto Task Scheduling
You can also set daily tasks and make them automatic by installing this program at PythonAnywhere.

## Contributing
Feel free to contribute to the project by opening issues or creating pull requests.

# Educational Insights
This project provides hands-on experience with key Python concepts:

* API Integration: Using the Open Notify and Sunrise-Sunset APIs.
* Email Sending: Using smtplib to send email notifications.
* Time Handling: Checking if it is nighttime based on the user's location.
## Conclusion
I hope you find the ISS Tracker and Notifier helpful for tracking the ISS and receiving notifications! It's been a great journey reaching Day 33, and I'm excited to continue exploring and learning. Happy coding!

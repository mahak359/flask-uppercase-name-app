# flask-uppercase-name-app
Flask app that converts user name from URL into uppercase with bonus features
# Flask Name Utilities App

This is a simple Flask web application that takes a user name from the URL query parameter and performs different string operations like greeting, converting to uppercase, and reversing the name.

The project demonstrates how query parameters work in Flask and how multiple routes can be used to build useful web utilities.

---

## Available Endpoints

### 1. Greeting
http://127.0.0.1:5000/greet?name=mahak  
Displays a friendly greeting with the given name.

### 2. Shout (Uppercase)
http://127.0.0.1:5000/shout?name=mahak  
Converts the name into UPPERCASE and displays it.

### 3. Reverse
http://127.0.0.1:5000/reverse?name=mahak  
Reverses the given name and displays it.

---

## Example

URL:
http://127.0.0.1:5000/shout?name=mahak  

Output:
MAHAK  

URL:
http://127.0.0.1:5000/reverse?name=mahak  

Output:
kaham  

---

## How to Run the App

1. Install Flask  
pip install flask  

2. Run the application  
python app3.py  

3. Open your browser and visit any of the URLs above.

---

## Technologies Used

Python  
Flask  
HTML rendered through Flask  

---

## Purpose

This project is a beginner-friendly Flask application designed to demonstrate how to use query parameters, create multiple routes, and perform basic string operations in a web application. It is ideal for learning Flask and for showcasing on GitHub or in internship portfolios.


from flask import Flask, request
import random

app = Flask(__name__)

# Main route: Converts name to UPPER CASE and displays it
@app.route('/greet')
def greet():
    name = request.args.get('name')
    if not name:
        return "<h1>Error: Please provide a 'name' query parameter, e.g., /greet?name=John</h1>"
    upper_name = name.upper()
    return f"<h1>Hello, {upper_name}!</h1><p>Your name in UPPER CASE: {upper_name}</p>"

# Bonus creative route 1: "Shout" the name with random emojis and excitement
@app.route('/shout')
def shout():
    name = request.args.get('name')
    if not name:
        return "<h1>Error: Please provide a 'name' query parameter, e.g., /shout?name=John</h1>"
    upper_name = name.upper()
    emojis = ["🔥", "🚀", "💥", "🌟", "😎", "🎉"]
    random_emoji = random.choice(emojis)
    return f"<h1>{upper_name}!!! {random_emoji}</h1><p>Shouting your name loud and proud!</p>"

# Bonus creative route 2: Reverse the name, uppercase it, and add a fun twist
@app.route('/reverse')
def reverse():
    name = request.args.get('name')
    if not name:
        return "<h1>Error: Please provide a 'name' query parameter, e.g., /reverse?name=John</h1>"
    reversed_name = name[::-1].upper()
    return f"<h1>Reversed and UPPER CASE: {reversed_name}</h1><p>Whoa, {name} backwards is {reversed_name}! Time travel much? 🕰️</p>"

if __name__ == '__main__':
    app.run(debug=True)
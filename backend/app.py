from flask import Flask, render_template
import os

# Set path to the templates folder relative to app.py
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('code.html')  # Render the HTML page

if __name__ == '__main__':
    app.run(debug=True)

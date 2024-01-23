import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import send_from_directory

app = Flask(__name__)

MEDIA_FOLDER = '/home/yencarnacion/daytrading'  # Set your path here
app.config['MEDIA_FOLDER'] = MEDIA_FOLDER

@app.route('/')
def index():
    files = [f for f in os.listdir(app.config['MEDIA_FOLDER']) if f.endswith('.mp4')]
    return render_template('index.html', files=files)

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['MEDIA_FOLDER'], filename)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

